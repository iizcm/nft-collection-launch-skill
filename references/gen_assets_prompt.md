# Asset generation prompts (IAMHC, proven 2026-07-17)

## Engine
- Endpoint: `https://api.iamhc.cn/v1/images/generations`
- Model: `step-image-edit-2`
- Size: `1024x1024`
- Keys: `/root/valid_keys.txt` (9 valid, rotate per worker)
- Resize: `ffmpeg -i raw.png -vf "scale='max(W,H)':-1,crop=W:H" out.png`

## 10 char (gecko cyberpunk, lime bg)
"cyberpunk gecko lizard character portrait, {trait}, anthropomorphic reptile,
big expressive eyes, neon pink #FF00FF / purple #9B30FF / cyan #00FFFF accent,
solid lime green #CCFF00 background, streetwear fashion, 80s-90s synthwave,
clean lineart, cell-shading, 1024x1024, no text"

Traits pool:
- visor goggles glowing cyan
- neon pink hoodie with circuit lines
- chrome chain with neon purple glow
- cyber headphone with magenta light
- long chrome tongue sticking out
- spiky neon mohawk hair cyan
- techwear jacket neon pink trim
- cyber mask with purple vents
- broken neon crown magenta
- cyber sunglasses reflective pink

## Logo 500x500 (clean)
"minimalist clean gecko lizard logo icon, cyberpunk, neon outline on solid
lime green #CCFF00 background, no text, flat vector, 500x500"

## Banner 1500x500
"wide banner, group of cyberpunk gecko characters with neon streetwear accents,
solid lime green #CCFF00 background, neon glow, no text, cinematic, 1500x500"

## Prereveal 500x500
"mysterious pre-reveal placeholder, solid lime green #CCFF00 background with faint
glitch silhouette of a gecko, neon matrix rain, no text, 500x500"

## NOTE
- KRN user benci copy-paste template, tiap project MODIFIKASI prompt
  (ganti species/style) tp TETAP bg = lime #CCFF00.
- Delivery: HTTP link VPS `http://134.199.170.183:8000/<file>`.
