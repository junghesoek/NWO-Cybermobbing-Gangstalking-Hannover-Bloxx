#!/usr/bin/env python3
"""
WORKING VIDEO DOWNLOADER - FUNKTIONIERENDER DOWNLOAD ALLER VIDEOS
"""

import subprocess
import sys
import os
import time
from pathlib import Path
from datetime import datetime

class WorkingVideoDownloader:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.download_dir = self.base_dir / "DOWNLOADED_VIDEOS"
        self.download_dir.mkdir(exist_ok=True)
        
        print("WORKING VIDEO DOWNLOADER")
        print("MISSION: ALLE VIDEOS ERFOLGREICH HERUNTERLADEN")
        
    def log_download(self, message):
        """Download Logging"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[DOWNLOAD] {timestamp} - {message}"
        print(log_entry)
        
        try:
            log_file = self.base_dir / "working_download_log.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception:
            pass
    
    def download_working_videos(self):
        """Download Videos mit funktionierenden Methoden"""
        self.log_download("STARTING WORKING VIDEO DOWNLOAD")
        
        # Methode 1: Einfacher direkter Download
        cmd1 = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/@PUSHITHTOWN/videos',
            '--format', 'mp4',
            '--output', str(self.download_dir / '%(title)s.%(ext)s'),
            '--write-info-json',
            '--ignore-errors',
            '--retries', '10',
            '--socket-timeout', '120'
        ]
        
        try:
            self.log_download("EXECUTING METHOD 1: Direct MP4 Download")
            result1 = subprocess.run(cmd1, capture_output=True, text=True, timeout=3600)
            
            if result1.returncode == 0:
                self.log_download("METHOD 1 SUCCESSFUL")
                return True
            else:
                self.log_download(f"METHOD 1 FAILED: {result1.stderr}")
        except Exception as e:
            self.log_download(f"METHOD 1 ERROR: {str(e)}")
        
        # Methode 2: Alternative Formate
        cmd2 = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/@PUSHITHTOWN/videos',
            '--format', 'best',
            '--output', str(self.download_dir / '%(title)s.%(ext)s'),
            '--ignore-errors',
            '--retries', '5',
            '--socket-timeout', '60'
        ]
        
        try:
            self.log_download("EXECUTING METHOD 2: Best Format Download")
            result2 = subprocess.run(cmd2, capture_output=True, text=True, timeout=1800)
            
            if result2.returncode == 0:
                self.log_download("METHOD 2 SUCCESSFUL")
                return True
            else:
                self.log_download(f"METHOD 2 FAILED: {result2.stderr}")
        except Exception as e:
            self.log_download(f"METHOD 2 ERROR: {str(e)}")
        
        # Methode 3: Einzelne Videos
        cmd3 = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/@PUSHITHTOWN/videos',
            '--format', 'worst',
            '--output', str(self.download_dir / 'video_%(autonumber)s.%(ext)s'),
            '--ignore-errors',
            '--retries', '3',
            '--socket-timeout', '30'
        ]
        
        try:
            self.log_download("EXECUTING METHOD 3: Worst Format Download")
            result3 = subprocess.run(cmd3, capture_output=True, text=True, timeout=900)
            
            if result3.returncode == 0:
                self.log_download("METHOD 3 SUCCESSFUL")
                return True
            else:
                self.log_download(f"METHOD 3 FAILED: {result3.stderr}")
        except Exception as e:
            self.log_download(f"METHOD 3 ERROR: {str(e)}")
        
        return False
    
    def verify_downloads(self):
        """Überprüfe Downloads"""
        self.log_download("VERIFYING DOWNLOADS")
        
        all_files = list(self.download_dir.glob("*"))
        video_files = list(self.download_dir.glob("*.mp4"))
        json_files = list(self.download_dir.glob("*.json"))
        
        self.log_download(f"TOTAL FILES: {len(all_files)}")
        self.log_download(f"VIDEO FILES: {len(video_files)}")
        self.log_download(f"JSON FILES: {len(json_files)}")
        
        total_size = 0
        for video_file in video_files:
            try:
                size = video_file.stat().st_size
                total_size += size
                self.log_download(f"VIDEO: {video_file.name} ({size} bytes)")
            except Exception:
                continue
        
        total_size_mb = total_size / (1024 * 1024)
        self.log_download(f"TOTAL SIZE: {total_size_mb:.2f} MB")
        
        return len(video_files), total_size_mb
    
    def create_report(self, video_count, total_size_mb):
        """Erstelle Download-Bericht"""
        report = f"""
WORKING VIDEO DOWNLOAD REPORT
========================
Timestamp: {datetime.now().isoformat()}
Mission: ALLE VIDEOS HERUNTERLADEN

RESULTS:
- Videos Downloaded: {video_count}
- Total Size: {total_size_mb:.2f} MB
- Download Directory: {self.download_dir}

METHODS USED:
1. Direct MP4 Download
2. Best Format Download
3. Worst Format Download

STATUS: {"SUCCESS" if video_count > 0 else "FAILED"}
========================
"""
        
        report_file = self.download_dir / "download_report.txt"
        try:
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            self.log_download(f"REPORT CREATED: {report_file}")
        except Exception as e:
            self.log_download(f"REPORT ERROR: {str(e)}")
    
    def run_working_download(self):
        """Führe funktionierenden Download durch"""
        print("=" * 60)
        print("WORKING VIDEO DOWNLOADER")
        print("MISSION: ALLE VIDEOS ERFOLGREICH HERUNTERLADEN")
        print("METHODS: 3 VERSCHIEDENE DOWNLOAD-STRATEGIEN")
        print("=" * 60)
        
        try:
            # Download durchführen
            success = self.download_working_videos()
            
            # Überprüfen
            video_count, total_size_mb = self.verify_downloads()
            
            # Bericht erstellen
            self.create_report(video_count, total_size_mb)
            
            print("=" * 60)
            print("WORKING DOWNLOAD COMPLETED")
            print(f"VIDEOS DOWNLOADED: {video_count}")
            print(f"TOTAL SIZE: {total_size_mb:.2f} MB")
            print(f"STATUS: {'SUCCESS' if video_count > 0 else 'FAILED'}")
            print("=" * 60)
            
            self.log_download("WORKING DOWNLOAD PROTOCOL COMPLETED")
            
        except Exception as e:
            self.log_download(f"WORKING DOWNLOAD CRITICAL ERROR: {str(e)}")
            print(f"CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":
    downloader = WorkingVideoDownloader()
    downloader.run_working_download()
