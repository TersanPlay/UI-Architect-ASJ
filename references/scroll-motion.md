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

## Remotion — mídia audiovisual dentro da landing page

**Remotion não é a biblioteca principal para controlar o scroll da página, mas pode ser uma ferramenta oficial da UI Architect ASJ para produzir ou reproduzir animações e vídeos usados dentro da landing page.**

Use Remotion quando a página se beneficiar de uma peça audiovisual criada programaticamente em React, por exemplo:

- hero video curto demonstrando o produto;
- product demo animada;
- walkthrough de funcionalidades;
- motion graphics de marca;
- animação explicativa de processo;
- visualização animada de dados;
- mockup de interface em movimento;
- background motion discreto;
- loop visual em seção de feature;
- vídeo de lançamento ou prova de conceito;
- composição parametrizada por dados ou props.

A mídia deve reforçar a narrativa da landing, e não competir com headline, proposta de valor ou CTA.

### Estratégias de integração

Escolha conscientemente entre:

1. **Vídeo pré-renderizado** — Remotion produz MP4/WebM e a página incorpora o resultado com `<video>`. É a opção preferencial para conteúdo linear e não interativo.
2. **Remotion Player** — use quando a composição precisa permanecer React em runtime, receber props, mudar dinamicamente ou responder a controles da aplicação.
3. **Poster/frame estático** — use como fallback para reduced motion, conexões restritas, carregamento inicial ou quando a reprodução não for necessária.

Não carregue o runtime completo do Remotion apenas porque o vídeo foi produzido com Remotion. Se o resultado é linear, prefira exportar e servir a mídia otimizada.

### Hero video e product showcase

Quando a mídia aparecer no Hero ou em uma seção de produto:

- reserve `aspect-ratio` e dimensões para evitar CLS;
- use poster/frame inicial coerente;
- mantenha loops curtos e contínuos quando decorativos;
- preserve contraste e legibilidade de headline, lede e CTA;
- não dependa do vídeo para comunicar informação essencial;
- não reproduza áudio automaticamente;
- para autoplay decorativo, use `muted` e uma estratégia apropriada de reduced motion;
- para conteúdo essencial, forneça controles e alternativa textual/captions quando aplicável.

### Performance da mídia

- prefira MP4/WebM otimizado para web;
- use `preload="metadata"` ou `none` quando a mídia não for imediatamente necessária;
- carregue vídeo abaixo da dobra de forma preguiçosa quando apropriado;
- evite vários vídeos pesados reproduzindo simultaneamente;
- pause mídia fora da viewport quando isso reduzir custo sem prejudicar UX;
- mantenha dimensões estáveis;
- ajuste bitrate e resolução ao tamanho real de exibição;
- não use 4K em uma região pequena apenas por qualidade teórica;
- considere poster estático para dispositivos ou conexões modestos.

### Remotion + GSAP/ScrollTrigger

É permitido combinar as ferramentas quando a mídia fizer parte de uma narrativa dependente de scroll:

```text
Scroll da página
    ↓
GSAP / ScrollTrigger
    ↓ controla progresso/estado
Vídeo pré-renderizado ou Remotion Player
```

Casos válidos:

- product demo que avança com o scroll;
- texto sincronizado a momentos específicos da mídia;
- mídia pinned enquanto a narrativa progride;
- scroll controlando o tempo ou frame exibido.

Nessa arquitetura:

- **GSAP/ScrollTrigger governa a relação com a rolagem**;
- **Remotion produz ou reproduz a composição audiovisual**;
- a página deve continuar utilizável sem a sincronização;
- mobile e reduced motion devem possuir comportamento simplificado;
- scroll-jacking continua proibido por padrão.

Para vídeo pré-renderizado, a camada da página pode mapear progresso do scroll para o playback. Para Remotion Player, a integração da UI controla o progresso/estado do Player; a composição não deve esconder um mecanismo próprio de scroll.

### Quando não usar Remotion

Não use quando:

- CSS resolve a animação com poucas propriedades;
- o efeito é apenas hover, reveal ou microinteração;
- GSAP resolve diretamente os elementos DOM sem necessidade de timeline audiovisual;
- uma imagem comunica o mesmo conteúdo com melhor performance;
- o custo de vídeo/runtime é maior do que o ganho de comunicação.

### Acessibilidade e reduced motion

- conteúdo essencial não pode existir somente dentro do vídeo;
- forneça texto/caption equivalente quando necessário;
- não reproduza áudio automaticamente;
- respeite `prefers-reduced-motion`;
- em reduced motion, prefira poster, frame final ou versão estática;
- controles devem operar por teclado e possuir nomes acessíveis.

### QA de mídia Remotion na landing

Valide:

- carregamento inicial;
- poster/primeiro frame;
- autoplay quando utilizado;
- loop sem salto perceptível quando necessário;
- pause/play e controles quando aplicáveis;
- desktop, tablet e mobile;
- reduced motion;
- falha ou lentidão no carregamento;
- ausência de CLS;
- custo de CPU/GPU aceitável;
- legibilidade ao redor da mídia;
- sincronização scroll/mídia quando existir.

## Ordem preferencial da Skill

Escolha nesta ordem:

1. CSS/transitions para feedback simples;
2. IntersectionObserver para reveals discretos;
3. CSS Scroll-driven Animations para progresso simples quando compatibilidade permitir;
4. GSAP + ScrollTrigger para scroll complexo e coreografado;
5. Remotion quando a landing precisar de vídeo, motion graphics, product demo animada ou mídia React incorporada — sem usá-lo como motor de scroll.

## Banned

- adicionar GSAP por padrão em toda landing page;
- usar Remotion como biblioteca de scroll motion;
- carregar Remotion Player quando um MP4/WebM pré-renderizado resolve melhor;
- autoplay com áudio;
- mídia audiovisual que contém informação essencial sem alternativa textual;
- pinning prolongado sem justificativa narrativa;
- scrub em texto longo apenas por decoração;
- scroll-jacking;
- esconder conteúdo essencial até JavaScript executar;
- motion dependente de hover no mobile;
- ignorar `prefers-reduced-motion`;
- animação que deixa a UI em estado intermediário após resize;
- múltiplas bibliotecas de motion resolvendo o mesmo problema sem necessidade.

## Pre-flight — Scroll Motion e mídia

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
- [ ] Se Remotion produz mídia da landing, foi decidido entre pré-renderizado, Player e poster/fallback.
- [ ] Vídeo decorativo não inicia com áudio.
- [ ] A mídia possui dimensões estáveis e estratégia de loading.
- [ ] Conteúdo audiovisual essencial possui alternativa textual/caption quando aplicável.
- [ ] Se o scroll controla a mídia, GSAP/ScrollTrigger ou camada equivalente da UI governa a sincronização.
