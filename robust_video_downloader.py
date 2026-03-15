#!/usr/bin/env python3
"""
ROBUST VIDEO DOWNLOADER - ROBUSTER DOWNLOAD MIT ALTERNATIVEN
"""

import subprocess
import sys
import os
import time
from pathlib import Path
from datetime import datetime

class RobustVideoDownloader:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.download_dir = self.base_dir / "ROBUST_VIDEOS"
        self.download_dir.mkdir(exist_ok=True)
        
        print("ROBUST VIDEO DOWNLOADER")
        print("MISSION: ROBUSTER DOWNLOAD ALLER VIDEOS")
        
    def log_robust(self, message):
        """Robust Logging"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[ROBUST] {timestamp} - {message}"
        print(log_entry)
        
        try:
            log_file = self.base_dir / "robust_download_log.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception:
            pass
    
    def try_download_method(self, method_name, cmd):
        """Versuche Download-Methode"""
        self.log_robust(f"TRYING METHOD: {method_name}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=1200)
            
            if result.returncode == 0:
                self.log_robust(f"METHOD {method_name} SUCCESS")
                return True
            else:
                self.log_robust(f"METHOD {method_name} FAILED: {result.stderr[:200]}")
                return False
                
        except Exception as e:
            self.log_robust(f"METHOD {method_name} ERROR: {str(e)}")
            return False
    
    def download_robust_videos(self):
        """Robuster Download mit vielen Methoden"""
        self.log_robust("STARTING ROBUST VIDEO DOWNLOAD")
        
        # Methode 1: yt-dlp mit mp4
        cmd1 = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/@PUSHITHTOWN/videos',
            '--format', 'mp4',
            '--output', str(self.download_dir / 'mp4_%(title)s.%(ext)s'),
            '--ignore-errors',
            '--retries', '10',
            '--socket-timeout', '180'
        ]
        
        if self.try_download_method("MP4_DIRECT", cmd1):
            return True
        
        # Methode 2: yt-dlp mit best
        cmd2 = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/@PUSHITHTOWN/videos',
            '--format', 'best',
            '--output', str(self.download_dir / 'best_%(title)s.%(ext)s'),
            '--ignore-errors',
            '--retries', '8',
            '--socket-timeout', '120'
        ]
        
        if self.try_download_method("BEST_FORMAT", cmd2):
            return True
        
        # Methode 3: yt-dlp mit worst
        cmd3 = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/@PUSHITHTOWN/videos',
            '--format', 'worst',
            '--output', str(self.download_dir / 'worst_%(title)s.%(ext)s'),
            '--ignore-errors',
            '--retries', '5',
            '--socket-timeout', '60'
        ]
        
        if self.try_download_method("WORST_FORMAT", cmd3):
            return True
        
        # Methode 4: yt-dlp mit alternativer URL
        cmd4 = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/c/PUSHITHTOWN',
            '--format', 'mp4',
            '--output', str(self.download_dir / 'alt_%(title)s.%(ext)s'),
            '--ignore-errors',
            '--retries', '5',
            '--socket-timeout', '60'
        ]
        
        if self.try_download_method("ALT_URL", cmd4):
            return True
        
        # Methode 5: yt-dlp mit playlist
        cmd5 = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/playlist?list=UU...',
            '--format', 'mp4',
            '--output', str(self.download_dir / 'playlist_%(title)s.%(ext)s'),
            '--ignore-errors',
            '--retries', '3',
            '--socket-timeout', '30'
        ]
        
        if self.try_download_method("PLAYLIST", cmd5):
            return True
        
        return False
    
    def check_downloads(self):
        """Überprüfe Downloads"""
        self.log_robust("CHECKING DOWNLOADS")
        
        all_files = list(self.download_dir.glob("*"))
        video_files = [f for f in all_files if f.suffix.lower() in ['.mp4', '.avi', '.mov', '.mkv']]
        
        self.log_robust(f"TOTAL FILES: {len(all_files)}")
        self.log_robust(f"VIDEO FILES: {len(video_files)}")
        
        for video_file in video_files:
            try:
                size = video_file.stat().st_size
                self.log_robust(f"VIDEO: {video_file.name} ({size} bytes)")
            except Exception:
                continue
        
        return len(video_files)
    
    def run_robust_download(self):
        """Führe robusten Download durch"""
        print("=" * 60)
        print("ROBUST VIDEO DOWNLOADER")
        print("MISSION: ROBUSTER DOWNLOAD ALLER VIDEOS")
        print("METHODS: 5 VERSCHIEDENE DOWNLOAD-STRATEGIEN")
        print("=" * 60)
        
        try:
            # Download durchführen
            success = self.download_robust_videos()
            
            # Überprüfen
            video_count = self.check_downloads()
            
            print("=" * 60)
            print("ROBUST DOWNLOAD COMPLETED")
            print(f"VIDEOS DOWNLOADED: {video_count}")
            print(f"STATUS: {'SUCCESS' if video_count > 0 else 'ALL METHODS FAILED'}")
            print("=" * 60)
            
            self.log_robust("ROBUST DOWNLOAD PROTOCOL COMPLETED")
            
        except Exception as e:
            self.log_robust(f"ROBUST DOWNLOAD CRITICAL ERROR: {str(e)}")
            print(f"CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":
    downloader = RobustVideoDownloader()
    downloader.run_robust_download()
