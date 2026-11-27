"""Post de BOM DIA: frase sobre foto (quadro de um vídeo da pasta Pirei vídeos), 1080x1350.
Uso: python3 bomdia.py <video.mp4> <segundo> "<linha1>|<linha2>|<linha3>" <saida.jpg>
A primeira linha vira o título (ex.: BOM DIA!)."""
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

F = "/usr/share/fonts/truetype/google-fonts/Poppins-"

def gerar(video, seg, linhas, saida):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(seg), "-i", video, "-frames:v", "1",
                    "-vf", "scale=1080:1350:force_original_aspect_ratio=increase,crop=1080:1350", "/tmp/_bg.png"], check=True)
    bg = ImageEnhance.Brightness(Image.open("/tmp/_bg.png").convert("RGB")).enhance(0.78).convert("RGBA")
    W, H = bg.size
    d0 = ImageDraw.Draw(bg)
    estilos = [("Bold", 96)] + [("Regular", 60)] * (len(linhas) - 2) + [("Medium", 60)]
    pos, y = [], 0
    for i, (t, (p, s)) in enumerate(zip(linhas, estilos)):
        f = ImageFont.truetype(F + p + ".ttf", s)
        pos.append((t, f, (W - d0.textlength(t, font=f)) / 2, y))
        y += int(s * 1.35) + (25 if i == 0 else 0)
    off = (H - y) // 2 - 30
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    for t, f, x, yy in pos:
        ds.text((x, yy + off + 3), t, font=f, fill=(0, 0, 0, 215))
    out = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(6)))
    d = ImageDraw.Draw(out)
    for t, f, x, yy in pos:
        d.text((x, yy + off), t, font=f, fill="white")
    out.convert("RGB").save(saida, quality=92)

if __name__ == "__main__":
    gerar(sys.argv[1], sys.argv[2], sys.argv[3].split("|"), sys.argv[4])
