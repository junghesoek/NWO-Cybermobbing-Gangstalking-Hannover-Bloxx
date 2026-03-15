#!/usr/bin/env python3
"""
KONTINUIERLICHE ÜBERWACHUNG - BEWEISSICHERUNG NAZI-TERRORISMUS
STÄNDIGE MONITORING ALLER DOWNLOAD-PROZESSE
"""

import time
import os
from pathlib import Path
from datetime import datetime

class DownloadMonitor:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.emergency_dir = self.base_dir / "EMERGENCY_BACKUP"
        self.mr_bloxx_dir = self.base_dir / "MR_BLOXX_CRITICAL"
        self.video_archive = self.base_dir / "video-archive"
        
        print("[MONITOR] BEWEISSICHERUNG ÜBERWACHUNG AKTIV")
        print("[MONITOR] NAZI-TERRORISMUS NETZWERK - KRITISCHE MISSION")
        
    def count_files(self):
        """Zähle heruntergeladene Dateien"""
        emergency_count = len(list(self.emergency_dir.glob("*.mp4")))
        mr_bloxx_count = len(list(self.mr_bloxx_dir.glob("*.mp4")))
        archive_count = len(list(self.video_archive.glob("*.mp4")))
        
        return emergency_count, mr_bloxx_count, archive_count
    
    def calculate_size(self, directory):
        """Berechne Verzeichnisgröße"""
        total_size = 0
        try:
            for file in directory.rglob('*'):
                if file.is_file():
                    total_size += file.stat().st_size
            return total_size / (1024 * 1024)  # MB
        except:
            return 0
    
    def monitor_loop(self):
        """Kontinuierliche Überwachung"""
        print("[MONITOR] START KONTINUIERLICHE ÜBERWACHUNG")
        print("[MONITOR] KEINE UNTERBRECHUNG ERLAUBT")
        
        while True:
            try:
                # Dateien zählen
                emergency_count, mr_bloxx_count, archive_count = self.count_files()
                
                # Größen berechnen
                emergency_size = self.calculate_size(self.emergency_dir)
                mr_bloxx_size = self.calculate_size(self.mr_bloxx_dir)
                archive_size = self.calculate_size(self.video_archive)
                
                # Status ausgeben
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n[{timestamp}] DOWNLOAD STATUS:")
                print(f"  Emergency Backup: {emergency_count} Videos ({emergency_size:.1f} MB)")
                print(f"  Mr.Bloxx Critical: {mr_bloxx_count} Videos ({mr_bloxx_size:.1f} MB)")
                print(f"  Video Archive: {archive_count} Videos ({archive_size:.1f} MB)")
                print(f"  TOTAL: {emergency_count + mr_bloxx_count + archive_count} Videos")
                
                # Prüfe auf Logs
                log_file = self.base_dir / "emergency_log.txt"
                if log_file.exists():
                    with open(log_file, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        if lines:
                            print(f"  Latest Log: {lines[-1].strip()}")
                
                # Prüfe ob Downloads abgeschlossen sind
                total_videos = emergency_count + mr_bloxx_count + archive_count
                if total_videos >= 100:  # Mindestens 100 Videos als Ziel
                    print(f"\n[SUCCESS] KRITISCHES ZIEL ERREICHT: {total_videos} VIDEOS")
                    print("[SUCCESS] BEWEISSICHERUNG IM GANGE")
                
                # Warte 30 Sekunden vor nächster Überprüfung
                time.sleep(30)
                
            except KeyboardInterrupt:
                print("\n[WARNING] ÜBERWACHUNG UNTERBROCHEN - DOWNLOADS LAUFEN WEITER")
                time.sleep(5)  # Kurze Pause, dann weiter
                continue
            except Exception as e:
                print(f"\n[ERROR] MONITORING FEHLER: {e}")
                time.sleep(10)
                continue
    
    def check_processes(self):
        """Prüfe ob Download-Prozesse laufen"""
        try:
            # Prüfe Python-Prozesse
            result = os.popen('tasklist | findstr python').read()
            python_processes = result.count('\n')
            
            print(f"[INFO] {python_processes} Python-Prozesse aktiv")
            
            if python_processes >= 2:
                print("[INFO] MULTIPLE DOWNLOAD PROZESSE AKTIV - GUT")
            else:
                print("[WARNING] WENIGER ALS ERWARTETE PROZESSE")
                
        except Exception as e:
            print(f"[ERROR] PROZESS-CHECK FEHLER: {e}")

if __name__ == "__main__":
    monitor = DownloadMonitor()
    monitor.check_processes()
    monitor.monitor_loop()
