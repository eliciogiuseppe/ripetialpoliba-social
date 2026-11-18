#!/bin/sh
# Trasforma una story PNG 1080x1920 in un video MP4 di 7 s con la musica originale.
# Uso: sh storia_video.sh input.png output.mp4 OFFSET_SECONDI
DIR=$(dirname "$0")
ffmpeg -v error -y -loop 1 -framerate 30 -i "$1" -ss "$3" -t 7 -i "$DIR/musica/lofi-norm.flac" \
 -filter_complex "[0:v]scale=2160:3840,zoompan=z='1+0.0002*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,format=yuv420p,fade=t=in:st=0:d=0.35[v];[1:a]afade=t=in:st=0:d=0.4,afade=t=out:st=6.5:d=0.5[a]" \
 -map "[v]" -map "[a]" -t 7 -c:v libx264 -preset veryfast -crf 20 -profile:v high -c:a aac -b:a 160k -movflags +faststart "$2"
