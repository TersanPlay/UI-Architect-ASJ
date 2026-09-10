# Scroll Motion — UI Architect ASJ

Este documento define quando e como usar animações dependentes de scroll na UI Architect ASJ.

> Observação: a biblioteca correta é **GSAP**, não “GASP”.

## Objetivo

Animações dependentes de scroll devem melhorar orientação, progressão narrativa, relação espacial, demonstração de produto ou percepção de continuidade. Elas não devem existir apenas para tornar a página mais chamativa.

A Skill deve escolher a técnica mais simples capaz de resolver o problema.

## Matriz de decisão

### 1. IntersectionObserver + CSS

Use quando o efeito for discreto e baseado em entrada/saída da viewport, por exemplo:

- reveal de seção;
- fade/translate de cards;
- ativação de estado ao entrar em viewport;
- animação que roda uma vez ou em poucos estados discretos.

Não use para scrub contínuo de progresso.

### 2. CSS Scroll-driven Animations

Use para efeitos simples cujo progresso acompanha diretamente o scroll, quando o suporte de navegador do projeto for suficiente.

Padrões possíveis:

- `animation-timeline: scroll()`;
- `animation-timeline: view()`;
- scroll progress;
- view progress;
- progress indicators;
- parallax muito leve;
- transformações simples ligadas à posição no viewport.

Como `animation-timeline`, `scroll()` e APIs relacionadas ainda podem ter suporte desigual entre navegadores, devem ser utilizadas com `@supports`, progressive enhancement e fallback apropriado quando compatibilidade ampla for requisito.

### 3. GSAP + ScrollTrigger

Use **GSAP ScrollTrigger** quando a animação exigir orquestração complexa ou controle preciso do progresso do scroll.

É a escolha preferencial para:

- `scrub`;
- `pin`;
- `snap`;
- timelines com vários elementos;
- sequências sincronizadas;
- z-axis cascade complexo;
- storytelling por scroll;
- product showcase com múltiplas etapas;
- mudanças coordenadas entre texto e visual;
- parallax controlado em múltiplas camadas;
- horizontal scroll intencional;
- callbacks de entrada/saída avançados;
- seções que precisam permanecer fixadas durante parte da narrativa.

Não adicione GSAP para um reveal que CSS + IntersectionObserver resolvem com clareza.

## GSAP ScrollTrigger — regras obrigatórias

- registrar `ScrollTrigger` explicitamente;
- usar `start` e `end` claros e previsíveis;
- usar `scrub` apenas quando o progresso realmente deve acompanhar o scroll;
- evitar `pin` em excesso;
- não animar diretamente o elemento que está sendo `pin` quando isso comprometer as medições; preferir animar filhos internos;
- não criar ScrollTriggers globais desnecessários;
- evitar listeners manuais de `scroll` quando ScrollTrigger ou APIs nativas resolvem melhor;
- usar markers somente em desenvolvimento;
- chamar `ScrollTrigger.refresh()` quando mudanças relevantes de layout exigirem recálculo;
- limpar timelines, triggers e listeners ao desmontar componentes.

## React + GSAP

Quando o projeto usar React:

- preferir `useGSAP()` de `@gsap/react` quando GSAP já fizer parte da solução;
- ou usar `gsap.context()` com cleanup explícito;
- escopar selectors ao componente por `ref`;
- executar `revert()` no cleanup;
- evitar criar novas timelines a cada render;
- mapear dependências do hook conscientemente;
- garantir que Strict Mode não duplique efeitos persistentes;
- usar `gsap.matchMedia()` para diferenças entre desktop, mobile e `prefers-reduced-motion`.

## Responsividade

Animação de scroll precisa possuir contratos separados para desktop e mobile quando a composição mudar estruturalmente.

Em telas pequenas:

- remover `pin` prolongado quando reduzir legibilidade ou causar scroll artificial;
- remover overlaps complexos;
- reduzir profundidade de parallax;
- evitar horizontal-scroll storytelling como única forma de acessar conteúdo;
- manter conteúdo no fluxo normal se o efeito for removido;
- garantir alvos de toque e scroll natural.

## Reduced motion

Toda experiência scroll-driven deve funcionar sem a animação.

Quando `prefers-reduced-motion: reduce` estiver ativo:

- eliminar ou reduzir scrub, parallax, scale e deslocamentos grandes;
- evitar pinning puramente decorativo;
- apresentar conteúdo em estado final legível;
- não esconder conteúdo aguardando um trigger de animação;
- preservar navegação e contexto.

Em GSAP, `gsap.matchMedia()` pode separar explicitamente a configuração com e sem motion.

## Scroll-jacking

Não substituir o comportamento de rolagem do navegador apenas para obter sensação cinematográfica.

Evite:

- bloquear wheel/touch sem necessidade;
- impedir a rolagem natural;
- controlar posição do usuário artificialmente;
- snap agressivo em conteúdo textual;
- smooth scroll obrigatório que altere ergonomia;
- efeitos que causem enjoo ou dificultem retorno visual.

Se smooth scrolling for usado, precisa preservar acessibilidade, teclado, âncoras, histórico e navegação natural.

## Performance

Priorize animações de:

- `transform`;
- `opacity`.

Use blur, filter e grandes camadas de composição com moderação.

Evite:

- animar layout continuamente;
- cálculos de `getBoundingClientRect()` em listeners de scroll sem controle;
- dezenas de observers ou timelines independentes para microelementos;
- múltiplos efeitos de parallax concorrentes;
- imagens sem dimensões estáveis dentro de seções pinned;
- `will-change` global.

## Debug e QA

Para animações dependentes de scroll, a validação deve considerar:

- entrada rápida e lenta na seção;
- scroll para frente e para trás;
- resize;
- conteúdo dinâmico;
- alteração de altura por fontes/imagens;
- navegação via âncora;
- refresh no meio da página;
- teclado;
- touch/mobile;
- reduced motion;
- ausência de layout jump;
- ausência de elementos presos após sair da seção;
- console sem warnings/erros relacionados à animação.

## Remotion — quando usar e quando não usar

**Remotion não é uma biblioteca principal para animação de scroll de páginas web.**

Remotion é voltado à criação programática de vídeos e motion graphics com React, incluindo renderização de vídeo, Player e aplicações de vídeo.

Use Remotion quando o objetivo for:

- gerar MP4/WebM;
- criar vídeo de demonstração do produto;
- produzir motion graphics;
- gerar vídeos parametrizados;
- incorporar uma experiência de vídeo controlável via Remotion Player;
- construir um editor ou pipeline de vídeo.

Não use Remotion para substituir:

- IntersectionObserver;
- CSS Scroll-driven Animations;
- GSAP ScrollTrigger;
- animações normais de componentes React;
- progressão visual dependente do scroll da página.

Se uma landing page precisar controlar a progressão de um vídeo pelo scroll, o controle de scroll continua pertencendo à camada de UI (por exemplo GSAP/ScrollTrigger ou outra técnica apropriada). Remotion pode produzir ou reproduzir a mídia, mas não deve ser escolhido como motor principal do scroll da página.

## Ordem preferencial da Skill

Escolha nesta ordem:

1. CSS/transitions para feedback simples;
2. IntersectionObserver para reveals discretos;
3. CSS Scroll-driven Animations para progresso simples quando compatibilidade permitir;
4. GSAP + ScrollTrigger para scroll complexo e coreografado;
5. Remotion somente quando o artefato principal for vídeo ou uma experiência de vídeo incorporada.

## Banned

- adicionar GSAP por padrão em toda landing page;
- usar Remotion como biblioteca de scroll motion;
- pinning prolongado sem justificativa narrativa;
- scrub em texto longo apenas por decoração;
- scroll-jacking;
- esconder conteúdo essencial até JavaScript executar;
- motion dependente de hover no mobile;
- ignorar `prefers-reduced-motion`;
- animação que deixa a UI em estado intermediário após resize;
- múltiplas bibliotecas de motion resolvendo o mesmo problema sem necessidade.

## Pre-flight — Scroll Motion

- [ ] A animação resolve um problema concreto de UX/narrativa.
- [ ] A técnica escolhida é a mais simples suficiente.
- [ ] IntersectionObserver foi preferido para reveal simples.
- [ ] CSS scroll timeline só foi usada com suporte/fallback adequado.
- [ ] GSAP foi reservado para orquestração realmente complexa.
- [ ] `pin`, `scrub` e `snap` possuem justificativa explícita.
- [ ] React possui cleanup correto.
- [ ] Mobile possui comportamento próprio quando necessário.
- [ ] Reduced motion foi implementado.
- [ ] O conteúdo continua acessível sem animação.
- [ ] Não existe scroll-jacking desnecessário.
- [ ] Performance foi inspecionada.
- [ ] Resize, back-scroll e refresh no meio da página foram considerados.
- [ ] Remotion não foi usado como motor de scroll da página.
