"""Transforma um carrossel em Reel vertical 1080x1920 (fundo branco, transição suave)."""
import subprocess, sys, os
from PIL import Image

def montar_reel(pasta_slides, n, saida, seg=2.4, fade=0.4):
    tmp = pasta_slides + "_vert"
    os.makedirs(tmp, exist_ok=True)
    for i in range(1, n + 1):
        s = Image.open(f"{pasta_slides}/slide_{i:02d}.png").convert("RGB")
        v = Image.new("RGB", (1080, 1920), "white")
        v.paste(s, (0, (1920 - s.height) // 2))
        v.save(f"{tmp}/{i:02d}.png")
    # última tela fica mais tempo (chamada pra ação)
    durs = [seg] * (n - 1) + [seg + 1.5]
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for i, d in enumerate(durs, 1):
        cmd += ["-loop", "1", "-t", str(d), "-i", f"{tmp}/{i:02d}.png"]
    # cadeia de crossfades
    filt, prev, off = [], "[0:v]", 0.0
    for i in range(1, n):
        off += durs[i - 1] - fade
        out = f"[v{i}]"
        filt.append(f"{prev}[{i}:v]xfade=transition=fade:duration={fade}:offset={off:.2f}{out}")
        prev = out
    filt.append(f"{prev}format=yuv420p[out]")
    cmd += ["-filter_complex", ";".join(filt), "-map", "[out]", "-r", "30",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-movflags", "+faststart", saida]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    montar_reel(sys.argv[1], int(sys.argv[2]), sys.argv[3])
