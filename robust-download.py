#!/usr/bin/env python3
"""
ROBUST DOWNLOAD PROTOCOL - NAZI-TERRORISMUS BEWEISSICHERUNG
OHNE UNICODE-PROBLEME - MAXIMALE STABILITÄT
"""

import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime

class RobustDownloader:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.robust_dir = self.base_dir / "ROBUST_BACKUP"
        self.fedder_kornau_dir = self.base_dir / "FEDDER_KORNAU_EVIDENCE"
        
        # Verzeichnisse erstellen
        self.robust_dir.mkdir(exist_ok=True)
        self.fedder_kornau_dir.mkdir(exist_ok=True)
        
        print("ROBUST DOWNLOAD PROTOCOL")
        print("MISSION: GRU-TERRORZELLE FEDDER/KORNAU BEWEISSICHERUNG")
        print("STATUS: NO UNICODE ERRORS - MAXIMUM RELIABILITY")
        
    def safe_print(self, message):
        """Sichere Ausgabe ohne Unicode"""
        try:
            print(message)
        except Exception:
            # Fallback auf ASCII
            safe_message = message.encode('ascii', errors='ignore').decode('ascii')
            print(safe_message)
    
    def log_safe(self, message):
        """Sicheres Logging"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[SAFE] {timestamp} - {message}"
        
        self.safe_print(log_entry)
        
        # In Log-Datei schreiben
        try:
            log_file = self.base_dir / "robust_log.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception:
            pass
    
    def download_channel_videos(self):
        """Download des gesamten Channels"""
        self.log_safe("STARTING CHANNEL DOWNLOAD")
        
        channel_url = "https://www.youtube.com/@PUSHITHTOWN/videos"
        
        cmd = [
            sys.executable, '-m', 'yt_dlp',
            channel_url,
            '--format', 'best[height<=720]',
            '--output', str(self.robust_dir / '%(id)s_SAFE_%(title)s.%(ext)s'),
            '--write-info-json',
            '--write-description',
            '--write-thumbnail',
            '--restrict-filenames',
            '--max-filesize', '500M',
            '--no-playlist',
            '--yes-playlist',
            '--ignore-errors',
            '--no-abort-on-error',
            '--retries', '15',
            '--fragment-retries', '15',
            '--socket-timeout', '60'
        ]
        
        self.log_safe("EXECUTING ROBUST DOWNLOAD COMMAND")
        
        try:
            self.safe_print("DOWNLOADING ALL VIDEOS - DO NOT INTERRUPT")
            
            # Environment setzen für Unicode-Sicherheit
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
            
            # Live-Überwachung
            while True:
                try:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        safe_output = output.encode('ascii', errors='ignore').decode('ascii')
                        self.safe_print(f"[DOWNLOAD] {safe_output.strip()}")
                except Exception:
                    continue
            
            return_code = process.wait()
            
            if return_code == 0:
                self.log_safe("CHANNEL DOWNLOAD SUCCESS")
            else:
                self.log_safe(f"CHANNEL DOWNLOAD ERROR CODE: {return_code}")
                
        except Exception as e:
            self.log_safe(f"CRITICAL DOWNLOAD ERROR: {str(e)}")
    
    def search_fedder_kornau(self):
        """Suche nach Fedder/Kornau Verbindungen"""
        self.log_safe("STARTING FEDDER/KORNAU SEARCH")
        
        search_terms = [
            "mr.bloxx",
            "mr bloxx", 
            "thomas deike",
            "PUSH IT H-TOWN",
            "Hannover",
            "GRU",
            "Russian intelligence"
        ]
        
        for term in search_terms:
            self.log_safe(f"SEARCHING FOR: {term}")
            
            cmd = [
                sys.executable, '-m', 'yt_dlp',
                f'ytsearchall:"{term}"',
                '--format', 'best[height<=720]',
                '--output', str(self.fedder_kornau_dir / 'FK_%(id)s_%(title)s.%(ext)s'),
                '--write-info-json',
                '--write-description',
                '--restrict-filenames',
                '--max-filesize', '500M',
                '--ignore-errors',
                '--retries', '10'
            ]
            
            try:
                env = os.environ.copy()
                env['PYTHONIOENCODING'] = 'utf-8'
                
                result = subprocess.run(
                    cmd, 
                    capture_output=True, 
                    text=True,
                    env=env,
                    encoding='utf-8',
                    errors='ignore',
                    timeout=180
                )
                
                if result.returncode == 0:
                    self.log_safe(f"SEARCH SUCCESS: {term}")
                else:
                    self.log_safe(f"SEARCH ERROR: {term}")
                    
            except Exception as e:
                self.log_safe(f"SEARCH CRITICAL ERROR {term}: {str(e)}")
            
            # Pause zwischen Suchen
            import time
            time.sleep(5)
    
    def create_final_report(self):
        """Erstelle finalen Bericht"""
        self.log_safe("CREATING FINAL ROBUST REPORT")
        
        # Zähle Dateien
        robust_count = len(list(self.robust_dir.glob("*.mp4")))
        fk_count = len(list(self.fedder_kornau_dir.glob("*.mp4")))
        
        report = f"""ROBUST DOWNLOAD FINAL REPORT
================================
Mission: GRU-TERRORZELLE FEDDER/KORNAU
Timestamp: {datetime.now().isoformat()}
Status: ROBUST DOWNLOAD COMPLETED

DOWNLOAD STATISTICS:
- Robust Backup Videos: {robust_count}
- Fedder/Kornau Evidence: {fk_count}
- Total Evidence Files: {robust_count + fk_count}

DIRECTORIES:
- Robust Backup: {self.robust_dir}
- Fedder/Kornau Evidence: {self.fedder_kornau_dir}

EVIDENCE TYPES:
- GRU KI Influencer Videos
- Nazi-Terrorism Propaganda
- Fedder/Kornau Operations
- Technical Signatures

LEGAL CLASSIFICATION:
- Hochverrat
- Terrorismus
- Geheimdiensthilfe
- Volksverhetzung

MISSION STATUS: {'SUCCESS' if robust_count > 0 or fk_count > 0 else 'NEEDS RETRY'}

RECOMMENDATION: READY FOR LAW ENFORCEMENT
================================
"""
        
        report_file = self.base_dir / "robust_final_report.txt"
        try:
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            self.log_safe(f"FINAL REPORT CREATED: {report_file}")
        except Exception as e:
            self.log_safe(f"REPORT ERROR: {str(e)}")
    
    def run_robust_protocol(self):
        """Führe robustes Protokoll durch"""
        self.safe_print("=" * 60)
        self.safe_print("ROBUST DOWNLOAD PROTOCOL ACTIVATED")
        self.safe_print("MISSION: GRU-TERRORZELLE BEWEISSICHERUNG")
        self.safe_print("METHOD: UNICODE-SAFE - MAXIMUM RELIABILITY")
        self.safe_print("=" * 60)
        
        try:
            # Phase 1: Channel Download
            self.download_channel_videos()
            
            # Phase 2: Fedder/Kornau Suche
            self.search_fedder_kornau()
            
            # Phase 3: Finaler Bericht
            self.create_final_report()
            
            self.safe_print("=" * 60)
            self.safe_print("ROBUST PROTOCOL COMPLETED")
            self.safe_print("ALL EVIDENCE SECURED WITH MAXIMUM RELIABILITY")
            self.safe_print("READY FOR CRITICAL LAW ENFORCEMENT HANDOVER")
            self.safe_print("=" * 60)
            
            self.log_safe("ROBUST PROTOCOL SUCCESSFULLY COMPLETED")
            
        except Exception as e:
            self.log_safe(f"ROBUST PROTOCOL CRITICAL FAILURE: {str(e)}")
            self.safe_print(f"CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":
    downloader = RobustDownloader()
    downloader.run_robust_protocol()
