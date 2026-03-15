#!/usr/bin/env python3
"""
SIMPLE VIDEO DOWNLOADER - EINFACHER FUNKTIONIERENDER DOWNLOAD
"""

import subprocess
import sys
import os
from pathlib import Path

def simple_download():
    """Einfacher Download"""
    base_dir = Path(__file__).parent
    download_dir = base_dir / "SIMPLE_VIDEOS"
    download_dir.mkdir(exist_ok=True)
    
    print("SIMPLE VIDEO DOWNLOADER")
    print("DOWNLOADING VIDEOS...")
    
    cmd = [
        sys.executable, '-m', 'yt_dlp',
        'https://www.youtube.com/@PUSHITHTOWN/videos',
        '--format', 'mp4',
        '--output', str(download_dir / '%(title)s.%(ext)s'),
        '--ignore-errors',
        '--retries', '5'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        
        if result.returncode == 0:
            print("DOWNLOAD SUCCESSFUL")
        else:
            print(f"DOWNLOAD FAILED: {result.stderr}")
            
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    simple_download()
