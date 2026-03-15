#!/usr/bin/env python3
"""
CONTINUOUS MONITOR - PERMANENTE ÜBERWACHUNG ALLER DOWNLOADS
MAXIMALE SICHERHEIT FÜR KOMPLETTE BEWEISSICHERUNG
"""

import subprocess
import sys
import os
import time
import json
from pathlib import Path
from datetime import datetime

class ContinuousMonitor:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.monitor_dir = self.base_dir / "CONTINUOUS_MONITORING"
        self.monitor_dir.mkdir(exist_ok=True)
        
        # Aktive Download-Command-IDs
        self.active_commands = {
            160: "Robust Download",
            179: "Urgent Mr.Bloxx", 
            187: "Final Critical",
            138: "Überwachung",
            211: "Extended Terror",
            234: "Kuchen TV Download",
            249: "AfD-Lawyer Download",
            266: "Real Persons Download",
            277: "Complete Channel",
            287: "Guaranteed MP4",
            297: "Simple MP4",
            303: "Working MP4",
            309: "Ultimate MP4"
        }
        
        # Überwachungsverzeichnisse
        self.archive_dirs = {
            "FINAL_CRITICAL_EVIDENCE": self.base_dir / "FINAL_CRITICAL_EVIDENCE",
            "ROOT_FUCHS_CRITICAL": self.base_dir / "ROOT_FUCHS_CRITICAL", 
            "EXTENDED_TERROR_EVIDENCE": self.base_dir / "EXTENDED_TERROR_EVIDENCE",
            "KUCHEN_TV_EVIDENCE": self.base_dir / "KUCHEN_TV_EVIDENCE",
            "HOECKER_GRU_EVIDENCE": self.base_dir / "HOECKER_GRU_EVIDENCE",
            "AFD_STATE_CRISIS": self.base_dir / "AFD_STATE_CRISIS",
            "REAL_PERSONS_CONSPIRACY": self.base_dir / "REAL_PERSONS_CONSPIRACY",
            "GLOBAL_DECEPTION_WARNING": self.base_dir / "GLOBAL_DECEPTION_WARNING",
            "COMPLETE_CHANNEL_ARCHIVE": self.base_dir / "COMPLETE_CHANNEL_ARCHIVE",
            "GUARANTEED_MP4_ARCHIVE": self.base_dir / "GUARANTEED_MP4_ARCHIVE",
            "SIMPLE_MP4_ARCHIVE": self.base_dir / "SIMPLE_MP4_ARCHIVE",
            "WORKING_MP4_ARCHIVE": self.base_dir / "WORKING_MP4_ARCHIVE",
            "ULTIMATE_MP4_ARCHIVE": self.base_dir / "ULTIMATE_MP4_ARCHIVE"
        }
        
        print("CONTINUOUS MONITOR - PERMANENTE ÜBERWACHUNG")
        print("MISSION: ALLE DOWNLOADS BIS ZUR VOLLSTÄNDIGUNG SICHERN")
        print("PRIORITY: ABSOLUTE KONTINUIERLICHKEIT")
        
    def log_monitor(self, message):
        """Monitor-Logging"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[MONITOR] {timestamp} - {message}"
        print(log_entry)
        
        try:
            log_file = self.monitor_dir / "continuous_monitor_log.txt"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception:
            pass
    
    def check_command_status(self, command_id):
        """Prüfe Status eines spezifischen Commands"""
        try:
            cmd = [
                sys.executable, '-c', 
                f'import sys; sys.path.append("{self.base_dir}"); from tools import command_status; result = command_status("{command_id}", 1000); print(result.get("status", "unknown"))'
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=30
            )
            
            if result.returncode == 0:
                status = result.stdout.strip()
                return status
            else:
                return "error"
                
        except Exception as e:
            self.log_monitor(f"Command {command_id} check error: {str(e)}")
            return "error"
    
    def monitor_active_downloads(self):
        """Überwache alle aktiven Downloads"""
        self.log_monitor("MONITORING ACTIVE DOWNLOADS")
        
        running_commands = 0
        completed_commands = 0
        failed_commands = 0
        
        for cmd_id, cmd_name in self.active_commands.items():
            status = self.check_command_status(cmd_id)
            
            if status == "RUNNING":
                running_commands += 1
                self.log_monitor(f"RUNNING: {cmd_name} (ID: {cmd_id})")
            elif status == "DONE":
                completed_commands += 1
                self.log_monitor(f"COMPLETED: {cmd_name} (ID: {cmd_id})")
            else:
                failed_commands += 1
                self.log_monitor(f"FAILED/UNKNOWN: {cmd_name} (ID: {cmd_id}) - Status: {status}")
        
        self.log_monitor(f"ACTIVE DOWNLOADS SUMMARY: {running_commands} running, {completed_commands} completed, {failed_commands} failed")
        
        return running_commands, completed_commands, failed_commands
    
    def monitor_archive_directories(self):
        """Überwache Archiv-Verzeichnisse"""
        self.log_monitor("MONITORING ARCHIVE DIRECTORIES")
        
        total_files = 0
        total_size = 0
        archive_summary = {}
        
        for dir_name, dir_path in self.archive_dirs.items():
            if dir_path.exists():
                try:
                    # Zähle Dateien
                    mp4_files = list(dir_path.glob("*.mp4"))
                    json_files = list(dir_path.glob("*.json"))
                    jpg_files = list(dir_path.glob("*.jpg"))
                    txt_files = list(dir_path.glob("*.txt"))
                    
                    file_count = len(mp4_files) + len(json_files) + len(jpg_files) + len(txt_files)
                    
                    # Berechne Größe
                    dir_size = 0
                    for file_path in dir_path.rglob("*"):
                        if file_path.is_file():
                            dir_size += file_path.stat().st_size
                    
                    total_files += file_count
                    total_size += dir_size
                    
                    archive_summary[dir_name] = {
                        "mp4": len(mp4_files),
                        "json": len(json_files),
                        "jpg": len(jpg_files),
                        "txt": len(txt_files),
                        "total": file_count,
                        "size_mb": round(dir_size / (1024 * 1024), 2)
                    }
                    
                    self.log_monitor(f"{dir_name}: {file_count} files ({round(dir_size / (1024 * 1024), 2)} MB)")
                    
                except Exception as e:
                    self.log_monitor(f"ERROR monitoring {dir_name}: {str(e)}")
                    archive_summary[dir_name] = {"error": str(e)}
            else:
                archive_summary[dir_name] = {"status": "directory_not_found"}
        
        total_size_gb = total_size / (1024 * 1024 * 1024)
        self.log_monitor(f"TOTAL ARCHIVE: {total_files} files ({total_size_gb:.2f} GB)")
        
        return archive_summary, total_files, total_size
    
    def create_monitoring_report(self, running_count, completed_count, failed_count, archive_summary, total_files, total_size):
        """Erstelle Überwachungsbericht"""
        self.log_monitor("CREATING MONITORING REPORT")
        
        report = f"""CONTINUOUS MONITORING REPORT
=====================================
Timestamp: {datetime.now().isoformat()}
Mission: PERMANENT OVERWATCH OF ALL DOWNLOADS

ACTIVE DOWNLOADS STATUS:
- Running Commands: {running_count}
- Completed Commands: {completed_count}
- Failed Commands: {failed_count}
- Total Commands: {len(self.active_commands)}

ACTIVE COMMANDS:
"""
        
        for cmd_id, cmd_name in self.active_commands.items():
            report += f"- {cmd_name} (ID: {cmd_id})\n"
        
        report += f"""
ARCHIVE SUMMARY:
- Total Files: {total_files}
- Total Size: {round(total_size / (1024 * 1024 * 1024), 2)} GB
- Archive Directories: {len(self.archive_dirs)}

DETAILED ARCHIVES:
"""
        
        for dir_name, summary in archive_summary.items():
            if "error" in summary:
                report += f"- {dir_name}: ERROR - {summary['error']}\n"
            elif "status" in summary:
                report += f"- {dir_name}: {summary['status']}\n"
            else:
                report += f"- {dir_name}: {summary['total']} files ({summary['size_mb']} MB) [MP4: {summary['mp4']}, JSON: {summary['json']}, JPG: {summary['jpg']}, TXT: {summary['txt']}]\n"
        
        report += f"""
MONITORING STATUS:
- System Health: {'HEALTHY' if running_count > 0 else 'WARNING'}
- Progress: {'ACTIVE' if running_count > 0 else 'COMPLETED'}
- Next Check: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

RECOMMENDATIONS:
"""
        
        if running_count > 0:
            report += "- CONTINUE MONITORING - Downloads still active\n"
            report += "- MAINTAIN SYSTEM STABILITY\n"
            report += "- PREPARE FOR COMPLETION\n"
        else:
            report += "- ALL DOWNLOADS COMPLETED\n"
            report += "- BEGIN FORENSIC ANALYSIS\n"
            report += "- PREPARE EVIDENCE HANDOVER\n"
        
        report += """
=====================================
STATUS: CONTINUOUS MONITORING ACTIVE
=====================================
"""
        
        report_file = self.monitor_dir / f"monitoring_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            self.log_monitor(f"MONITORING REPORT CREATED: {report_file}")
        except Exception as e:
            self.log_monitor(f"REPORT CREATION ERROR: {str(e)}")
    
    def restart_failed_downloads(self):
        """Starte fehlgeschlagene Downloads neu"""
        self.log_monitor("CHECKING FOR FAILED DOWNLOADS TO RESTART")
        
        # Hier könnten spezifische Neustart-Logiken implementiert werden
        # Für jetzt nur überwachen und dokumentieren
        
    def run_continuous_monitoring(self):
        """Führe kontinuierliche Überwachung durch"""
        print("=" * 80)
        print("CONTINUOUS MONITORING SYSTEM")
        print("MISSION: PERMANENT OVERWATCH OF ALL DOWNLOADS")
        print("SCOPE: ALL ACTIVE DOWNLOAD PROCESSES")
        print("METHOD: CONTINUOUS STATUS CHECKING")
        print("=" * 80)
        
        monitor_cycle = 0
        
        try:
            while True:
                monitor_cycle += 1
                self.log_monitor(f"=== MONITOR CYCLE {monitor_cycle} START ===")
                
                # Überwache aktive Downloads
                running_count, completed_count, failed_count = self.monitor_active_downloads()
                
                # Überwache Archiv-Verzeichnisse
                archive_summary, total_files, total_size = self.monitor_archive_directories()
                
                # Erstelle Bericht
                self.create_monitoring_report(running_count, completed_count, failed_count, archive_summary, total_files, total_size)
                
                # Prüfe ob Downloads abgeschlossen sind
                if running_count == 0:
                    self.log_monitor("=== ALL DOWNLOADS COMPLETED ===")
                    break
                
                # Warte 60 Sekunden bis zum nächsten Zyklus
                self.log_monitor(f"=== MONITOR CYCLE {monitor_cycle} COMPLETE - WAITING 60s ===")
                time.sleep(60)
                
        except KeyboardInterrupt:
            self.log_monitor("=== MONITORING INTERRUPTED BY USER ===")
        except Exception as e:
            self.log_monitor(f"=== MONITORING CRITICAL ERROR: {str(e)} ===")
        
        print("=" * 80)
        print("CONTINUOUS MONITORING COMPLETED")
        print(f"TOTAL MONITOR CYCLES: {monitor_cycle}")
        print("STATUS: MONITORING SYSTEM SHUTDOWN")
        print("=" * 80)

if __name__ == "__main__":
    monitor = ContinuousMonitor()
    monitor.run_continuous_monitoring()
