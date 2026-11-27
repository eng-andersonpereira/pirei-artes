# Perfis de referência do @pireioficial

Lista usada pela tarefa diária para modelar conteúdo (pegar ideia e formato, nunca copiar).
Novos perfis são adicionados aqui.

| Perfil | Seguidores | Melhor uso | O que funciona |
|---|---|---|---|
| resiliencia_humana | 13,1 mi | carrossel e frase | dica útil do dia a dia, curiosidade, reflexão com data ("faltam X dias") |
| resilienciaepazz | 1,5 mi | carrossel e frase de relacionamento | amor-próprio, "pare de aceitar menos", "você não é opção" (evitar técnicas de manipulação) |
| resilienciamilionaria | 1,4 mi | carrossel de motivação | "volta pra luta", "o que deu errado precisava dar errado", "você vai incomodar" |
| evolua_mude | 557 mil (restrito) | carrossel de mentalidade/dinheiro | disciplina, evolução, liberdade financeira (só bio disponível) |
| sincerooficial | 20,6 mi | frase de humor | memes de texto do dia a dia, legenda de 2-3 palavras ("novembro passou voando" 235 mil curtidas, "preciso de férias", "sem condições") |
| sigofrases | 3,9 mi | frase única | frases curtas de reflexão, amor, fé e humor; legenda curtíssima ("pense nisso. ❤️" 23 mil, "lembrete!" 15 mil, "fato!" 10 mil, "que assim seja!"); posts das 8h da manhã foram os que mais curtiram |
| motivacoespositiva | 3,9 mi | frase de fé curta | frases curtas de gratidão e fé ("Obrigada Pai", "Seja sempre grato"); muitos posts são de afiliado "comenta QUERO" (ignorar) |
| encorajo | 1,0 mi | frase de reflexão/fé + legenda longa | imagem com frase + legenda-texto longa e emotiva; temas de fim de ano ("Que 2027 seja...", "Dezembro será um mês de honra" 206 comentários), gratidão (16,8 mil), sonhos, "nunca mais se abandone"; usa colaboradores |
| versos | 1,5 mi | carrossel de curiosidade | carrosséis "Na Índia/Colômbia/Turquia existe..." sobre lugares incríveis do mundo; bandeira do país no início da legenda |
| menteposittiva | 2,4 mi | frase de reflexão | frase única de reflexão; posts de imagem com 23–32 mil curtidas |

Observação: alguns desses perfis colocam textos em inglês sobre celebridades na legenda (truque de alcance). NÃO copiar isso: pode ser punido pelo Instagram e não combina com o Pirei.

## Instruções extras para a tarefa diária (pedidas pelo Anderson)
- **Carrossel de curiosidade de vez em quando:** 2 a 3 vezes por semana (não em dias seguidos), troque UM dos 3 carrosséis do dia por um carrossel de curiosidade no estilo do @versos (ex.: "Na Índia existe uma ponte feita de raízes vivas..."). Use só fatos reais e verificáveis; na dúvida, escolha outro fato. Mesmo design (fundo branco, sem aspas), slide 8 com Curta/Compartilhe/Siga. Alterne qual nicho sai nesse dia.
- **Fim de ano (até 31/12):** aproveite o tema que está bombando nas referências ("Dezembro abençoado", "Que 2027 seja...", balanço do ano, gratidão pelo que passou) em pelo menos uma frase ou carrossel a cada 2 dias, sem repetir o mesmo ângulo. Ajuste contagens ("faltam X dias") à data real de publicação.

## Ajustes pelos números (27/11) — valem a partir de agora
Diagnóstico: o perfil tem 20,9 mil seguidores, mas cada post alcançou só 3 a 33 pessoas (seguidores antigos/inativos). O melhor post foi "Volta pra luta" (motivação): 28 de alcance, 12 compartilhamentos e 7 salvamentos.
- **Mix de carrosséis:** 2 dos 3 carrosséis do dia devem ser de MOTIVAÇÃO/SUPERAÇÃO (ângulos diferentes); o terceiro alterna entre relacionamento, mentalidade/dinheiro e curiosidade.
- **Capa mais forte:** o slide 1 deve parar o dedo: frase de impacto, pergunta direta ou fala com a pessoa ("Se você está cansado, lê isso até o fim", "Ninguém vai te contar isso, mas..."). Evite capas que são só um tema ("Disciplina").
- **Reel de teste diário (5º post):** transforme o carrossel de motivação mais forte do dia em Reel: renderize os slides com `render(..., reel=True)` (não desenha o "arrasta") e rode `python3 reel.py <pasta_dos_slides> 8 <saida.mp4>` (o script está na raiz do repositório; cada slide fica 2,4 s, o último um pouco mais). Suba em `AAAA-MM/reels/<slug>.mp4`. Publique com action "create_video_post", trial_params {"graduation_strategy": "SS_PERFORMANCE"} (mostra só pra quem não segue e vai pro feed sozinho se performar bem), video_url "https://cdn.jsdelivr.net/gh/eng-andersonpereira/pirei-artes@main/<caminho>" (fallback: o link raw.githubusercontent). Legenda curta com gancho ("assiste até o fim"), sem colaboradores. Agende às 15:00 junto com os outros após o "posta".

## Reels lifestyle com frase (pedido do Anderson em 27/11)
- Vídeos de lifestyle feminino do Anderson (ele tem os direitos): pasta do Google Drive "Pack de luxo feminino" / "Pirei vídeos" (procure com o conector do Google Drive por vídeos .mp4 nessa pasta ou em pastas com "Pirei" no nome). Não repita um vídeo já usado (veja `AAAA-MM/reels/`).
- Estilo da frase: no MEIO da tela, fonte serifada (Liberation Serif Regular), branca com contorno preto, tamanho ~110 — use `python3 frase_video.py <video.mp4> "<frase com \n>" <saida.mp4>` (script na raiz do repositório).
- Frases de impacto curtas (2 a 4 linhas), originais, combinando com o clima do vídeo (mulher forte, elegância, autoestima, superação). Legenda curtinha ("marca aquela amiga que é assim ✨") + Manda/Segue + hashtags.
- Publicar como Reel de teste (create_video_post com trial_params SS_PERFORMANCE), link jsDelivr. Quando houver vídeos disponíveis, faça 1 Reel lifestyle por dia, agendado às 09:00 junto com os outros após o "posta" (a frase-imagem passa para as 10:30).
