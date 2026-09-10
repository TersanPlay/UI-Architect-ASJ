from pathlib import Path
import re

path = Path("SKILL.md")
text = path.read_text(encoding="utf-8")

# 1) Canonical principle: add classification and make contract wording explicit.
text = text.replace(
    "**Entender → inspecionar → pesquisar → comparar → sintetizar → contratar → selecionar → adaptar → implementar → validar → refinar.**",
    "**Entender → inspecionar → classificar → pesquisar → comparar → sintetizar → definir o contrato → selecionar → adaptar → implementar → validar → refinar.**",
)

# 2) Canonical execution sequence before technical inspection.
canonical_heading = "# Sequência canônica de execução"
if canonical_heading not in text:
    marker = "# Fase 0 — Inspeção do projeto\n"
    block = r'''# Sequência canônica de execução

A sequência abaixo governa tarefas relevantes de criação, redesign e refatoração. Ela é um **contrato de execução**, não um formato obrigatório de resposta ao usuário.

1. **Problema** — registrar objetivo, escopo, fluxos que precisam ser preservados e qualquer autorização explícita para mudar produto ou regra de negócio.
2. **Modo de trabalho** — classificar como criar, refatorar, reproduzir, melhorar ou componente isolado.
3. **Referências** — selecionar somente fontes úteis ao problema.
4. **Padrão de UX** — definir arquitetura, hierarquia, densidade, fluxo e comportamento.
5. **Design Contract** — fixar Hard Rules, Banned Patterns, Required Regions, responsividade, acessibilidade, motion e performance.
6. **Seleção** — escolher primitives, componentes e padrões com menor custo de integração.
7. **Adaptação** — normalizar tudo ao Design System e aos contratos existentes.
8. **Implementação** — preservar negócio, dados, permissões e comportamento não autorizado a mudar.
9. **Validação** — verificar página completa, região alterada, estados, breakpoints e fluxos preservados com evidência proporcional ao escopo.

Uma mudança de endpoint, payload, permissão, regra de negócio, persistência, fluxo ou contrato de dados **só pode ser tratada como parte do redesign se tiver sido explicitamente autorizada e registrada no Problema antes da implementação**.

---

'''
    if marker not in text:
        raise SystemExit("Fase 0 marker not found")
    text = text.replace(marker, block + marker, 1)

# 3) Shared primitives and scoped styling contract.
primitive_heading = "# Regra de primitives compartilhadas e escopo de estilos"
if primitive_heading not in text:
    marker = "# Regras de adoção de componente externo\n"
    block = r'''# Regra de primitives compartilhadas e escopo de estilos

Quando o projeto já possuir uma primitive compartilhada — como Button, Checkbox, Switch, Select, Dialog, Input, Table ou equivalente — **não crie uma cópia local apenas para acomodar o redesign**.

Prioridade:

1. reutilizar a primitive existente;
2. usar uma variante oficial da primitive;
3. ampliar a API da primitive somente quando a mudança for reutilizável e o impacto global estiver mapeado;
4. aplicar composição ou wrapper local quando o comportamento for específico da tela;
5. criar nova primitive apenas quando existir uma diferença semântica ou funcional real.

Não altere uma primitive global para resolver um problema local sem avaliar o **blast radius**.

Estilos específicos devem ser isolados por componente, variante, classe ou escopo previsível. Evite seletores genéricos como `input`, `button`, `[role="switch"]`, `.card` ou equivalentes quando puderem contaminar outras primitives e páginas.

Um redesign não pode corrigir uma tela quebrando silenciosamente outra.

---

'''
    if marker not in text:
        raise SystemExit("external component marker not found")
    text = text.replace(marker, block + marker, 1)

# 4) Truthful affordance rule before form guidance.
affordance_heading = "# Regra de verdade da interface — sem falsa affordance"
if affordance_heading not in text:
    marker = "# Formulários\n"
    block = r'''# Regra de verdade da interface — sem falsa affordance

Todo elemento que **parece interativo, editável, persistente ou mensurável deve produzir a consequência que comunica**.

A Skill não pode:

- transformar informação somente leitura em campo com aparência editável sem existir edição real;
- criar toggle, checkbox, botão, menu ou CTA sem ação correspondente quando apresentado como funcional;
- indicar “salvo”, “ativo”, “sincronizado”, “enviado”, “concluído” ou estado equivalente sem evidência do estado real;
- criar filtros que não alteram os dados;
- criar paginação ou ordenação apenas visual;
- inventar métricas, permissões ou estados para preencher layout;
- mostrar autosave se a aplicação exige salvamento explícito;
- ocultar uma limitação de API com uma affordance visual falsa.

Se um controle existir apenas como demonstração, protótipo ou placeholder, isso deve estar claramente delimitado e não pode ser apresentado como comportamento de produção.

---

'''
    if marker not in text:
        raise SystemExit("forms marker not found")
    text = text.replace(marker, block + marker, 1)

# 5) Critical actions contract before tables.
critical_heading = "# Ações críticas, destrutivas e de alto impacto"
if critical_heading not in text:
    marker = "# Tabelas e interfaces de dados\n"
    block = r'''# Ações críticas, destrutivas e de alto impacto

Ações de risco não podem possuir a mesma hierarquia visual e o mesmo fluxo de confirmação de uma ação comum.

Considere como críticas, conforme o domínio:

- excluir ou apagar dados;
- restaurar backup;
- redefinir senha de outra pessoa;
- revogar acesso;
- alterar permissões sensíveis;
- bloquear ou desativar entidade;
- substituir dados existentes;
- operações irreversíveis ou de grande alcance.

A interface deve comunicar, de forma proporcional ao risco:

- **contexto** — o que está sendo alterado;
- **consequência** — o que acontecerá depois da ação;
- **escopo** — quais registros, usuários ou recursos serão afetados;
- **reversibilidade** — se existe desfazer, restauração ou recuperação;
- **confirmação** — somente quando o risco justificar;
- **feedback** — sucesso, falha e estado em andamento de forma inequívoca.

Não use confirmação pesada para ações triviais, mas também não reduza operações destrutivas a um clique indistinguível de ações comuns.

---

'''
    if marker not in text:
        raise SystemExit("table marker not found")
    text = text.replace(marker, block + marker, 1)

# 6) Verifiable-result contract immediately before visual validation.
result_heading = "# Contrato de resultado final verificável"
if result_heading not in text:
    marker = "# Validação visual\n"
    block = r'''# Contrato de resultado final verificável

Redesign não é autorização implícita para mudar produto. O resultado deve ser visualmente melhor **sem mascarar ou alterar contratos funcionais que estavam fora do escopo**.

## A Skill não pode

Em redesigns e refatorações, salvo autorização explícita registrada no Problema, a Skill não pode alterar apenas para acomodar a solução visual:

- endpoints ou rotas de API;
- payloads, nomes de campos ou contratos de dados;
- permissões, papéis ou regras de acesso;
- regras de negócio;
- persistência e efeitos colaterais;
- ordenação;
- paginação;
- filtros e parâmetros de URL;
- importação ou exportação;
- locale;
- timezone;
- representação persistida de datas, valores ou identificadores;
- comportamento de submissão de formulários;
- fluxos críticos já existentes.

Também não pode:

- redesenhar áreas fora do escopo sem necessidade funcional clara;
- substituir primitives compartilhadas por clones locais sem justificativa;
- aplicar estilos genéricos que contaminem outras primitives;
- criar falsa affordance;
- declarar validação visual, funcional ou de acessibilidade que não foi executada;
- transformar `build`, `lint`, testes unitários ou TypeScript sem erros em prova de QA visual;
- esconder como “aprovado” um fluxo que permaneceu sem inspeção por limitação do ambiente.

## O resultado final deve

Uma entrega relevante só pode ser considerada concluída quando, proporcionalmente ao escopo:

- preserva fluxos, contratos de dados e permissões mapeados, ou enumera objetivamente as mudanças autorizadas;
- parece parte do Design System e do shell existentes, sem colagem visual ou técnica;
- comunica prioridade, risco, estado, persistência e consequência de forma verdadeira;
- possui estratégia responsiva definida para tabelas, filtros, tabs, dialogs, sidebars, formulários e ações críticas relevantes;
- opera com semântica adequada, teclado, foco visível, contraste, feedback textual e reduced motion;
- mantém comportamento correto nos estados relevantes, incluindo loading, empty, error, success, disabled e permission denied quando aplicável;
- foi verificada tanto na **página completa** quanto na **região alterada**;
- foi verificada nos breakpoints relevantes ao escopo;
- teve os fluxos que precisavam ser preservados exercitados quando o ambiente permitiu;
- não apresenta erros de console relacionados ao fluxo validado quando houver acesso a navegador/console;
- registra explicitamente tudo que não pôde ser verificado.

## Evidência proporcional ao escopo

Use evidência adequada ao tipo de afirmação:

- **estrutura/código** → diff, inspeção de implementação, lint, TypeScript, build e testes automatizados;
- **visual** → página renderizada e inspeção da região alterada nos viewports relevantes;
- **funcional** → execução do fluxo, eventos, persistência e efeitos esperados;
- **acessibilidade** → teclado, foco, labels, semântica, contraste e comportamento do overlay/controle;
- **responsividade** → verificação dos breakpoints e transformações estruturais relevantes.

Quando forem produzidas capturas ou outros artefatos de QA que sustentem aprovação, prefira evidências duráveis no PR, relatório ou artefato de revisão. Se a evidência permanecer temporária, registre essa limitação.

## Status da validação

Use a semântica abaixo por dimensão de validação quando houver relatório, QA ou entrega que declare status:

- **`passed`** — a verificação correspondente foi realmente executada e o critério foi atendido;
- **`partial`** — parte dos critérios foi executada; declare objetivamente o que passou e o que permanece sem validação;
- **`pending`** — a verificação não pôde ser executada por limitação de ambiente, ferramenta, acesso, dados ou dependência.

Regras:

- `passed` nunca pode ser inferido de ausência de erro em uma camada diferente;
- build aprovado não significa QA visual aprovado;
- TypeScript aprovado não significa fluxo funcional aprovado;
- teste de segurança aprovado não significa teclado ou responsividade aprovados;
- ausência de navegador significa validação visual `pending` ou `partial`, não `passed`;
- uma limitação deve permanecer explícita até que a verificação correspondente seja executada.

---

'''
    if marker not in text:
        raise SystemExit("visual validation marker not found")
    text = text.replace(marker, block + marker, 1)

# 7) Strengthen overlay focus restoration in accessibility guidance.
old = "- dialogs com foco controlado;\n- menus operáveis por teclado;"
new = "- dialogs e overlays com foco controlado e restauração de foco ao elemento de origem quando fechados;\n- menus operáveis por teclado;"
text = text.replace(old, new)

# 8) Add verifiable-result checks to pre-flight.
preflight_heading = "## Fidelidade funcional e validação verificável"
if preflight_heading not in text:
    marker = "## Estados\n\n- [ ] Hover existe quando apropriado.\n"
    block = r'''## Fidelidade funcional e validação verificável

- [ ] Endpoints, payloads, permissões, regras de negócio, persistência, ordenação, paginação, exportação, locale e timezone foram preservados, salvo mudança explicitamente autorizada.
- [ ] Não existe falsa affordance: todo controle funcional produz a consequência comunicada.
- [ ] Primitives compartilhadas foram reutilizadas ou alteradas com impacto mapeado; não há clone local arbitrário.
- [ ] Estilos específicos não contaminam primitives e páginas fora do escopo.
- [ ] Ações críticas comunicam contexto, consequência, escopo, reversibilidade e feedback proporcional ao risco.
- [ ] Página completa e região alterada foram verificadas quando o ambiente permitiu.
- [ ] Breakpoints, estados e fluxos relevantes foram exercitados proporcionalmente ao escopo.
- [ ] `passed`, quando utilizado, corresponde a uma verificação realmente executada.
- [ ] Verificações não executadas estão marcadas como `partial` ou `pending`.
- [ ] Build/lint/TypeScript não foram usados como substitutos de QA visual ou funcional.
- [ ] Erros de console relacionados ao fluxo foram verificados quando havia navegador/console disponível.
- [ ] Evidências que sustentam aprovação são duráveis quando possível, ou sua natureza temporária foi registrada.

'''
    if marker not in text:
        raise SystemExit("preflight states marker not found")
    text = text.replace(marker, block + marker, 1)

# 9) Remove the legacy "Formato de resposta" section to avoid treating the canonical sequence as a writing format.
text = re.sub(
    r"\n# Formato de resposta da Skill\n.*?\n---\n\n# Exemplo — Dashboard de gerenciamento de usuários\n",
    "\n# Exemplo — Dashboard de gerenciamento de usuários\n",
    text,
    flags=re.S,
)

path.write_text(text, encoding="utf-8")
