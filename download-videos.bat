@echo off
echo Starte YouTube Video Download...
cd /d "c:\Users\x\Documents\GitHub\NWO-Cybermobbing-Gangstalking-Hannover-Bloxx"

echo Erstelle Verzeichnisse...
if not exist "video-archive" mkdir "video-archive"
if not exist "mr-bloxx-videos" mkdir "mr-bloxx-videos"

echo Sammle Video-Informationen...
python -m yt_dlp --flat-playlist --print-json "https://www.youtube.com/@PUSHITHTOWN/videos" > video-list.json

echo Starte Download aller Videos...
python -m yt_dlp --format "best[height<=720]" --output "video-archive/%%(id)s_%%(title)s.%%(ext)s" --write-info-json --write-description --write-thumbnail --no-playlist --restrict-filenames --max-filesize 500M --batch-file video-list.json

echo Suche Mr.Bloxx Videos...
findstr /i "mr.bloxx mr bloxx bloxx thomas deike" video-list.json > mr-bloxx-videos.txt

echo Download Mr.Bloxx Videos...
for /f "tokens=*" %%i in (mr-bloxx-videos.txt) do (
    echo Lade %%i...
    python -m yt_dlp "%%i" --format "best[height<=720]" --output "mr-bloxx-videos/%%(id)s_%%(title)s.%%(ext)s" --write-info-json --write-description --write-thumbnail --restrict-filenames --max-filesize 500M
)

echo Download abgeschlossen!
echo Videos in video-archive: %%count%%
echo Mr.Bloxx Videos in mr-bloxx-videos: %%count%%
pause
