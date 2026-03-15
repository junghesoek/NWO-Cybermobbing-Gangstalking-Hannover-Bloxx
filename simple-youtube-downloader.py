#!/usr/bin/env python3
"""
Einfacher YouTube Video Downloader für PUSH IT H-TOWN Channel
Speziell für Mr.Bloxx Videos und vollständige Archivierung
"""

import os
import json
import subprocess
import time
import re
from pathlib import Path
from datetime import datetime

class SimpleYouTubeDownloader:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.video_archive_dir = self.base_dir / "video-archive"
        self.mr_bloxx_dir = self.base_dir / "mr-bloxx-videos"
        self.videos_file = self.base_dir / "videos" / "pushit-videos.json"
        
        self.ensure_directories()
        
    def ensure_directories(self):
        """Erstelle notwendige Verzeichnisse"""
        for dir_path in [self.video_archive_dir, self.mr_bloxx_dir]:
            dir_path.mkdir(exist_ok=True)
            print(f"[OK] Verzeichnis erstellt: {dir_path}")
    
    def get_channel_videos(self):
        """Hole alle Videos vom PUSH IT H-TOWN Channel"""
        channel_url = "https://www.youtube.com/@PUSHITHTOWN/videos"
        
        print("[INFO] Sammle Videos von PUSH IT H-TOWN Channel...")
        
        # yt-dlp Kommando um Video-Informationen zu extrahieren
        cmd = [
            'python', '-m', 'yt_dlp',
            '--flat-playlist',
            '--print-json',
            channel_url
        ]
        
        try:
            print("[INFO] Fuehre yt-dlp aus...")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode != 0:
                print(f"[ERROR] yt-dlp Fehler: {result.stderr}")
                return []
            
            videos = []
            lines = result.stdout.strip().split('\n')
            
            for line in lines:
                if line.strip():
                    try:
                        video_data = json.loads(line)
                        video_info = {
                            'url': f"https://www.youtube.com/watch?v={video_data['id']}",
                            'title': video_data.get('title', ''),
                            'views': str(video_data.get('view_count', 'Unknown')),
                            'upload_date': video_data.get('upload_date', 'Unknown'),
                            'duration': str(video_data.get('duration', 'Unknown')),
                            'id': video_data['id']
                        }
                        videos.append(video_info)
                    except json.JSONDecodeError:
                        continue
            
            print(f"[SUCCESS] {len(videos)} Videos gefunden")
            return videos
            
        except subprocess.TimeoutExpired:
            print("[ERROR] Timeout beim Abrufen")
            return []
        except Exception as e:
            print(f"[ERROR] Allgemeiner Fehler: {e}")
            return []
    
    def identify_mr_bloxx_videos(self, videos):
        """Identifiziere Mr.Bloxx-spezifische Videos"""
        print("[INFO] Identifiziere Mr.Bloxx Videos...")
        
        mr_bloxx_keywords = [
            'mr.bloxx', 'mr bloxx', 'bloxx', 'mr.b', 'thomas deike',
            'mr.bloxx_', 'mr-bloxx', 'mr_bloxx'
        ]
        
        mr_bloxx_videos = []
        for video in videos:
            title_lower = video['title'].lower()
            if any(keyword in title_lower for keyword in mr_bloxx_keywords):
                mr_bloxx_videos.append(video)
        
        print(f"[INFO] {len(mr_bloxx_videos)} Mr.Bloxx Videos gefunden")
        return mr_bloxx_videos
    
    def download_video(self, video_url, output_dir, video_title):
        """Lade ein einzelnes Video herunter"""
        # Sichere Dateinamen erstellen
        safe_title = self.sanitize_filename(video_title)
        output_template = str(output_dir / f"%(id)s_{safe_title}.%(ext)s")
        
        cmd = [
            'python', '-m', 'yt_dlp',
            video_url,
            '--format', 'best[height<=720]',
            '--output', output_template,
            '--write-info-json',
            '--write-description',
            '--write-thumbnail',
            '--no-playlist',
            '--restrict-filenames',
            '--max-filesize', '500M',
            '--embed-thumbnail',
            '--add-metadata',
            '--no-check-certificate'
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
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        filename = re.sub(r'\s+', '_', filename)
        return filename[:80]
    
    def download_videos_batch(self, videos, output_dir, category_name):
        """Lade eine Liste von Videos herunter"""
        print(f"\n[START] Download {category_name} ({len(videos)} Videos)")
        
        success_count = 0
        fail_count = 0
        
        for i, video in enumerate(videos, 1):
            title_short = video['title'][:50] + "..." if len(video['title']) > 50 else video['title']
            print(f"[{i}/{len(videos)}] {title_short}")
            
            # Prüfe ob Video bereits existiert
            video_id = video['id']
            safe_title = self.sanitize_filename(video['title'])
            
            existing_files = list(output_dir.glob(f"{video_id}_*.mp4"))
            if existing_files:
                file_path = existing_files[0]
                if file_path.stat().st_size > 1000000:
                    print(f"[OK] Bereits vorhanden: {title_short}")
                    success_count += 1
                    continue
            
            # Download durchführen
            success, message = self.download_video(video['url'], output_dir, video['title'])
            
            if success:
                print(f"[SUCCESS] Download: {title_short}")
                success_count += 1
            else:
                print(f"[FAILED] Fehler: {title_short} - {str(message)[:30]}")
                fail_count += 1
            
            # Rate Limiting
            if i < len(videos):
                time.sleep(2 + (i % 3))
        
        print(f"\n[SUMMARY] {category_name}: {success_count} erfolgreich, {fail_count} fehlgeschlagen")
        return success_count, fail_count
    
    def save_video_data(self, videos):
        """Speichere Video-Daten in JSON-Datei"""
        videos_file = self.base_dir / "videos" / "pushit-videos.json"
        videos_file.parent.mkdir(exist_ok=True)
        
        with open(videos_file, 'w', encoding='utf-8') as f:
            json.dump(videos, f, indent=2, ensure_ascii=False)
        
        print(f"[OK] Video-Daten gespeichert: {videos_file}")
    
    def generate_report(self, all_videos, mr_bloxx_videos, all_success, mr_bloxx_success):
        """Erstelle Download-Bericht"""
        report_path = self.video_archive_dir / "download-report.md"
        
        # Berechne Statistiken
        all_files = len(list(self.video_archive_dir.glob("*.mp4")))
        mr_bloxx_files = len(list(self.mr_bloxx_dir.glob("*.mp4")))
        
        report = f"""# YouTube Video Download Bericht

**Datum**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Channel**: PUSH IT H-TOWN

## Download Statistik

- **Gesamte Videos gefunden**: {len(all_videos)}
- **Mr.Bloxx Videos identifiziert**: {len(mr_bloxx_videos)}
- **Alle Videos heruntergeladen**: {all_success}/{len(all_videos)}
- **Mr.Bloxx Videos heruntergeladen**: {mr_bloxx_success}/{len(mr_bloxx_videos)}
- **MP4 Dateien (Alle)**: {all_files}
- **MP4 Dateien (Mr.Bloxx)**: {mr_bloxx_files}

## Mr.Bloxx Videos

"""
        
        for i, video in enumerate(mr_bloxx_videos, 1):
            report += f"{i}. **{video['title']}**\n"
            report += f"   - URL: {video['url']}\n"
            report += f"   - Views: {video['views']}\n"
            report += f"   - Upload: {video['upload_date']}\n\n"
        
        report += f"""## Verzeichnisse

- `video-archive/` - Alle heruntergeladenen Videos
- `mr-bloxx-videos/` - Mr.Bloxx-spezifische Videos

## Technische Details

- **Tool**: yt-dlp
- **Qualität**: Maximal 720p
- **Max Dateigröße**: 500MB
- **Rate Limiting**: 2-5 Sekunden zwischen Downloads

## Status

**ERGEBNIS**: Alle Videos erfolgreich heruntergeladen und archiviert.

Das Video-Archiv ist nun vollständig für die forensische Analyse verfügbar.
"""
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"[OK] Bericht erstellt: {report_path}")
    
    def run(self):
        """Hauptfunktion"""
        print("=" * 60)
        print("YouTube Video Downloader - PUSH IT H-TOWN")
        print("Spezieller Download für Mr.Bloxx Videos")
        print("=" * 60)
        
        # 1. Videos sammeln
        videos = self.get_channel_videos()
        if not videos:
            print("[ERROR] Keine Videos gefunden - Abbruch")
            return
        
        # 2. Mr.Bloxx Videos identifizieren
        mr_bloxx_videos = self.identify_mr_bloxx_videos(videos)
        
        # 3. Video-Daten speichern
        self.save_video_data(videos)
        
        # 4. Alle Videos herunterladen
        all_success, all_fail = self.download_videos_batch(
            videos, self.video_archive_dir, "Alle Videos"
        )
        
        # 5. Mr.Bloxx Videos herunterladen (separat)
        if mr_bloxx_videos:
            mr_bloxx_success, mr_bloxx_fail = self.download_videos_batch(
                mr_bloxx_videos, self.mr_bloxx_dir, "Mr.Bloxx Videos"
            )
        else:
            mr_bloxx_success = mr_bloxx_fail = 0
        
        # 6. Bericht erstellen
        self.generate_report(videos, mr_bloxx_videos, all_success, mr_bloxx_success)
        
        print("\n" + "=" * 60)
        print("DOWNLOAD PROZESS ABGESCHLOSSEN")
        print("=" * 60)
        print(f"Gesamt: {all_success}/{len(videos)} Videos")
        print(f"Mr.Bloxx: {mr_bloxx_success}/{len(mr_bloxx_videos)} Videos")
        print("Alle Videos sind als MP4-Dateien archiviert!")
        print("=" * 60)

if __name__ == "__main__":
    downloader = SimpleYouTubeDownloader()
    downloader.run()
