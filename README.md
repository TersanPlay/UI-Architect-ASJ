# UI Architect ASJ

Skill especializada em **UI/UX + Frontend** para pesquisa, planejamento, composição, adaptação, implementação e validação de interfaces modernas para aplicações web.

O objetivo não é apenas melhorar aparência: em redesigns e refatorações, a Skill deve preservar contratos funcionais, dados, permissões, acessibilidade e comportamento existente, salvo mudança explicitamente autorizada.

## Fontes principais

- [React Bits](https://reactbits.dev) — efeitos, backgrounds e componentes animados.
- [Aceternity UI](https://ui.aceternity.com) — landing pages, seções e layouts de marketing.
- [21st.dev](https://21st.dev) — componentes e blocos React.
- [Componentry](https://componentry.dev) — microinterações e animações modernas.
- [Refero](https://refero.design) — padrões de UX e referências de produtos maduros.

## Princípio operacional

**Entender → inspecionar → classificar → pesquisar → comparar → sintetizar → definir o contrato → selecionar → adaptar → implementar → validar → refinar.**

A sequência canônica da Skill organiza o trabalho em:

1. Problema;
2. Modo de trabalho;
3. Referências;
4. Padrão de UX;
5. Design Contract;
6. Seleção;
7. Adaptação;
8. Implementação;
9. Validação.

Qualquer mudança de endpoint, payload, permissão, regra de negócio, persistência, fluxo ou contrato de dados deve ser explicitamente autorizada no **Problema** antes da implementação.

## Contrato de redesign

Em redesigns e refatorações, a Skill deve:

- preservar fluxos, dados, permissões e regras não autorizadas a mudar;
- evitar falsa affordance — todo controle funcional deve produzir a consequência comunicada;
- reutilizar primitives compartilhadas e isolar estilos específicos para evitar regressões;
- dar tratamento proporcional a ações críticas e destrutivas;
- definir comportamento responsivo para tabelas, filtros, dialogs, sidebars e controles relevantes;
- validar página completa, região alterada, estados, breakpoints e fluxos preservados quando o ambiente permitir;
- declarar limitações de validação em vez de inferir aprovação.

## Status de validação

Quando uma entrega declarar QA ou validação, use:

- **`passed`** — a verificação correspondente foi realmente executada e aprovada;
- **`partial`** — apenas parte dos critérios foi verificada;
- **`pending`** — a verificação não pôde ser executada por limitação de ambiente, ferramenta, acesso ou dependência.

Build, lint ou TypeScript sem erros **não equivalem** a QA visual ou funcional aprovado.

## Controles de formulário

A Skill evita entregar a aparência nativa do navegador como solução final para controles complexos quando houver alternativa moderna e acessível. Consulte [`references/modern-form-controls.md`](./references/modern-form-controls.md) para Select, Combobox, Calendar, Date Picker e controles equivalentes.

## Stack preferencial

Quando o projeto não definir outra stack:

- React
- TypeScript
- Vite
- React Router
- Tailwind CSS
- shadcn/ui
- Radix UI
- Lucide Icons

## Estratégia rápida

| Problema | Prioridade |
|---|---|
| Landing page | Aceternity UI → 21st.dev → Refero → React Bits → Componentry |
| Dashboard | Refero → 21st.dev → Aceternity UI |
| Sistema administrativo | Refero → 21st.dev |
| Animações | React Bits → Componentry |
| Componente específico | 21st.dev → React Bits → Componentry |
| UX SaaS | Refero → 21st.dev |

## Estrutura

```text
UI-Architect-ASJ/
├── SKILL.md
├── README.md
├── references/
│   ├── react-bits.md
│   ├── aceternity-ui.md
│   ├── 21st-dev.md
│   ├── componentry.md
│   ├── refero.md
│   └── modern-form-controls.md
└── examples/
    ├── dashboard.md
    ├── landing-page.md
    ├── admin-system.md
    ├── web-turquoise-Architect-ASJ.html
    └── web-turquoise-components-ASJ.html
```

O contrato completo de execução, Design System, preset **Turquoise Architect ASJ**, regras de redesign e pre-flight estão em [`SKILL.md`](./SKILL.md).
