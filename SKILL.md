---
name: nft-collection-launch
description: "End-to-end launch NFT collection di EVM/RBH: gen asset (logo/banner/prereveal/10 char), build website (Vercel, distinct UX tiap project, bg lime #CCFF00), tulis item name+desc prereveal, dan 4 post shill (OpenSea link duluan). Pakai saat user mulai project NFT baru, minta buat website/logo/shill, atau ganti tema project."
---

# NFT Collection Launch

## KAPAN PAKAI
- User mulai project NFT baru (kasih nama / gambar karakter).
- User minta logo, banner, prereveal, 10 char, website, atau shill post.
- User ganti project (misal NeonHood -> RobinGeckos) -> reuse wallet, gen asset baru.

## WORKFLOW (urutan)
1. **Nama + tema** - user kasih nama & gaya karakter. Lock ke memori (ACTIVE project).
2. **Gen 10 char** (IAMHC, concurrent key) - bg = warna project (lihat TEMA).
3. **Gen 3 asset** - logo 500x500, banner 1500x500, prereveal 500x500 (BG SESUAI TEMA).
4. **Item name + desc prereveal** - LANGSUNG sekalian (gak terpisah). Simpen.
5. **Website** - rpad-style, deploy Vercel. Tombol MINT -> OpenSea collection.
6. **4 post shill** - OpenSea link duluan.

## TEMA BG (WAJIB - rule user)
- **MAIN background semua project = LIME GREEN `#CCFF00`** (warna Robinhood network, acuan/baseline user utk project kedepan).
- Karakter/art boleh neon accents (misal RobinGeckos = gecko neon pink/purple/cyan) TAPI **bg site & bg prereveal = lime**.
- JANGAN pakai `#A4F329` (tema Robin Hoodies dead).
- Asset wajib: logo 500x500 + banner 1500x500 + prereveal 500x500 + 10 char.

## ASSET GEN
- Engine: IAMHC 9 key (`/root/valid_keys.txt`, `api.iamhc.cn/v1/images/generations`, model `step-image-edit-2`, size `1024x1024`).
- Style prompt: "cyberpunk gecko character portrait, neon accents, solid <BGCOLOR> background, no text, 1024x1024".
- Resize: `ffmpeg -i raw -vf "scale='max(W,H)':-1,crop=W:H" out.png`.
- Delivery: HTTP link VPS `http://134.199.170.183:8000/<file>` (JANGAN kirim media TG langsung).

## LIVE SUPPLY WIDGET (add to launch sites)
User asked for "mint countdown / live supply widget" → drop in `templates/live_supply_widget.html`.
- Pure client-side: `fetch` JSON-RPC `eth_call` (selector `0x18160ddd` = `totalSupply()`) to the chain RPC.
  RBH RPC allows browser CORS, so NO backend / API key needed. Refreshes every 15s.
- Edit `CONTRACT` (NFT addr), `MAX` (supply), `FREE_CAP` (free allocation), `RPC`, `MINT_START`
  (empty = "MINT IS LIVE"; set ISO string for a real countdown).
- Verified on Outlawhood (RBH contract `0xa697333b6589e9fdab36bbd220b1871d5fb0b35d`, maxSupply 3333,
  totalSupply 0 pre-mint). Pre-check on-chain: `totalSupply()` = current minted; `maxSupply()` may return cap.

## BANNER NUANCE (Outlawhood lesson)
User sent TWO banners: a centered "OUTLAW HOOD" logo composite FIRST, then a WIDER promo banner
(lineup of characters + "SUPPLY 3333 / FREE FOR 50% / FIRST COME FIRST SERVED" + social footer:
outlawhood.xyz, @OutlawHoodNFT, discord.gg/outlawhood). **Use the wider promo banner as hero** —
it carries more info + socials. Then mirror those socials into nav + footer links (prefer the asset
with the most project text/socials, not just the logo).

## WEBSITE (UX RULE - PENTING)
**USER CORRECTION (2026-07-17):** "UX jelek banget, copy-paste kayak website sebelumnya".
- **JANGAN** pake template yg sama persis tiap project. Tiap project bikin **UX beda / terinspirasi referensi user** (misal rpad.fun = card-grid + stats bar + mint card).
- Structure proven (rpad-style): nav (logo+MINT/GALLERY/OPENSEA) + hero compact (text kiri, banner kanan) + **stats bar 4-kotak** + **mint card** (info + meta + button) + **gallery card-grid** (border + caption per item) + footer + floaty.
- Lime bg, teks dark. Tombol MINT -> `https://opensea.io/collection/<nama>`.
- Deploy: `vercel deploy --prod --yes --token $VERCEL_TOKEN` di folder site.
- Lihat `templates/website_rpad_style.html`.
- Live supply/countdown widget: `templates/live_supply_widget.html` (client-side RPC, no backend).
  Verified on Outlawhood (RBH contract `0xa697333b6589e9fdab36bbd220b1871d5fb0b35d`,
  maxSupply 3333, totalSupply 0 pre-mint). For a FULL 3333-image collection from a few
  edited PNGs (no API), use `creative/nft-bulk-generation` `scripts/gen_variants_from_seeds.py`.

## PREREVEAL (RULE)
- Pas gen image prereveal, **LANGSUNG bikin item name + desc** (gak terpisah) biar siap listings OpenSea.
- Format: Name = `<Project> - Sealed [???]`, Desc = narrative singkat + supply + freemint + "no roadmap, just vibes".

## SHILL POST (RULE - OpenSea duluan)
**USER RULE (2026-07-17):** "biasakan link openseanya dibanding website".
- Tiap post: **OpenSea collection link DULUAN**, website Vercel KEDUA.
- Format: hook/CTA + Mint: `https://opensea.io/collection/<nama>` + `https://<vercel>.vercel.app` + hashtag (#Nama #RBH #FreeMint #NFT).
- Buat 4 variasi: (1) Hook/Launch, (2) FOMO/Scarcity, (3) Vibe, (4) CTA.

## REUSE WALLET
- 100 sub + primary di `/root/wallet/sybil_wallets.json` (reuse antar project RBH).
- Sniper: `node /root/ai-mint-bot/mint_project.js 0xKONTRAK` (butuh calldata_sub0.txt).
- Cek mint contract: `node /root/ai-mint-bot/scripts/probe_contract_rbh.js <addr>`.

## PITFALLS
- **JANGAN copy-paste HTML template lama** - user benci, bikin UX beda tiap project.
- **BG jangan lupa lime** - user minta main bg = #CCFF00 utk semua project.
- **Shill jangan taruh website duluan** - OpenSea collection harus di atas.
- **Prereveal: name+desc sekalian pas gen** - jangan nunggu terpisah.
- **Delivery file = HTTP link VPS**, gak kirim media langsung ke TG.
- **STANDALONE image edit gak = launch.** User sering kirim pixel-art PNG terus
  bilang "ganti bg jadi lime, gak ada urusan sama project kita" → itu PURE edit task
  (pakai `nft-bulk-generation` `scripts/pixel_bg_swap.py`), BUKAN mulai project NFT baru.
  Jangan panggil flow launch (nama/tema/asset-gen/website) cuma krna ada gambar.
  BARU jadi launch kalau user explicitly bilang bikin project/website/shill dr gambar itu.
- **Reuse edited PNG sbg site asset:** kalau user kerjain bg-swap standalone trus
  bilang "buat website utk NFT ini" (contoh: Outlawhood — 6 char lime + banner
  "OUTLAW HOOD" → site Vercel), itu saatnya jalanin launch flow: copy asset ke
  folder site, build HTML (hero banner + bio + stats supply/freemint + crew grid
  + tombol MINT→OpenSea), deploy. Outlawhood template: hero=banner user,
  bio persis user, supply 3333, freemint 50% (1667 gratis), 🟢 stay Robinhood.

## ANIMATED BG INJECTION (for existing pages — 2026-07-23)
For existing static pages (Strikingly export, generic HTML), add floating particles WITHOUT modifying page content:
- Inject `<style>` + `<div>` + `<script>` before `</body>`
- Uses fixed overlay with CSS keyframes for GPU-accelerated animation (transform+opacity only)
- Particles: random SVG icons + neon colors, auto-cleanup after 40s
- See `references/animated-bg-injection.md` for full template and adaptation notes
- Applied to portfolio https://iiz-portfolio.vercel.app — original Strikingly page preserved

## COLLAGE → INDIVIDUAL TRANSPARENT PNGs (Brainhood lesson)
User often sends a SINGLE image that is a **grid/collage of many characters** (e.g. 3x6 = 18
NFT PFPs on a solid WHITE or lime background). To use them you must split + remove bg.
- **Split:** divide by grid math (`W//cols`, `H//rows`), `img.crop()` each cell.
- **Remove solid bg → transparent PNG:** numpy mask `all(R,G,B > 240)` (white) or
  lime `#CCFF00` = `(204,255,0)`); set alpha 0 there, 255 elsewhere → RGBA.
  Then `crop(getbbox())` + pad to square so all tiles align in a grid.
- **Reusable script:** `scripts/split_collage.py <collage> <out_dir> [cols=6] [rows=3] [bg=white|lime]`
  does the full crop+transparent+square-pad in one pass. Add `names` list in the script if you
  want labeled tiles (Brainhood run used indexed 01..18).
- White-bg collages are EASIER (clean threshold) than lime-bg (antialiased edges near char).

## ANIMATED GALLERY BG (Brainhood lesson — IMPORTANT SEPARATION)
- **Gallery GRID** = the real showcased characters (few, curated, e.g. 4 lime-bg PFPs) on a
  solid lime panel. This is the "product".
- **Animated BACKGROUND** = separate floating elements behind the grid, looping via pure CSS
  (no video file, no bandwidth). Pattern that worked:
  - `.gallery{ overflow:hidden; position:relative; }` + `@keyframes limePulse` on bg color.
  - `.floaters{ position:absolute; inset:0; z-index:0; pointer-events:none; }` with N `<span>`
    each holding a transparent-PNG char, `animation: floatUp linear infinite` (translateY
    110vh→-20vh + rotate 360deg, opacity fade in/out), staggered `animation-duration` (18–28s)
    + `animation-delay` per `:nth-child` for a non-repeating drift.
  - Grid container gets `position:relative; z-index:2` so it sits ABOVE floaters.
- User explicitly said: "18 char itu buat bg animated. Gallery tetep pake yg sebelumnya yg bg
  lime green." → **never merge the two roles.** Background = eye-candy loop; grid = the assets.
- If the user sends a STATIC logo/mascot image when they said "animated bg", treat it as a
  logo asset, not a video — generate the motion with CSS floaters from existing PNGs.
