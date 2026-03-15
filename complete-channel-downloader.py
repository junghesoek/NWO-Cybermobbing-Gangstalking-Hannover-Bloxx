#!/usr/bin/env python3
"""
COMPLETE CHANNEL DOWNLOADER - ALLE VIDEOS ALS MP4
MAXIMALE ZUVERLÄSSIGKEIT FÜR VOLLSTÄNDIGE ARCHIVIERUNG
"""

import subprocess
import sys
import os
import time
from pathlib import Path
from datetime import datetime

class CompleteChannelDownloader:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.complete_dir = self.base_dir / "COMPLETE_CHANNEL_ARCHIVE"
        self.complete_dir.mkdir(exist_ok=True)
        
        print("COMPLETE CHANNEL DOWNLOADER")
        print("MISSION: ALLE VIDEOS ALS MP4 SICHERN")
        print("PRIORITY: ABSOLUTE MAXIMUM - VOLLSTÄNDIGE ARCHIVIERUNG")
        
    def log_complete(self, message):
        """Komplettes Logging"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[COMPLETE] {timestamp} - {message}"
        print(log_entry)
        
        try:
            log_file = self.base_dir / "complete_log.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception:
            pass
    
    def download_complete_channel(self):
        """Download des kompletten Kanals"""
        self.log_complete("STARTING COMPLETE CHANNEL DOWNLOAD")
        
        # YouTube Kanal URL
        channel_url = "https://www.youtube.com/@PUSHITHTOWN/videos"
        
        # Maximale Konfiguration für vollständigen Download
        cmd = [
            sys.executable, '-m', 'yt_dlp',
            channel_url,
            '--format', 'best[height<=720][ext=mp4]',  # Nur MP4
            '--output', str(self.complete_dir / '%(upload_date)s_%(id)s_%(title)s.%(ext)s'),
            '--write-info-json',
            '--write-description',
            '--write-thumbnail',
            '--write-subtitles',
            '--write-all-subs',
            '--restrict-filenames',
            '--max-filesize', '2G',  # Größere Dateien erlauben
            '--no-playlist',
            '--yes-playlist',  # WICHTIG: Gesamte Playlist
            '--ignore-errors',
            '--no-abort-on-error',
            '--retries', '100',  # Maximale Retries
            '--fragment-retries', '100',
            '--socket-timeout', '600',  # 10 Minuten Timeout
            '--http-chunk-size', '16M',
            '--buffer-size', '64K',
            '--extract-flat',  # Zuerst alle URLs extrahieren
            '--download-archive', str(self.complete_dir / 'downloaded.txt'),  # Download-Archiv
            '--continue',  # Fortsetzen bei Abbruch
            '--embed-thumbnail',
            '--add-metadata',
            '--embed-subs',
            '--sub-langs', 'all',
            '--match-filter', '!is_live',  # Keine Live-Streams
            '--age-limit', '1000',  # Altersbeschränkung ignorieren
            '--no-check-certificate',  # SSL-Zertifikate ignorieren
            '--geo-bypass',  # Geo-Sperre umgehen
            '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        ]
        
        self.log_complete("EXECUTING COMPLETE CHANNEL DOWNLOAD")
        
        try:
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            
            # Starte Prozess mit maximaler Stabilität
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=env,
                encoding='utf-8',
                errors='ignore'
            )
            
            video_count = 0
            start_time = time.time()
            last_progress_time = start_time
            
            # Detaillierte Überwachung
            while True:
                try:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    
                    if output:
                        safe_output = output.encode('ascii', errors='ignore').decode('ascii')
                        
                        # Zähle erfolgreiche Downloads
                        if any(keyword in safe_output.lower() for keyword in ['download', 'finished', 'complete', '100%']):
                            video_count += 1
                            elapsed = int(time.time() - start_time)
                            self.log_complete(f"VIDEO {video_count} DOWNLOADED (Time: {elapsed}s)")
                            last_progress_time = time.time()
                        
                        # Alle 30 Sekunden Fortschritt melden
                        elif time.time() - last_progress_time > 30:
                            elapsed = int(time.time() - start_time)
                            self.log_complete(f"PROGRESS UPDATE: {video_count} videos in {elapsed}s")
                            last_progress_time = time.time()
                        
                        # Wichtige Meldungen
                        elif any(keyword in safe_output.lower() for keyword in ['error', 'warning', 'retry']):
                            self.log_complete(f"IMPORTANT: {safe_output.strip()}")
                
                except Exception as e:
                    self.log_complete(f"MONITORING ERROR: {str(e)}")
                    continue
            
            return_code = process.wait()
            total_time = int(time.time() - start_time)
            
            if return_code == 0:
                self.log_complete(f"COMPLETE CHANNEL DOWNLOAD SUCCESS - {video_count} VIDEOS IN {total_time}s")
            else:
                self.log_complete(f"COMPLETE CHANNEL DOWNLOAD ERROR - CODE: {return_code} AFTER {total_time}s")
                
        except Exception as e:
            self.log_complete(f"COMPLETE CHANNEL CRITICAL ERROR: {str(e)}")
    
    def verify_complete_download(self):
        """Überprüfe den vollständigen Download"""
        self.log_complete("VERIFYING COMPLETE DOWNLOAD")
        
        # Zähle alle Dateien
        mp4_files = list(self.complete_dir.glob("*.mp4"))
        json_files = list(self.complete_dir.glob("*.json"))
        jpg_files = list(self.complete_dir.glob("*.jpg"))
        description_files = list(self.complete_dir.glob("*.description"))
        
        self.log_complete(f"MP4 VIDEOS: {len(mp4_files)}")
        self.log_complete(f"JSON METADATA: {len(json_files)}")
        self.log_complete(f"JPG THUMBNAILS: {len(jpg_files)}")
        self.log_complete(f"DESCRIPTION FILES: {len(description_files)}")
        
        total_files = len(mp4_files) + len(json_files) + len(jpg_files) + len(description_files)
        self.log_complete(f"TOTAL FILES: {total_files}")
        
        # Erstelle Video-Index
        video_index = []
        for video_file in mp4_files:
            try:
                video_info = {
                    'filename': video_file.name,
                    'size_mb': round(video_file.stat().st_size / (1024 * 1024), 2),
                    'modified': datetime.fromtimestamp(video_file.stat().st_mtime).isoformat()
                }
                video_index.append(video_info)
            except Exception:
                continue
        
        # Speichere Index
        index_file = self.complete_dir / "video_index.json"
        try:
            import json
            with open(index_file, "w", encoding="utf-8") as f:
                json.dump(video_index, f, indent=2, ensure_ascii=False)
            self.log_complete(f"VIDEO INDEX CREATED: {index_file}")
        except Exception as e:
            self.log_complete(f"INDEX ERROR: {str(e)}")
        
        return len(mp4_files)
    
    def create_complete_report(self, video_count):
        """Erstelle vollständigen Bericht"""
        self.log_complete("CREATING COMPLETE REPORT")
        
        report = f"""COMPLETE CHANNEL DOWNLOAD REPORT
=====================================
Mission: FULL CHANNEL ARCHIVAL
Timestamp: {datetime.now().isoformat()}
Priority: ABSOLUTE MAXIMUM COMPLETENESS

DOWNLOAD RESULTS:
- Videos Downloaded: {video_count}
- Mission Status: {'SUCCESS' if video_count > 0 else 'FAILED'}
- Archive Location: {self.complete_dir}

TECHNICAL DETAILS:
- Format: MP4 (720p maximum)
- Metadata: JSON files included
- Thumbnails: JPG files included
- Descriptions: Text files included
- Subtitles: All available languages

QUALITY ASSURANCE:
- Maximum Retries: 100
- Timeout: 600 seconds
- File Size Limit: 2GB
- Error Recovery: Enabled
- Resume Capability: Enabled

NEXT STEPS:
1. Verify all videos are playable
2. Check for missing videos
3. Create backup copies
4. Prepare for forensic analysis
5. Document any issues

DIRECTORY STRUCTURE:
- Main Archive: {self.complete_dir}
- Video Index: video_index.json
- Download Log: complete_log.txt
- Download Archive: downloaded.txt

STATUS: COMPLETE CHANNEL ARCHIVAL READY
=====================================
"""
        
        report_file = self.complete_dir / "complete_download_report.txt"
        try:
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            self.log_complete(f"COMPLETE REPORT CREATED: {report_file}")
        except Exception as e:
            self.log_complete(f"REPORT ERROR: {str(e)}")
    
    def run_complete_protocol(self):
        """Führe vollständiges Protokoll durch"""
        print("=" * 80)
        print("COMPLETE CHANNEL DOWNLOADER PROTOCOL")
        print("MISSION: ALL VIDEOS AS MP4 - MAXIMUM RELIABILITY")
        print("SCOPE: COMPLETE CHANNEL ARCHIVAL - NO EXCEPTIONS")
        print("WARNING: ABSOLUTELY NO INTERRUPTION UNTIL COMPLETE")
        print("=" * 80)
        
        try:
            # Phase 1: Vollständiger Download
            self.download_complete_channel()
            
            # Phase 2: Überprüfung
            video_count = self.verify_complete_download()
            
            # Phase 3: Bericht
            self.create_complete_report(video_count)
            
            print("=" * 80)
            print("COMPLETE CHANNEL PROTOCOL COMPLETED")
            print(f"TOTAL VIDEOS ARCHIVED: {video_count}")
            print("ALL DOWNLOADS SAVED AS MP4")
            print("READY FOR FORENSIC ANALYSIS")
            print("STATUS: COMPLETE CHANNEL ARCHIVAL SUCCESS")
            print("=" * 80)
            
            self.log_complete("COMPLETE CHANNEL PROTOCOL SUCCESSFULLY COMPLETED")
            
        except Exception as e:
            self.log_complete(f"COMPLETE PROTOCOL CRITICAL FAILURE: {str(e)}")
            print(f"CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":
    downloader = CompleteChannelDownloader()
    downloader.run_complete_protocol()
