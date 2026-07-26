# Animated Background Injection — Technique Reference

## Use Case
Add subtle floating particle animation to an existing static HTML page without modifying its content/structure. Useful for NFT portfolios, landing pages, project sites where you want "life" without a rebuild.

## Technique
Inject a `<style>` + `<div>` + `<script>` at end of `<body>` (before `</body>`). Particles are appended to fixed overlay, animated via CSS keyframes.

## Key Points
- `position:fixed; inset:0; pointer-events:none; z-index:9998` — covers viewport, no click interference
- Particles: random SVG icons (diamond, rocket, star, hexagon, bolt, coin) + random neon colors
- CSS animation: `float-up linear infinite` — bottom to top with horizontal drift + rotation
- Spawn: initial burst (15 over 4s), then continuous (~1/sec)
- Cleanup: each particle auto-removed after ~40s
- Total DOM nodes: ~25-35 at any time — negligible perf impact

## Code Template
```html
<!-- Injected before </body> -->
<style>
.floater-layer{position:fixed;inset:0;pointer-events:none;z-index:9998;overflow:hidden}
.floater{position:absolute;opacity:0;animation:float-up linear infinite}
@keyframes float-up{
  0%{transform:translateY(105vh) translateX(0) rotate(0deg);opacity:0}
  10%{opacity:.25}
  90%{opacity:.25}
  100%{transform:translateY(-10vh) translateX(var(--drift,40px)) rotate(360deg);opacity:0}
}
.floater svg{width:100%;height:100%;filter:drop-shadow(0 0 6px currentColor)}
</style>
<div class="floater-layer" id="floaterLayer"></div>
<script>
(function(){
  var ICONS=[/* 6-8 inline SVG strings */];
  var COLORS=['#7c3aed','#00e676','#00e5ff','#cc40ff','#a78bfa','#6366f1','#64ffda'];
  var C=document.getElementById('floaterLayer');
  function spawn(){
    var el=document.createElement('div'); el.className='floater';
    var s=12+Math.random()*24;
    el.style.cssText='width:'+s+'px;height:'+s+'px;left:'+Math.random()*100+'%;color:'+COLORS[Math.floor(Math.random()*COLORS.length)]+';animation-duration:'+(15+Math.random()*18)+'s;animation-delay:'+Math.random()*4+'s;--drift:'+((Math.random()-0.5)*120)+'px';
    el.innerHTML=ICONS[Math.floor(Math.random()*ICONS.length)];
    C.appendChild(el);
    setTimeout(function(){if(el.parentNode)el.remove();},40000);
  }
  for(var i=0;i<15;i++)setTimeout(spawn,i*400);
  setInterval(spawn,1500);
})();
</script>
```

## Adaptation Notes
- **Color palette**: Match brand/theme (lime #CCFF00 for RBH, cyan/purple for Web3, etc.)
- **Icon set**: Swap SVGs for theme-relevant shapes (NFT cards, rockets, diamonds, tokens)
- **Density**: Adjust spawn interval (1500ms) and initial burst count
- **Speed**: Animation duration range (15-33s) — slower = more subtle
- **Z-index**: 9998 sits above page content but below modals/overlays (usually 9999+)
- **Performance**: Uses transform + opacity only (GPU-accelerated). No layout thrash.

## Real Usage (This Session)
Applied to Strikingly-exported portfolio at https://iiz-portfolio.vercel.app — original page untouched, particles injected via patch. Verified working in browser.

## Pitfalls
- Don't inject inside page wrappers — must be direct child of `<body>` for fixed positioning
- If page has existing `z-index:9999` modals, particles may show over them (raise modal z-index or lower floater to 9990)
- Mobile: acceptable but consider reducing particle count for battery (check `navigator.connection?.saveData`)
- Screen readers: `pointer-events:none` + no text content = invisible to a11y tree (good)