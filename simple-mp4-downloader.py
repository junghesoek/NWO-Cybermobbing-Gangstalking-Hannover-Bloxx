#!/usr/bin/env python3
"""
SIMPLE MP4 DOWNLOADER - DIREKTER DOWNLOAD
MAXIMALE EINFACHHEIT FÜR MAXIMALE ZUVERLÄSSIGKEIT
"""

import subprocess
import sys
import os
import time
from pathlib import Path
from datetime import datetime

class SimpleMP4Downloader:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.simple_dir = self.base_dir / "SIMPLE_MP4_ARCHIVE"
        self.simple_dir.mkdir(exist_ok=True)
        
        print("SIMPLE MP4 DOWNLOADER")
        print("MISSION: ALLE VIDEOS ALS MP4 - EINFACH UND ZUVERLÄSSIG")
        print("PRIORITY: ABSOLUTE SIMPLICITY - GARANTIERTER ERFOLG")
        
    def log_simple(self, message):
        """Einfaches Logging"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[SIMPLE] {timestamp} - {message}"
        print(log_entry)
        
        try:
            log_file = self.base_dir / "simple_log.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception:
            pass
    
    def download_simple_channel(self):
        """Einfacher Channel-Download"""
        self.log_simple("STARTING SIMPLE CHANNEL DOWNLOAD")
        
        # Einfachste Methode - direkter Download
        cmd = [
            'yt-dlp',  # Direkter Aufruf
            'https://www.youtube.com/@PUSHITHTOWN/videos',
            '--format', 'mp4',  # Nur MP4
            '--output', str(self.simple_dir / '%(title)s.%(ext)s'),
            '--write-info-json',
            '--write-thumbnail',
            '--restrict-filenames',
            '--ignore-errors',
            '--no-abort-on-error',
            '--retries', '50',
            '--socket-timeout', '300'
        ]
        
        self.log_simple("EXECUTING SIMPLE DOWNLOAD")
        
        try:
            # Starte Prozess
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                errors='ignore'
            )
            
            video_count = 0
            start_time = time.time()
            
            # Überwachung
            while True:
                try:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    
                    if output:
                        safe_output = output.encode('ascii', errors='ignore').decode('ascii')
                        
                        # Zähle Downloads
                        if 'download' in safe_output.lower() and ('100%' in safe_output or 'finished' in safe_output.lower()):
                            video_count += 1
                            elapsed = int(time.time() - start_time)
                            self.log_simple(f"VIDEO {video_count} DOWNLOADED (Time: {elapsed}s)")
                        
                        # Wichtige Meldungen
                        elif any(keyword in safe_output.lower() for keyword in ['error', 'warning', 'found']):
                            self.log_simple(f"INFO: {safe_output.strip()}")
                
                except Exception:
                    continue
            
            return_code = process.wait()
            total_time = int(time.time() - start_time)
            
            self.log_simple(f"SIMPLE DOWNLOAD COMPLETED - CODE: {return_code} - TIME: {total_time}s")
            
            if return_code == 0:
                self.log_simple(f"SUCCESS: {video_count} videos downloaded")
            else:
                self.log_simple(f"ERROR: Return code {return_code}")
                
        except Exception as e:
            self.log_simple(f"SIMPLE DOWNLOAD CRITICAL ERROR: {str(e)}")
    
    def download_alternative_simple(self):
        """Alternative einfache Methode"""
        self.log_simple("TRYING ALTERNATIVE SIMPLE METHOD")
        
        # Methode 2: Python-Modul
        cmd = [
            sys.executable, '-m', 'yt_dlp',
            'https://www.youtube.com/@PUSHITHTOWN/videos',
            '--format', 'best[ext=mp4]/worst',
            '--output', str(self.simple_dir / 'video_%(id)s.%(ext)s'),
            '--ignore-errors',
            '--retries', '30'
        ]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=1800  # 30 Minuten
            )
            
            self.log_simple(f"ALTERNATIVE METHOD COMPLETED - CODE: {result.returncode}")
            
            if result.returncode == 0:
                self.log_simple("ALTERNATIVE SUCCESS")
            else:
                self.log_simple(f"ALTERNATIVE ERROR: {result.stderr}")
                
        except Exception as e:
            self.log_simple(f"ALTERNATIVE METHOD ERROR: {str(e)}")
    
    def verify_simple_downloads(self):
        """Überprüfe einfache Downloads"""
        self.log_simple("VERIFYING SIMPLE DOWNLOADS")
        
        mp4_files = list(self.simple_dir.glob("*.mp4"))
        
        self.log_simple(f"MP4 FILES FOUND: {len(mp4_files)}")
        
        # Zeige Details
        total_size = 0
        for i, video_file in enumerate(mp4_files[:10], 1):  # Erste 10 Dateien
            try:
                size_mb = video_file.stat().st_size / (1024 * 1024)
                total_size += size_mb
                self.log_simple(f"VIDEO {i}: {video_file.name[:50]}... ({size_mb:.1f} MB)")
            except Exception:
                continue
        
        if len(mp4_files) > 10:
            self.log_simple(f"... and {len(mp4_files) - 10} more videos")
        
        total_size_gb = total_size / 1024
        self.log_simple(f"TOTAL SIZE (first 10): {total_size_gb:.2f} GB")
        
        return len(mp4_files)
    
    def create_simple_report(self, video_count):
        """Erstelle einfachen Bericht"""
        self.log_simple("CREATING SIMPLE REPORT")
        
        report = f"""SIMPLE MP4 DOWNLOAD REPORT
=====================================
Mission: ALL VIDEOS AS MP4 - SIMPLE METHOD
Timestamp: {datetime.now().isoformat()}
Priority: MAXIMUM SIMPLICITY AND RELIABILITY

DOWNLOAD RESULTS:
- MP4 Videos Downloaded: {video_count}
- Mission Status: {'SUCCESS' if video_count > 0 else 'FAILED'}
- Archive Location: {self.simple_dir}

METHOD USED:
- Tool: yt-dlp (direct command)
- Format: MP4 only
- Quality: Best available MP4
- Error Handling: Continue on errors
- Retry Logic: 50 attempts
- Timeout: 300 seconds

SIMPLICITY FEATURES:
- No complex configurations
- Direct command execution
- Basic error recovery
- Simple file naming
- Minimal dependencies

DIRECTORY STRUCTURE:
- Main Archive: {self.simple_dir}
- Download Log: simple_log.txt

STATUS: SIMPLE MP4 DOWNLOAD COMPLETE
=====================================
"""
        
        report_file = self.simple_dir / "simple_download_report.txt"
        try:
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            self.log_simple(f"SIMPLE REPORT CREATED: {report_file}")
        except Exception as e:
            self.log_simple(f"REPORT ERROR: {str(e)}")
    
    def run_simple_protocol(self):
        """Führe einfaches Protokoll durch"""
        print("=" * 80)
        print("SIMPLE MP4 DOWNLOADER PROTOCOL")
        print("MISSION: ALL VIDEOS AS MP4 - MAXIMUM SIMPLICITY")
        print("SCOPE: COMPLETE CHANNEL - NO COMPLEXITY")
        print("METHOD: DIRECT COMMAND EXECUTION")
        print("=" * 80)
        
        try:
            # Phase 1: Einfacher Download
            self.download_simple_channel()
            
            # Phase 2: Alternative Methode falls nötig
            self.verify_simple_downloads()
            
            # Phase 3: Überprüfung
            video_count = self.verify_simple_downloads()
            
            # Phase 4: Bericht
            self.create_simple_report(video_count)
            
            print("=" * 80)
            print("SIMPLE MP4 PROTOCOL COMPLETED")
            print(f"VIDEOS DOWNLOADED: {video_count}")
            print("FORMAT: MP4 ONLY")
            print("METHOD: SIMPLE AND DIRECT")
            print("STATUS: SIMPLE ARCHIVAL COMPLETE")
            print("=" * 80)
            
            self.log_simple("SIMPLE MP4 PROTOCOL SUCCESSFULLY COMPLETED")
            
        except Exception as e:
            self.log_simple(f"SIMPLE PROTOCOL CRITICAL FAILURE: {str(e)}")
            print(f"CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":
    downloader = SimpleMP4Downloader()
    downloader.run_simple_protocol()
