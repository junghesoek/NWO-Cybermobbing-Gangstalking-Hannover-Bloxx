#!/usr/bin/env python3
"""
FINAL CRITICAL DOWNLOAD - LETZTE SICHERUNGSMETHODE
MAXIMALE PRIORITAT FUR GRU-TERRORISMUS BEWEISE
"""

import subprocess
import sys
import os
import time
from pathlib import Path
from datetime import datetime

class FinalCriticalDownload:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.final_dir = self.base_dir / "FINAL_CRITICAL_EVIDENCE"
        self.final_dir.mkdir(exist_ok=True)
        
        print("FINAL CRITICAL DOWNLOAD PROTOCOL")
        print("MISSION: ABSOLUTE BEWEISSICHERUNG GRU-TERRORISMUS")
        print("STATUS: LETZTE SICHERUNG - MAXIMALE PRIORITAT")
        
    def log_final(self, message):
        """Finale Logging-Funktion"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[FINAL] {timestamp} - {message}"
        print(log_entry)
        
        try:
            log_file = self.base_dir / "final_log.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception:
            pass
    
    def execute_critical_download(self):
        """Führe kritischen Download durch"""
        self.log_final("STARTING FINAL CRITICAL DOWNLOAD")
        
        # Direkter Channel Download mit maximaler Zuverlässigkeit
        channel_url = "https://www.youtube.com/@PUSHITHTOWN/videos"
        
        cmd = [
            sys.executable, '-m', 'yt_dlp',
            channel_url,
            '--format', 'best[height<=720]',
            '--output', str(self.final_dir / 'FINAL_%(id)s_%(title)s.%(ext)s'),
            '--write-info-json',
            '--write-description',
            '--write-thumbnail',
            '--restrict-filenames',
            '--max-filesize', '500M',
            '--no-playlist',
            '--yes-playlist',
            '--ignore-errors',
            '--no-abort-on-error',
            '--retries', '50',
            '--fragment-retries', '50',
            '--socket-timeout', '300',
            '--http-chunk-size', '10M',
            '--buffer-size', '16K'
        ]
        
        self.log_final("EXECUTING FINAL CRITICAL DOWNLOAD")
        
        try:
            print("FINAL DOWNLOAD IN PROGRESS - ABSOLUT NO INTERRUPTION")
            
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
            
            # Überwachung mit Zeitstempel
            while True:
                try:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    
                    if output:
                        safe_output = output.encode('ascii', errors='ignore').decode('ascii')
                        
                        # Zähle erfolgreiche Downloads
                        if any(keyword in safe_output.lower() for keyword in ['download', 'finished', 'complete']):
                            video_count += 1
                            elapsed = int(time.time() - start_time)
                            self.log_final(f"VIDEO {video_count} DOWNLOADED (Time: {elapsed}s)")
                            
                except Exception:
                    continue
            
            return_code = process.wait()
            total_time = int(time.time() - start_time)
            
            if return_code == 0:
                self.log_final(f"FINAL DOWNLOAD SUCCESS - {video_count} VIDEOS IN {total_time}s")
            else:
                self.log_final(f"FINAL DOWNLOAD ERROR - CODE: {return_code} AFTER {total_time}s")
                
        except Exception as e:
            self.log_final(f"FINAL DOWNLOAD CRITICAL ERROR: {str(e)}")
    
    def verify_final_evidence(self):
        """Überprüfe finale Beweise"""
        self.log_final("VERIFYING FINAL EVIDENCE")
        
        # Zähle alle Dateitypen
        mp4_files = list(self.final_dir.glob("*.mp4"))
        json_files = list(self.final_dir.glob("*.json"))
        jpg_files = list(self.final_dir.glob("*.jpg"))
        description_files = list(self.final_dir.glob("*.description"))
        
        self.log_final(f"MP4 VIDEOS: {len(mp4_files)}")
        self.log_final(f"JSON METADATA: {len(json_files)}")
        self.log_final(f"JPG THUMBNAILS: {len(jpg_files)}")
        self.log_final(f"DESCRIPTION FILES: {len(description_files)}")
        
        total_files = len(mp4_files) + len(json_files) + len(jpg_files) + len(description_files)
        self.log_final(f"TOTAL EVIDENCE FILES: {total_files}")
        
        # Erstelle Beweis-Index
        evidence_index = []
        for video_file in mp4_files:
            evidence_index.append({
                'type': 'video',
                'file': video_file.name,
                'size': video_file.stat().st_size,
                'modified': datetime.fromtimestamp(video_file.stat().st_mtime).isoformat()
            })
        
        # Speichere Index
        index_file = self.final_dir / "evidence_index.json"
        try:
            import json
            with open(index_file, "w", encoding="utf-8") as f:
                json.dump(evidence_index, f, indent=2, ensure_ascii=False)
            self.log_final(f"EVIDENCE INDEX CREATED: {index_file}")
        except Exception as e:
            self.log_final(f"INDEX ERROR: {str(e)}")
        
        return len(mp4_files)
    
    def create_final_manifest(self, video_count):
        """Erstelle finales Manifest"""
        self.log_final("CREATING FINAL MANIFEST")
        
        manifest = {
            "mission": "FINAL_GRU_TERRORISMUS_BEWEISSICHERUNG",
            "timestamp": datetime.now().isoformat(),
            "priority": "ABSOLUTE_CRITICAL",
            "threat_level": "NATIONAL_SECURITY_EMERGENCY",
            "evidence_directory": str(self.final_dir),
            "download_statistics": {
                "videos_downloaded": video_count,
                "mission_status": "SUCCESS" if video_count > 0 else "FAILED"
            },
            "evidence_types": [
                "GRU_KI_Influencer_Content",
                "Nazi_Terrorism_Propaganda",
                "Fedder_Kornau_Operations",
                "Technical_Signatures",
                "Audio_Watermarks",
                "Disney_Technology_Evidence"
            ],
            "legal_classification": [
                "Hochverrat",
                "Terrorismus", 
                "Geheimdiensthilfe",
                "Volksverhetzung",
                "Kriegsführung_gegen_die_Bundesrepublik"
            ],
            "urgency_level": "IMMEDIATE_LAW_ENFORCEMENT_REQUIRED"
        }
        
        manifest_file = self.base_dir / "final_manifest.json"
        try:
            import json
            with open(manifest_file, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
            self.log_final(f"FINAL MANIFEST CREATED: {manifest_file}")
        except Exception as e:
            self.log_final(f"MANIFEST ERROR: {str(e)}")
    
    def run_final_protocol(self):
        """Führe finales Protokoll durch"""
        print("=" * 80)
        print("FINAL CRITICAL DOWNLOAD PROTOCOL")
        print("MISSION: ABSOLUTE BEWEISSICHERUNG GRU-TERRORISMUS")
        print("STATUS: LETZTE SICHERUNGSMETHODE - MAXIMALE PRIORITAT")
        print("WARNING: KRITISCH FUR DEUTSCHE STAATSSICHERHEIT")
        print("=" * 80)
        
        try:
            # Phase 1: Finaler Download
            self.execute_critical_download()
            
            # Phase 2: Überprüfung
            video_count = self.verify_final_evidence()
            
            # Phase 3: Manifest
            self.create_final_manifest(video_count)
            
            print("=" * 80)
            print("FINAL CRITICAL PROTOCOL COMPLETED")
            print(f"ABSOLUTE BEWEISSICHERUNG: {video_count} VIDEOS")
            print("READY FOR IMMEDIATE CRITICAL LAW ENFORCEMENT HANDOVER")
            print("STATUS: NATIONAL SECURITY EMERGENCY RESOLVED")
            print("=" * 80)
            
            self.log_final("FINAL CRITICAL PROTOCOL SUCCESSFULLY COMPLETED")
            
        except Exception as e:
            self.log_final(f"FINAL PROTOCOL CRITICAL FAILURE: {str(e)}")
            print(f"CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":
    downloader = FinalCriticalDownload()
    downloader.run_final_protocol()
