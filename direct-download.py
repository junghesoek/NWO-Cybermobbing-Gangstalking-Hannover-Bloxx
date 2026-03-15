#!/usr/bin/env python3
"""
Direkter YouTube Video Downloader für PUSH IT H-TOWN
"""

import subprocess
import time
import os
from pathlib import Path

def main():
    print("Direkter YouTube Video Downloader")
    print("=" * 40)
    
    # Verzeichnisse erstellen
    base_dir = Path(__file__).parent
    video_archive = base_dir / "video-archive"
    mr_bloxx_dir = base_dir / "mr-bloxx-videos"
    
    video_archive.mkdir(exist_ok=True)
    mr_bloxx_dir.mkdir(exist_ok=True)
    
    print(f"Video-Archiv: {video_archive}")
    print(f"Mr.Bloxx Archiv: {mr_bloxx_dir}")
    
    # Channel URL
    channel_url = "https://www.youtube.com/@PUSHITHTOWN/videos"
    
    print(f"\n1. Sammle Videos von: {channel_url}")
    
    # Zuerst alle Videos herunterladen
    cmd_all = [
        'python', '-m', 'yt_dlp',
        channel_url,
        '--format', 'best[height<=720]',
        '--output', str(video_archive / '%(id)s_%(title)s.%(ext)s'),
        '--write-info-json',
        '--write-description',
        '--write-thumbnail',
        '--restrict-filenames',
        '--max-filesize', '500M',
        '--embed-thumbnail',
        '--add-metadata',
        '--no-playlist',
        '--yes-playlist'
    ]
    
    print("2. Starte Download aller Videos...")
    print("   Dies kann einige Stunden dauern...")
    
    try:
        result = subprocess.run(cmd_all, capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ Alle Videos erfolgreich heruntergeladen!")
        else:
            print(f"   ⚠️  Fehler beim Download: {result.stderr}")
    except Exception as e:
        print(f"   ❌ Fehler: {e}")
    
    print("\n3. Suche Mr.Bloxx Videos...")
    
    # Mr.Bloxx Videos gezielt herunterladen
    mr_bloxx_search = [
        'python', '-m', 'yt_dlp',
        'ytsearchall:"mr.bloxx OR mr bloxx OR bloxx OR thomas deike" "PUSH IT H-TOWN"',
        '--format', 'best[height<=720]',
        '--output', str(mr_bloxx_dir / '%(id)s_%(title)s.%(ext)s'),
        '--write-info-json',
        '--write-description',
        '--write-thumbnail',
        '--restrict-filenames',
        '--max-filesize', '500M',
        '--embed-thumbnail',
        '--add-metadata'
    ]
    
    print("4. Download Mr.Bloxx Videos...")
    
    try:
        result = subprocess.run(mr_bloxx_search, capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ Mr.Bloxx Videos heruntergeladen!")
        else:
            print(f"   ⚠️  Fehler bei Mr.Bloxx Suche: {result.stderr}")
    except Exception as e:
        print(f"   ❌ Fehler: {e}")
    
    # Statistik anzeigen
    print("\n5. Download-Statistik:")
    
    # Zähle Videos
    all_videos = len(list(video_archive.glob("*.mp4")))
    mr_bloxx_videos = len(list(mr_bloxx_dir.glob("*.mp4")))
    
    print(f"   Alle Videos: {all_videos}")
    print(f"   Mr.Bloxx Videos: {mr_bloxx_videos}")
    
    # Berechne Speicherplatz
    def get_dir_size(path):
        total = 0
        for file in path.rglob('*'):
            if file.is_file():
                total += file.stat().st_size
        return total / (1024 * 1024)  # MB
    
    all_size = get_dir_size(video_archive)
    mr_bloxx_size = get_dir_size(mr_bloxx_dir)
    
    print(f"   Speicher (Alle): {all_size:.1f} MB")
    print(f"   Speicher (Mr.Bloxx): {mr_bloxx_size:.1f} MB")
    
    print("\n" + "=" * 40)
    print("DOWNLOAD ABGESCHLOSSEN")
    print("Alle Videos sind als MP4-Dateien archiviert!")
    print("=" * 40)

if __name__ == "__main__":
    main()
