# Modern Form Controls — Regra de implementação

## Objetivo

Evitar que controles de formulário complexos sejam entregues com a aparência nativa/padrão do navegador quando houver uma alternativa moderna, acessível e compatível com o Design System.

Esta regra se aplica especialmente a:

- `select`;
- combobox;
- autocomplete;
- calendários;
- `input[type="date"]` quando sua UI nativa ficar visível como solução final;
- date pickers;
- date-range pickers;
- time pickers;
- dropdowns;
- popovers de escolha;
- multi-select;
- componentes equivalentes de seleção complexa.

## Regra principal

**Não entregar componentes nativos visuais do navegador como solução final para controles complexos quando houver um componente moderno equivalente adequado ao projeto.**

Preserve semântica, acessibilidade e comportamento funcional, mas substitua a aparência e a experiência nativa por um componente moderno alinhado ao Design System.

## Prioridade de implementação

1. Reutilizar primeiro um componente moderno já existente no projeto.
2. Se o projeto usa shadcn/ui ou Radix UI, preferir primitives adequadas como Select, Combobox, Popover, Calendar e Dialog/Drawer quando fizer sentido.
3. Pesquisar no 21st.dev alternativas compatíveis quando não existir componente local apropriado.
4. Consultar Refero para padrões maduros de UX em seleção, filtros, datas e formulários complexos.
5. Usar React Bits ou Componentry apenas para polish/microinteração e nunca para substituir a ergonomia principal do controle.
6. Adicionar nova dependência somente quando a solução existente não for suficiente.

## Requisitos obrigatórios

A substituição deve:

- evitar aparência padrão/nativa do navegador;
- utilizar componentes modernos com melhor UX;
- preservar todas as funcionalidades existentes;
- preservar valores, validação, eventos, submissão, filtros e integração com formulários;
- manter responsividade em desktop, tablet e mobile;
- preservar navegação por teclado;
- possuir `focus-visible` claro;
- manter labels e descrição acessíveis;
- usar ARIA apenas quando necessário e corretamente;
- manter estados `default`, `hover`, `focus`, `open`, `selected`, `disabled`, `invalid` e `loading` quando aplicáveis;
- manter consistência visual entre select, calendário, date picker e demais controles;
- respeitar tokens de cor, radius, spacing, typography, border, shadow e motion do Design System;
- preservar a lógica de negócio e o comportamento funcional existente;
- não alterar formatos, regras de datas, timezone, filtros ou valores sem necessidade funcional explícita.

## Semântica nativa vs aparência nativa

Esta regra **não proíbe HTML nativo como fundamento semântico**.

É permitido manter elementos nativos quando eles forem importantes para:

- formulários;
- submissão;
- progressive enhancement;
- integração com bibliotecas;
- fallback;
- acessibilidade.

O que deve ser evitado é deixar a **UI nativa padrão do navegador** como experiência final quando ela conflita com o Design System ou oferece UX inferior.

Exemplo:

- um `input` hidden pode preservar valor e integração do formulário;
- um trigger moderno pode abrir um Calendar acessível;
- um Select/Combobox moderno pode substituir visualmente um `<select>` nativo;
- fallback nativo pode permanecer disponível quando necessário.

## Select / Combobox

Preferir componente moderno que suporte, conforme a necessidade:

- teclado;
- busca;
- opções desabilitadas;
- grupos;
- estados selecionados;
- scroll de lista;
- empty state;
- clear action;
- multi-select quando necessário;
- portal/popover com posicionamento seguro;
- mobile adequado.

Não recriar manualmente um select complexo com `div` + listeners se uma primitive acessível já existir.

## Calendar / Date Picker

O componente moderno deve considerar:

- locale;
- formato exibido;
- timezone quando relevante;
- data mínima/máxima;
- datas indisponíveis;
- seleção única ou range;
- navegação de mês/ano;
- teclado;
- foco;
- botão de limpar quando apropriado;
- estado inválido;
- mobile.

Em mobile, avaliar se Popover, Drawer, Sheet ou Dialog fornece melhor ergonomia sem alterar a lógica funcional.

## Aparência Turquoise Architect ASJ

Quando o preset Turquoise Architect ASJ estiver ativo:

- controles devem ter geometria retangular/sutilmente arredondada, não pill extrema;
- radius recomendado: `8px–12px`;
- popovers/calendários: aproximadamente `10px–16px`, conforme hierarquia;
- Primary: `#087F8C`;
- Primary Dark: `#075E67`;
- Soft Blue: `#DCEFF0`;
- superfícies: warm white/cream;
- texto: off-black;
- focus ring: turquesa;
- dourado `#C89B5B` somente para detalhes premium, nunca como estado padrão de formulário.

## Banned

Evitar:

- `<select>` com aparência padrão do sistema como UI final;
- `input[type="date"]` exibindo calendário nativo quando o produto exige UI consistente;
- date picker desktop quebrado em telas pequenas;
- componente custom sem navegação por teclado;
- remover outline sem focus substituto;
- dropdown sem gerenciamento de foco;
- calendário que depende somente de cor para comunicar seleção;
- alterar timezone ou formato de dado apenas para encaixar o componente visual;
- substituir um controle estável por uma biblioteca pesada sem benefício real;
- componentes diferentes com radii, typography e estados incompatíveis.

## Exceções

Um controle nativo visível pode permanecer quando:

- o usuário pedir explicitamente;
- o projeto exigir native-first;
- requisitos de plataforma/dispositivo justificarem;
- acessibilidade ou compatibilidade for comprovadamente melhor com o nativo;
- não houver alternativa moderna confiável dentro das restrições técnicas.

A exceção deve ser uma decisão consciente, não o comportamento padrão.

## Pre-flight

- [ ] Nenhum select/date picker nativo ficou visível por descuido.
- [ ] O componente moderno preserva o mesmo valor e comportamento de negócio.
- [ ] Keyboard navigation funciona.
- [ ] Focus-visible está presente.
- [ ] Labels e erros permanecem associados.
- [ ] Estados disabled/invalid/selected/open estão claros.
- [ ] Mobile foi validado.
- [ ] Popover/dialog não corta conteúdo nem sai da viewport.
- [ ] O controle utiliza os mesmos tokens do restante da interface.
- [ ] Formato de data, locale e timezone não foram alterados indevidamente.
- [ ] Não foi adicionada dependência desnecessária.
- [ ] Existe fallback quando necessário.
