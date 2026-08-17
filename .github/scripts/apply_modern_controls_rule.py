from pathlib import Path

skill = Path("SKILL.md")
text = skill.read_text(encoding="utf-8")

section_marker = "# Tabelas e interfaces de dados\n"
section_title = "# Regra obrigatória — Controles modernos no lugar da aparência nativa\n"

section = """# Regra obrigatória — Controles modernos no lugar da aparência nativa

Controles complexos de formulário **não devem ser entregues com a aparência padrão/nativa do navegador como solução final** quando houver uma alternativa moderna, acessível e compatível com o Design System.

Esta regra se aplica especialmente a:

- `<select>`;
- combobox;
- autocomplete;
- calendários;
- `input[type=\"date\"]` quando sua UI nativa ficar visível como solução final;
- date pickers;
- date-range pickers;
- time pickers;
- dropdowns;
- multi-select;
- popovers de seleção;
- componentes equivalentes de seleção complexa.

Leia e aplique também:

- `references/modern-form-controls.md`

## Semântica nativa ≠ aparência nativa

Esta regra **não proíbe HTML nativo como fundamento semântico**.

É permitido manter elementos nativos quando eles forem úteis para:

- submissão de formulário;
- progressive enhancement;
- integração com bibliotecas;
- fallback;
- acessibilidade;
- armazenamento do valor real.

O que deve ser evitado é deixar a **aparência padrão do navegador** como experiência final quando ela conflita com o Design System ou oferece UX inferior.

Exemplos:

- um input nativo/hidden pode preservar valor e submissão;
- um trigger moderno pode abrir um Calendar acessível;
- Select/Combobox moderno pode substituir visualmente um `<select>`;
- fallback nativo pode permanecer quando necessário.

## Prioridade de implementação

1. Reutilize primeiro um componente moderno já existente no projeto.
2. Se o projeto usar shadcn/ui ou Radix UI, prefira primitives acessíveis adequadas.
3. Use 21st.dev para comparar alternativas de Select, Combobox, Calendar, Date Picker, Popover e controles equivalentes.
4. Use Refero para estudar UX madura de seleção, filtros e datas.
5. Use React Bits ou Componentry apenas para polish/microinteração, nunca como fundamento da ergonomia.
6. Adicione nova dependência somente quando a solução existente não for suficiente.

## A substituição deve

- evitar a aparência nativa/padrão do navegador;
- utilizar componente moderno com UX melhor ou mais consistente;
- preservar todas as funcionalidades existentes;
- preservar valor, validação, eventos, submissão, filtros e integração com formulários;
- garantir responsividade em desktop, tablet e mobile;
- preservar navegação por teclado;
- manter `focus-visible` claro;
- preservar labels, descrições e mensagens de erro;
- usar ARIA somente quando necessário e corretamente;
- contemplar estados `default`, `hover`, `focus`, `open`, `selected`, `disabled`, `invalid` e `loading` quando aplicáveis;
- manter consistência visual entre selects, calendários, date pickers e demais controles;
- usar os mesmos tokens de cor, typography, radius, border, shadow, spacing e motion da aplicação;
- preservar a lógica de negócio e o comportamento funcional existente;
- não alterar formato de dados, timezone, regras de data, filtros ou valores por conveniência visual.

## Select e Combobox

Quando aplicável, considerar suporte a:

- teclado;
- busca;
- grupos;
- opções desabilitadas;
- estado selecionado;
- empty state;
- clear action;
- scroll de lista;
- portal/popover com posicionamento seguro;
- multi-select;
- comportamento mobile adequado.

Não recrie manualmente um select complexo com `div` + listeners quando uma primitive acessível já existir.

## Calendar e Date Picker

Considere:

- locale;
- formato exibido;
- timezone quando relevante;
- data mínima/máxima;
- datas indisponíveis;
- seleção única ou range;
- navegação por mês/ano;
- teclado;
- gerenciamento de foco;
- clear action quando apropriado;
- estado inválido;
- comportamento mobile.

Em mobile, avalie Popover, Drawer, Sheet ou Dialog conforme a ergonomia, sem alterar a lógica funcional.

## Turquoise Architect ASJ

Quando o preset estiver ativo:

- controles devem ter aspecto predominantemente retangular/sutilmente arredondado;
- evitar pills extremas;
- radius de controles: aproximadamente `8px–12px`;
- popovers/calendários: aproximadamente `10px–16px`;
- Primary `#087F8C`;
- Primary Dark `#075E67`;
- Soft Blue `#DCEFF0`;
- superfícies warm white/cream;
- texto off-black;
- focus ring turquesa;
- dourado `#C89B5B` apenas em detalhe premium, nunca como estado padrão de formulário.

## Banned

Evite:

- `<select>` com aparência padrão do sistema como UI final sem justificativa;
- calendário nativo exposto por `input[type=\"date\"]` quando o produto exige consistência visual;
- componente custom sem navegação por teclado;
- remover outline/foco sem substituto;
- dropdown sem gerenciamento de foco;
- seleção comunicada somente por cor;
- date picker desktop quebrado em mobile;
- alterar timezone ou representação dos dados para encaixar o componente;
- adicionar biblioteca pesada apenas para trocar aparência;
- controles de formulário com geometrias e estados visualmente incompatíveis.

## Exceções

Um controle nativo visível pode permanecer quando:

- o usuário pedir explicitamente;
- o projeto exigir estratégia native-first;
- requisitos de plataforma ou dispositivo justificarem;
- acessibilidade ou compatibilidade for comprovadamente superior com o nativo;
- não houver alternativa moderna confiável dentro das restrições técnicas.

A exceção deve ser consciente e justificável, não o comportamento padrão.

---

"""

if section_title not in text:
    if section_marker not in text:
        raise SystemExit("section marker not found")
    text = text.replace(section_marker, section + section_marker, 1)

check_marker = "## Estados\n\n- [ ] Hover existe quando apropriado.\n"
check_title = "## Controles de formulário modernos\n"
checklist = """## Controles de formulário modernos

- [ ] Nenhum `select`, calendário ou date picker nativo ficou visível por descuido.
- [ ] Controles complexos usam componente moderno compatível com o Design System quando aplicável.
- [ ] Valor, validação, eventos e lógica de negócio foram preservados.
- [ ] Navegação por teclado funciona.
- [ ] `focus-visible` está claro.
- [ ] Labels e mensagens de erro continuam corretamente associados.
- [ ] Estados `open`, `selected`, `disabled` e `invalid` estão definidos quando aplicáveis.
- [ ] Selects, calendários e date pickers compartilham a mesma linguagem visual.
- [ ] Mobile foi validado.
- [ ] Locale, formato e timezone não foram alterados indevidamente.
- [ ] Não foi adicionada dependência desnecessária.

"""

if check_title not in text and check_marker in text:
    text = text.replace(check_marker, checklist + check_marker, 1)

skill.write_text(text, encoding="utf-8")
