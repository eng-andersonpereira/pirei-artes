"""Coloca uma frase no meio de um vídeo vertical, estilo serifado branco com contorno preto."""
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont

FONTE = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"

def quebrar(d, texto, f, largura):
    linhas, atual = [], ""
    for w in texto.split():
        teste = (atual + " " + w).strip()
        if d.textlength(teste, font=f) <= largura:
            atual = teste
        else:
            linhas.append(atual); atual = w
    linhas.append(atual)
    return linhas

def overlay(texto, arquivo, W=1080, H=1920, tam=110):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONTE, tam)
    linhas = []
    for par in texto.split("\n"):
        linhas += quebrar(d, par, f, W - 160)
    alt = int(tam * 1.05)
    y = (H - alt * len(linhas)) // 2
    for l in linhas:
        w = d.textlength(l, font=f)
        d.text(((W - w) / 2, y), l, font=f, fill="white", stroke_width=5, stroke_fill="black")
        y += alt
    img.save(arquivo)

def gerar(video, texto, saida):
    overlay(texto, "/tmp/_ov.png")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-loop", "1", "-i", "/tmp/_ov.png",
        "-filter_complex", "[1:v]format=rgba,fade=in:st=0.3:d=0.5:alpha=1[o];[0:v][o]overlay=0:0:shortest=1,format=yuv420p",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "copy", "-movflags", "+faststart", saida], check=True)

if __name__ == "__main__":
    gerar(sys.argv[1], sys.argv[2].replace("\\n", "\n"), sys.argv[3])
