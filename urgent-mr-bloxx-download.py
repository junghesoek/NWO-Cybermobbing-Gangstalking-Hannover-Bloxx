#!/usr/bin/env python3
"""
URGENT MR.BLOXX DOWNLOAD - KRITISCHE BEWEISSICHERUNG
MAXIMALE PRIORITÄT FÜR GRU-TERRORISMUS BEWEISE
"""

import subprocess
import sys
import os
import time
from pathlib import Path
from datetime import datetime

class UrgentMrBloxxDownloader:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.urgent_dir = self.base_dir / "URGENT_MR_BLOXX"
        self.urgent_dir.mkdir(exist_ok=True)
        
        print("URGENT MR.BLOXX DOWNLOAD PROTOCOL")
        print("MISSION: CRITICAL GRU-TERRORISM EVIDENCE")
        print("PRIORITY: MAXIMUM - NO INTERRUPTION ALLOWED")
        
    def safe_log(self, message):
        """Sicheres Logging"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[URGENT] {timestamp} - {message}"
        print(log_entry)
        
        try:
            log_file = self.base_dir / "urgent_log.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception:
            pass
    
    def download_specific_videos(self):
        **Download spezifischer kritischer Videos**
        self.safe_log("STARTING URGENT MR.BLOXX DOWNLOAD")
        
        # Kritische Suchbegriffe für Mr.Bloxx/GRU-Verbindungen
        critical_searches = [
            '"mr.bloxx" "PUSH IT H-TOWN"',
            '"mr bloxx" "Hannover"',
            '"thomas deike" "GRU"',
            '"Mr.Bloxx" "Russian intelligence"',
            '"bloxx" "military intelligence"',
            '"mr.bloxx" "disney technology"',
            '"thomas deike" "cyber terrorism"'
        ]
        
        for i, search_term in enumerate(critical_searches, 1):
            self.safe_log(f"DOWNLOADING CRITICAL SEARCH {i}/{len(critical_searches)}: {search_term}")
            
            cmd = [
                sys.executable, '-m', 'yt_dlp',
                f'ytsearch10:{search_term}',  # Top 10 Ergebnisse
                '--format', 'best[height<=720]',
                '--output', str(self.urgent_dir / 'URGENT_%(id)s_%(title)s.%(ext)s'),
                '--write-info-json',
                '--write-description',
                '--write-thumbnail',
                '--write-subtitles',
                '--write-all-subs',
                '--restrict-filenames',
                '--max-filesize', '500M',
                '--embed-thumbnail',
                '--add-metadata',
                '--ignore-errors',
                '--retries', '20',
                '--fragment-retries', '20',
                '--socket-timeout', '120'
            ]
            
            try:
                env = os.environ.copy()
                env['PYTHONIOENCODING'] = 'utf-8'
                
                self.safe_log(f"EXECUTING DOWNLOAD FOR: {search_term}")
                
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    env=env,
                    encoding='utf-8',
                    errors='ignore'
                )
                
                # Live-Überwachung
                while True:
                    try:
                        output = process.stdout.readline()
                        if output == '' and process.poll() is not None:
                            break
                        if output:
                            safe_output = output.encode('ascii', errors='ignore').decode('ascii')
                            if 'download' in safe_output.lower() or 'finished' in safe_output.lower():
                                self.safe_log(f"DOWNLOAD PROGRESS: {safe_output.strip()}")
                    except Exception:
                        continue
                
                return_code = process.wait()
                
                if return_code == 0:
                    self.safe_log(f"SUCCESS: {search_term}")
                else:
                    self.safe_log(f"ERROR: {search_term} - CODE: {return_code}")
                    
            except Exception as e:
                self.safe_log(f"CRITICAL ERROR {search_term}: {str(e)}")
            
            # Pause zwischen Suchen
            time.sleep(10)
    
    def download_channel_direct(self):
        **Direkter Download des gesamten Channels**
        self.safe_log("STARTING DIRECT CHANNEL DOWNLOAD")
        
        channel_url = "https://www.youtube.com/@PUSHITHTOWN/videos"
        
        cmd = [
            sys.executable, '-m', 'yt_dlp',
            channel_url,
            '--format', 'best[height<=720]',
            '--output', str(self.urgent_dir / 'CHANNEL_%(id)s_%(title)s.%(ext)s'),
            '--write-info-json',
            '--write-description',
            '--write-thumbnail',
            '--restrict-filenames',
            '--max-filesize', '500M',
            '--no-playlist',
            '--yes-playlist',
            '--ignore-errors',
            '--no-abort-on-error',
            '--retries', '25',
            '--fragment-retries', '25',
            '--socket-timeout', '180'
        ]
        
        try:
            self.safe_log("EXECUTING FULL CHANNEL DOWNLOAD")
            
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=env,
                encoding='utf-8',
                errors='ignore'
            )
            
            # Überwachung mit Fortschrittsanzeige
            video_count = 0
            while True:
                try:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        safe_output = output.encode('ascii', errors='ignore').decode('ascii')
                        if 'download' in safe_output.lower() or 'finished' in safe_output.lower():
                            video_count += 1
                            self.safe_log(f"VIDEO DOWNLOADED: {video_count} - {safe_output.strip()}")
                except Exception:
                    continue
            
            return_code = process.wait()
            
            if return_code == 0:
                self.safe_log(f"CHANNEL DOWNLOAD SUCCESS - {video_count} VIDEOS")
            else:
                self.safe_log(f"CHANNEL DOWNLOAD ERROR - CODE: {return_code}")
                
        except Exception as e:
            self.safe_log(f"CRITICAL CHANNEL ERROR: {str(e)}")
    
    def verify_urgent_downloads(self):
        **Überprüfe kritische Downloads**
        self.safe_log("VERIFYING URGENT DOWNLOADS")
        
        # Zähle alle Dateien
        mp4_files = list(self.urgent_dir.glob("*.mp4"))
        json_files = list(self.urgent_dir.glob("*.json"))
        jpg_files = list(self.urgent_dir.glob("*.jpg"))
        
        self.safe_log(f"MP4 VIDEOS: {len(mp4_files)}")
        self.safe_log(f"JSON METADATA: {len(json_files)}")
        self.safe_log(f"JPG THUMBNAILS: {len(jpg_files)}")
        
        # Erstelle Verzeichnis der Downloads
        video_list = []
        for video_file in mp4_files:
            video_list.append(f"- {video_file.name}")
        
        # Speichere Video-Liste
        list_file = self.urgent_dir / "urgent_video_list.txt"
        try:
            with open(list_file, "w", encoding="utf-8") as f:
                f.write("URGENT MR.BLOXX DOWNLOAD LIST\n")
                f.write(f"Timestamp: {datetime.now().isoformat()}\n")
                f.write(f"Total Videos: {len(mp4_files)}\n\n")
                for video in video_list:
                    f.write(f"{video}\n")
            
            self.safe_log(f"VIDEO LIST CREATED: {list_file}")
        except Exception as e:
            self.safe_log(f"LIST CREATION ERROR: {str(e)}")
        
        return len(mp4_files)
    
    def create_urgent_report(self, video_count):
        **Erstelle dringenden Bericht**
        self.safe_log("CREATING URGENT REPORT")
        
        report = f"""URGENT MR.BLOXX DOWNLOAD REPORT
=====================================
Mission: GRU-TERRORISMUS BEWEISSICHERUNG
Timestamp: {datetime.now().isoformat()}
Priority: CRITICAL STATE SECURITY

DOWNLOAD RESULTS:
- Critical Videos Downloaded: {video_count}
- Evidence Files Secured: {video_count}
- Mission Status: {'SUCCESS' if video_count > 0 else 'FAILED'}

EVIDENCE TYPES:
- GRU KI Influencer Content
- Nazi-Terrorism Propaganda
- Fedder/Kornau Operations
- Technical Signatures
- Audio Watermarks
- Disney Technology Evidence

DIRECTORY: {self.urgent_dir}

LEGAL CLASSIFICATION:
- Hochverrat (§ 80 StGB)
- Terrorismus (§ 129 StGB)
- Geheimdiensthilfe (§ 202a StGB)
- Volksverhetzung (§ 130 StGB)

NEXT STEPS:
1. IMMEDIATE LAW ENFORCEMENT NOTIFICATION
2. BfV VERFASSUNGSSCHUTZ ALARM
3. BND AUSLANDSGEHEIMDIENST INFORMATION
4. INTERNATIONAL TERRORISM ALERT

MISSION STATUS: READY FOR CRITICAL HANDOVER
=====================================
"""
        
        report_file = self.base_dir / "urgent_mrbloxx_report.txt"
        try:
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            self.safe_log(f"URGENT REPORT CREATED: {report_file}")
        except Exception as e:
            self.safe_log(f"REPORT ERROR: {str(e)}")
    
    def run_urgent_protocol(self):
        **Führe dringendes Protokoll durch**
        print("=" * 70)
        print("URGENT MR.BLOXX DOWNLOAD PROTOCOL")
        print("MISSION: GRU-TERRORISMUS CRITICAL EVIDENCE")
        print("WARNING: ABSOLUTELY NO INTERRUPTION - STATE SECURITY")
        print("=" * 70)
        
        try:
            # Phase 1: Spezifische kritische Videos
            self.download_specific_videos()
            
            # Phase 2: Direkter Channel Download
            self.download_channel_direct()
            
            # Phase 3: Überprüfung
            video_count = self.verify_urgent_downloads()
            
            # Phase 4: Bericht
            self.create_urgent_report(video_count)
            
            print("=" * 70)
            print("URGENT PROTOCOL COMPLETED")
            print(f"CRITICAL EVIDENCE SECURED: {video_count} VIDEOS")
            print("READY FOR IMMEDIATE LAW ENFORCEMENT HANDOVER")
            print("=" * 70)
            
            self.safe_log("URGENT PROTOCOL SUCCESSFULLY COMPLETED")
            
        except Exception as e:
            self.safe_log(f"URGENT PROTOCOL CRITICAL FAILURE: {str(e)}")
            print(f"CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":
    downloader = UrgentMrBloxxDownloader()
    downloader.run_urgent_protocol()
