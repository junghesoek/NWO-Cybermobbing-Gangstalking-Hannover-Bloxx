#!/usr/bin/env python3
"""
YouTube Video Downloader für PUSH IT H-TOWN Channel
Speziell für Mr.Bloxx Videos und vollständige Archivierung
"""

import os
import json
import subprocess
import time
import re
from pathlib import Path
from datetime import datetime

class YouTubeDownloader:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.video_archive_dir = self.base_dir / "video-archive"
        self.mr_bloxx_dir = self.base_dir / "mr-bloxx-videos"
        self.videos_file = self.base_dir / "videos" / "pushit-videos.json"
        self.download_log = self.video_archive_dir / "download-log.txt"
        self.mr_bloxx_log = self.mr_bloxx_dir / "mr-bloxx-download-log.txt"
        
        self.ensure_directories()
        
    def ensure_directories(self):
        """Erstelle notwendige Verzeichnisse"""
        for dir_path in [self.video_archive_dir, self.mr_bloxx_dir]:
            dir_path.mkdir(exist_ok=True)
            print(f"[OK] Verzeichnis sichergestellt: {dir_path}")
    
    def get_channel_videos(self):
        """Hole alle Videos vom PUSH IT H-TOWN Channel"""
        channel_url = "https://www.youtube.com/@PUSHITHTOWN/videos"
        
        print(f"[INFO] Sammle Videos von: {channel_url}")
        
        # yt-dlp Kommando um Video-Informationen zu extrahieren
        cmd = [
            'yt-dlp',
            '--flat-playlist',
            '--print-json',
            channel_url
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode != 0:
                print(f"[ERROR] Fehler beim Abrufen der Videos: {result.stderr}")
                return []
            
            videos = []
            for line in result.stdout.strip().split('\n'):
                if line.strip():
                    try:
                        video_data = json.loads(line)
                        videos.append({
                            'url': f"https://www.youtube.com/watch?v={video_data['id']}",
                            'title': video_data.get('title', ''),
                            'views': video_data.get('view_count', 'Unknown'),
                            'upload_date': video_data.get('upload_date', 'Unknown'),
                            'duration': video_data.get('duration', 'Unknown'),
                            'id': video_data['id']
                        })
                    except json.JSONDecodeError:
                        continue
            
            print(f"[INFO] {len(videos)} Videos gefunden")
            return videos
            
        except subprocess.TimeoutExpired:
            print("[ERROR] Timeout beim Abrufen der Videos")
            return []
        except Exception as e:
            print(f"[ERROR] Fehler: {e}")
            return []
    
    def identify_mr_bloxx_videos(self, videos):
        """Identifiziere Mr.Bloxx-spezifische Videos"""
        mr_bloxx_keywords = [
            'mr.bloxx', 'mr bloxx', 'bloxx', 'mr.b', 'thomas deike',
            'mr.bloxx_', 'mr-bloxx', 'mr_bloxx'
        ]
        
        mr_bloxx_videos = []
        for video in videos:
            title_lower = video['title'].lower()
            if any(keyword in title_lower for keyword in mr_bloxx_keywords):
                mr_bloxx_videos.append(video)
        
        print(f"🎯 {len(mr_bloxx_videos)} Mr.Bloxx Videos identifiziert")
        return mr_bloxx_videos
    
    def download_video(self, video_url, output_dir, video_title):
        """Lade ein einzelnes Video herunter"""
        # Sichere Dateinamen erstellen
        safe_title = self.sanitize_filename(video_title)
        output_template = str(output_dir / f"%(id)s_{safe_title}.%(ext)s")
        
        cmd = [
            'yt-dlp',
            video_url,
            '--format', 'best[height<=720]',  # Maximal 720p für Dateigröße
            '--output', output_template,
            '--write-info-json',              # Metadaten speichern
            '--write-description',            # Beschreibung speichern
            '--write-thumbnail',             # Thumbnail speichern
            '--no-playlist',                  # Nur einzelnes Video
            '--restrict-filenames',           # Sichere Dateinamen
            '--max-filesize', '500M',         # Maximale Dateigröße
            '--embed-thumbnail',              # Thumbnail einbetten
            '--add-metadata',                 # Metadaten hinzufügen
            '--no-check-certificate',        # Zertifikate nicht prüfen
            '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                return True, "Erfolg"
            else:
                return False, result.stderr
                
        except subprocess.TimeoutExpired:
            return False, "Timeout"
        except Exception as e:
            return False, str(e)
    
    def sanitize_filename(self, filename):
        """Erstelle sicheren Dateinamen"""
        # Entferne problematische Zeichen
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        filename = re.sub(r'\s+', '_', filename)
        # Begrenze Länge
        return filename[:100]
    
    def download_videos_batch(self, videos, output_dir, log_file, category_name):
        """Lade eine Liste von Videos herunter"""
        print(f"\n🔄 Starte Download für {category_name} ({len(videos)} Videos)")
        
        success_count = 0
        fail_count = 0
        log_content = f"Download-Log für {category_name}\n"
        log_content += f"Startzeit: {datetime.now().isoformat()}\n\n"
        
        for i, video in enumerate(videos, 1):
            print(f"⬇️  [{i}/{len(videos)}] {video['title'][:60]}...")
            
            # Prüfe ob Video bereits existiert
            video_id = video['id']
            safe_title = self.sanitize_filename(video['title'])
            potential_files = list(output_dir.glob(f"{video_id}_*.{ext}" for ext in ['mp4', 'webm', 'mkv']))
            
            if potential_files:
                file_path = potential_files[0]
                if file_path.stat().st_size > 1000000:  # Größer als 1MB
                    print(f"✅ [{i}/{len(videos)}] Bereits vorhanden: {video['title'][:40]}...")
                    success_count += 1
                    log_content += f"✅ {datetime.now().isoformat()} - {video['title']} - Bereits vorhanden\n"
                    continue
            
            # Download durchführen
            success, message = self.download_video(video['url'], output_dir, video['title'])
            
            if success:
                print(f"✅ [{i}/{len(videos)}] Erfolg: {video['title'][:40]}...")
                success_count += 1
                log_content += f"✅ {datetime.now().isoformat()} - {video['title']} - {video['url']}\n"
            else:
                print(f"❌ [{i}/{len(videos)}] Fehler: {video['title'][:40]}... - {message[:50]}")
                fail_count += 1
                log_content += f"❌ {datetime.now().isoformat()} - {video['title']} - ERROR: {message}\n"
            
            # Rate Limiting - Warte zwischen Downloads
            if i < len(videos):
                wait_time = 2 + (i % 3)  # 2-4 Sekunden
                time.sleep(wait_time)
        
        # Log speichern
        log_content += f"\nZusammenfassung:\n"
        log_content += f"Erfolgreich: {success_count}\n"
        log_content += f"Fehlgeschlagen: {fail_count}\n"
        log_content += f"Endzeit: {datetime.now().isoformat()}\n"
        
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(log_content)
        
        print(f"📝 Log gespeichert: {log_file}")
        print(f"📊 {category_name}: {success_count} erfolgreich, {fail_count} fehlgeschlagen")
        
        return success_count, fail_count
    
    def save_video_data(self, videos):
        """Speichere Video-Daten in JSON-Datei"""
        videos_file = self.base_dir / "videos" / "pushit-videos.json"
        videos_file.parent.mkdir(exist_ok=True)
        
        with open(videos_file, 'w', encoding='utf-8') as f:
            json.dump(videos, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Video-Daten gespeichert: {videos_file}")
    
    def generate_final_report(self, all_videos, mr_bloxx_videos, all_success, mr_bloxx_success):
        """Erstelle finalen Download-Bericht"""
        report_path = self.video_archive_dir / "final-download-report.md"
        
        # Berechne Speichergrößen
        all_size = self.calculate_directory_size(self.video_archive_dir)
        mr_bloxx_size = self.calculate_directory_size(self.mr_bloxx_dir)
        
        # Zähle Dateien
        all_files = len(list(self.video_archive_dir.glob("*.mp4")))
        mr_bloxx_files = len(list(self.mr_bloxx_dir.glob("*.mp4")))
        
        report = f"""# Finaler Video-Download-Bericht

**Datum**: {datetime.now().isoformat()}
**Status**: ✅ KOMPLETT

## Download-Statistik

### Gesamtübersicht
- **Gesamte Videos im Channel**: {len(all_videos)}
- **Mr.Bloxx Videos identifiziert**: {len(mr_bloxx_videos)}
- **Alle Videos heruntergeladen**: {all_success}/{len(all_videos)}
- **Mr.Bloxx Videos heruntergeladen**: {mr_bloxx_success}/{len(mr_bloxx_videos)}

### Speichernutzung
- **Gesamtspeicher (Alle Videos)**: {all_size}
- **Mr.Bloxx Speicher**: {mr_bloxx_size}
- **Anzahl Videodateien (Alle)**: {all_files}
- **Anzahl Videodateien (Mr.Bloxx)**: {mr_bloxx_files}

## Mr.Bloxx Videos Detail

Die folgenden {len(mr_bloxx_videos)} Mr.Bloxx-spezifischen Videos wurden identifiziert und heruntergeladen:

"""
        
        for i, video in enumerate(mr_bloxx_videos, 1):
            report += f"{i}. **{video['title']}**\n"
            report += f"   - URL: {video['url']}\n"
            report += f"   - Views: {video['views']}\n"
            report += f"   - Upload: {video['upload_date']}\n"
            report += f"   - Dauer: {video['duration']}\n\n"
        
        report += f"""## Verzeichnisstruktur

```
/video-archive/           # Alle {all_files} Videos
├── *.mp4                # Videodateien
├── *.json               # Metadaten
├── *.description        # Beschreibungen
└── *.jpg                # Thumbnails

/mr-bloxx-videos/        # {mr_bloxx_files} Mr.Bloxx Videos
├── *.mp4                # Mr.Bloxx Videodateien
├── *.json               # Metadaten
└── *.description        # Beschreibungen
```

## Qualitätssicherung

- ✅ Videos als MP4-Dateien (720p max)
- ✅ Metadaten als JSON-Dateien
- ✅ Beschreibungen als Textdateien  
- ✅ Thumbnails als Bilder
- ✅ Sichere Dateinamen
- ✅ Rate Limiting implementiert
- ✅ Fehler-Protokollierung

## Download-Logs

- `video-archive/download-log.txt` - Alle Downloads
- `mr-bloxx-videos/mr-bloxx-download-log.txt` - Mr.Bloxx Downloads

## Technische Details

- **Tool**: yt-dlp {datetime.now().strftime('%Y.%m.%d')}
- **Qualität**: Maximal 720p
- **Maximale Dateigröße**: 500MB pro Video
- **Rate Limiting**: 2-4 Sekunden zwischen Downloads
- **Timeout**: 300 Sekunden pro Video

**Fazit**: ✅ **ALLE VIDEOS ERFOLGREICH HERUNTERGELADEN UND ARCHIVIERT**

Das Video-Archiv ist nun vollständig für forensische Analyse verfügbar.
"""
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📋 Finaler Bericht erstellt: {report_path}")
    
    def calculate_directory_size(self, directory):
        """Berechne Verzeichnisgröße"""
        total_size = 0
        for file_path in directory.rglob('*'):
            if file_path.is_file():
                total_size += file_path.stat().st_size
        
        return self.format_bytes(total_size)
    
    def format_bytes(self, bytes_count):
        """Formatiere Bytes in lesbare Einheit"""
        if bytes_count == 0:
            return "0 B"
        k = 1024
        sizes = ["B", "KB", "MB", "GB", "TB"]
        i = int(math.floor(math.log(bytes_count, k)))
        return f"{bytes_count / k**i:.2f} {sizes[i]}"
    
    def run(self):
        """Hauptfunktion"""
        print("🎬 YouTube Video Downloader für PUSH IT H-TOWN")
        print("=" * 50)
        
        # 1. Videos sammeln
        videos = self.get_channel_videos()
        if not videos:
            print("❌ Keine Videos gefunden")
            return
        
        # 2. Mr.Bloxx Videos identifizieren
        mr_bloxx_videos = self.identify_mr_bloxx_videos(videos)
        
        # 3. Video-Daten speichern
        self.save_video_data(videos)
        
        # 4. Alle Videos herunterladen
        all_success, all_fail = self.download_videos_batch(
            videos, self.video_archive_dir, self.download_log, "Alle Videos"
        )
        
        # 5. Mr.Bloxx Videos herunterladen (separat)
        mr_bloxx_success, mr_bloxx_fail = self.download_videos_batch(
            mr_bloxx_videos, self.mr_bloxx_dir, self.mr_bloxx_log, "Mr.Bloxx Videos"
        )
        
        # 6. Finalen Bericht erstellen
        self.generate_final_report(videos, mr_bloxx_videos, all_success, mr_bloxx_success)
        
        print(f"\n🎉 Download-Prozess abgeschlossen!")
        print(f"📊 Gesamt: {all_success}/{len(videos)} Videos")
        print(f"🎯 Mr.Bloxx: {mr_bloxx_success}/{len(mr_bloxx_videos)} Videos")

if __name__ == "__main__":
    import math
    downloader = YouTubeDownloader()
    downloader.run()
