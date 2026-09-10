from pathlib import Path

skill = Path('SKILL.md')
text = skill.read_text(encoding='utf-8')

marker = '# Hierarquia visual\n'
section_title = '# Scroll Motion Contract — animações dependentes de scroll\n'
section = '''# Scroll Motion Contract — animações dependentes de scroll

Animações dependentes de scroll devem possuir **intenção de UX, narrativa ou orientação espacial**. Elas não devem ser adicionadas automaticamente para tornar uma página mais chamativa.

Consulte também:

- `references/scroll-motion.md`

> A biblioteca correta é **GSAP**. “GASP” é apenas um erro comum de escrita.

## Escada de decisão obrigatória

Escolha a técnica mais simples suficiente para o efeito:

1. **CSS/transitions** — feedback pequeno sem dependência real de scroll.
2. **IntersectionObserver + CSS** — reveals discretos de entrada/saída da viewport.
3. **CSS Scroll-driven Animations** — progresso simples ligado ao scroll ou à visibilidade, somente quando o suporte exigido pelo projeto for suficiente e houver progressive enhancement/fallback.
4. **GSAP + ScrollTrigger** — scroll complexo, coreografado ou sincronizado.
5. **Remotion** — somente quando o artefato principal for vídeo, motion graphics ou uma experiência de vídeo incorporada; não usar como motor de scroll da página.

Não instale GSAP para um fade/translate simples que IntersectionObserver + CSS resolvem com clareza.

## Quando usar GSAP + ScrollTrigger

GSAP ScrollTrigger é a opção preferencial quando a interface exigir um ou mais destes comportamentos:

- `scrub` ligado ao progresso do scroll;
- `pin` de uma região por parte da narrativa;
- `snap` intencional;
- timeline com múltiplos elementos coordenados;
- storytelling por scroll;
- product showcase em etapas;
- texto e visual sincronizados;
- parallax multicamada controlado;
- horizontal scroll deliberado;
- z-axis cascade complexo;
- callbacks avançados de entrada, saída, retorno e progresso.

Regras:

- registre `ScrollTrigger` explicitamente;
- defina `start` e `end` de forma previsível;
- use `scrub` somente quando o progresso realmente deve acompanhar a rolagem;
- use `pin` com moderação e nunca para aprisionar conteúdo longo sem necessidade;
- prefira animar filhos de uma região pinned em vez de alterar diretamente a geometria do elemento usado como pin quando isso comprometer medições;
- markers são apenas para desenvolvimento;
- recalcule com `ScrollTrigger.refresh()` quando mudanças relevantes de layout exigirem;
- não misture listeners manuais de scroll e ScrollTrigger para resolver o mesmo comportamento sem necessidade.

## React + GSAP

Em React:

- prefira `useGSAP()` de `@gsap/react` quando GSAP fizer parte da solução;
- alternativamente, use `gsap.context()` e `revert()` no cleanup;
- escopar selectors por `ref` ao componente;
- não criar timelines novamente a cada render sem necessidade;
- limpar timelines, ScrollTriggers, observers e listeners no unmount;
- garantir que React Strict Mode não deixe triggers duplicados;
- usar `gsap.matchMedia()` para separar desktop, mobile e `prefers-reduced-motion` quando a composição mudar.

## CSS Scroll-driven Animations

`animation-timeline`, `scroll()` e `view()` podem ser usados para efeitos simples cujo progresso acompanha scroll/view progress.

Como o suporte entre navegadores pode não ser uniforme:

- use `@supports` quando necessário;
- mantenha fallback funcional;
- não esconda conteúdo essencial em browsers sem suporte;
- não dependa dessa API quando o requisito de compatibilidade do projeto não permitir.

## Remotion

**Remotion não deve ser escolhido como biblioteca de scroll motion da interface.**

Use Remotion quando o objetivo for:

- gerar MP4/WebM;
- criar vídeo de demonstração;
- produzir motion graphics;
- vídeo parametrizado;
- experiência baseada em Remotion Player;
- pipeline ou editor de vídeo.

Se a página controlar uma mídia pelo scroll, a camada de scroll deve continuar pertencendo à UI — por exemplo GSAP/ScrollTrigger ou técnica equivalente adequada. Remotion pode produzir ou reproduzir a mídia, mas não substitui a arquitetura de scroll da página.

## Scroll-jacking proibido por padrão

Não altere a mecânica natural de rolagem apenas para produzir sensação cinematográfica.

Evite:

- bloquear wheel/touch;
- impedir scroll natural;
- snap agressivo em conteúdo textual;
- smooth scroll obrigatório que comprometa teclado, âncoras ou histórico;
- pinning excessivo;
- seções que dificultem voltar ao conteúdo anterior;
- progressão que torne conteúdo inacessível sem a animação.

## Performance

Para scroll motion:

- priorize `transform` e `opacity`;
- reduza blur/filter em grandes superfícies;
- evite animar layout continuamente;
- evite `getBoundingClientRect()` repetitivo dentro de listeners de scroll manuais;
- não crie dezenas de observers/timelines independentes para microelementos;
- não use `will-change` globalmente;
- mantenha imagens e regiões pinned com dimensões estáveis quando possível.

## Responsive e reduced motion

Em mobile/tablet estreito:

- remova pin prolongado quando ele prejudicar leitura;
- elimine overlaps complexos;
- reduza parallax;
- não torne horizontal-scroll storytelling a única forma de acessar informação;
- preserve o fluxo vertical normal como fallback.

Com `prefers-reduced-motion: reduce`:

- remover ou reduzir scrub, parallax, scale e deslocamentos grandes;
- remover pinning puramente decorativo;
- renderizar o conteúdo em estado final legível;
- nunca deixar conteúdo invisível aguardando trigger de animação.

## QA específico de scroll

Valide, proporcionalmente ao escopo:

- scroll lento e rápido;
- avanço e retorno;
- resize;
- refresh no meio da página;
- carregamento tardio de imagens/fontes;
- navegação por âncora;
- teclado;
- touch/mobile;
- reduced motion;
- ausência de layout jump;
- ausência de elementos presos após sair da seção;
- cleanup após troca de rota em SPA;
- console sem erros relacionados ao motion.

---

'''

if section_title not in text:
    if marker not in text:
        raise SystemExit('motion insertion marker not found')
    text = text.replace(marker, section + marker, 1)

preflight_marker = '## Performance\n\n- [ ] Nenhuma biblioteca grande foi instalada por um efeito pequeno.\n'
preflight_title = '## Scroll motion\n'
preflight = '''## Scroll motion

- [ ] A animação dependente de scroll possui finalidade concreta.
- [ ] A técnica escolhida é a mais simples suficiente.
- [ ] Reveal simples não recebeu GSAP sem necessidade.
- [ ] CSS Scroll-driven Animations possui suporte/fallback adequado ao projeto quando utilizada.
- [ ] GSAP/ScrollTrigger foi reservado para orquestração complexa.
- [ ] `pin`, `scrub` e `snap` possuem justificativa explícita.
- [ ] React possui cleanup correto de timelines/triggers/listeners.
- [ ] Mobile possui comportamento próprio quando necessário.
- [ ] `prefers-reduced-motion` foi tratado.
- [ ] O conteúdo permanece acessível sem a animação.
- [ ] Não existe scroll-jacking desnecessário.
- [ ] Back-scroll, resize e refresh no meio da página foram considerados.
- [ ] Remotion não foi utilizado como motor de scroll da página.

'''

if preflight_title not in text:
    if preflight_marker not in text:
        raise SystemExit('preflight insertion marker not found')
    text = text.replace(preflight_marker, preflight + preflight_marker, 1)

skill.write_text(text, encoding='utf-8')
