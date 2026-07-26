import os, time, requests
from concurrent.futures import ThreadPoolExecutor

# Proven asset gen (RobinGeckos 2026-07-17). Modify PROMPTS per project.
KEYS = [k.strip() for k in open("/root/valid_keys.txt").read().split("\n") if k.strip()]
OUT = "/root/dl"
os.makedirs(OUT, exist_ok=True)
URL = "https://api.iamhc.cn/v1/images/generations"
LIME = "lime green #CCFF00"
NEON = "neon pink #FF00FF / purple #9B30FF / cyan #00FFFF accent"

TRAITS = [
    ("visor", "cyber visor goggles glowing cyan"),
    ("hoodie", "neon pink hoodie with circuit lines"),
    ("chain", "chrome chain with neon purple glow"),
    ("headphone", "cyber headphone with magenta light"),
    ("tongue", "long chrome tongue sticking out"),
    ("spiky", "spiky neon mohawk hair cyan"),
    ("jacket", "techwear jacket neon pink trim"),
    ("mask", "cyber mask with purple vents"),
    ("crown", "broken neon crown magenta"),
    ("sunglass", "cyber sunglasses reflective pink"),
]

def fetch(prompt, tries=5):
    for a in range(tries):
        ki = a % len(KEYS)
        try:
            r = requests.post(URL, headers={"Authorization": f"Bearer {KEYS[ki]}",
                "Content-Type": "application/json"},
                json={"model":"step-image-edit-2","prompt":prompt,"n":1,"size":"1024x1024"}, timeout=60)
            j = r.json()
            if "data" in j and j["data"]:
                return requests.get(j["data"][0]["url"], timeout=60).content
        except Exception as e:
            time.sleep(4)
    return None

def gen_char(i):
    t = TRAITS[i % len(TRAITS)]
    prompt = (f"cyberpunk gecko lizard character portrait, {t[1]}, anthropomorphic reptile, "
              f"big expressive eyes, {NEON} accents, solid {LIME} background, streetwear fashion, "
              f"80s-90s synthwave, clean lineart, cell-shading, 1024x1024, no text")
    raw = fetch(prompt)
    if raw:
        open(f"{OUT}/chars/char_{i+1:02d}_{t[0]}.png","wb").write(raw)
        print(f"[ok] {i+1}")

if __name__ == "__main__":
    os.makedirs(f"{OUT}/chars", exist_ok=True)
    with ThreadPoolExecutor(max_workers=len(KEYS)) as ex:
        ex.map(gen_char, range(10))
    print("DONE 10 chars")
