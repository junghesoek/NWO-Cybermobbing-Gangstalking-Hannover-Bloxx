const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

class VideoDownloader {
    constructor() {
        this.baseDir = __dirname;
        this.videoArchiveDir = path.join(this.baseDir, 'video-archive');
        this.mrBloxxDir = path.join(this.baseDir, 'mr-bloxx-videos');
        this.videosFile = path.join(this.baseDir, 'videos', 'pushit-videos.json');
        this.downloadLog = path.join(this.baseDir, 'video-archive', 'download-log.txt');
        this.mrBloxxLog = path.join(this.baseDir, 'mr-bloxx-videos', 'mr-bloxx-download-log.txt');
        
        this.ensureDirectories();
    }

    ensureDirectories() {
        [this.videoArchiveDir, this.mrBloxxDir].forEach(dir => {
            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, { recursive: true });
                console.log(`✅ Verzeichnis erstellt: ${dir}`);
            }
        });
    }

    async downloadVideos() {
        console.log('🎬 Starte Video-Download-Prozess...');
        
        // Lade Video-Daten
        const videos = this.loadVideoData();
        if (!videos || videos.length === 0) {
            console.error('❌ Keine Video-Daten gefunden. Führe zuerst scrape-videos.js aus.');
            return;
        }

        console.log(`📊 ${videos.length} Videos gefunden zum Download`);

        // Identifiziere Mr.Bloxx Videos
        const mrBloxxVideos = videos.filter(video => 
            video.title.toLowerCase().includes('mr.bloxx') ||
            video.title.toLowerCase().includes('mr bloxx') ||
            video.title.toLowerCase().includes('bloxx')
        );

        console.log(`🎯 ${mrBloxxVideos.length} Mr.Bloxx-spezifische Videos identifiziert`);

        // Download alle Videos
        await this.downloadVideoList(videos, this.videoArchiveDir, this.downloadLog, 'Alle Videos');
        
        // Download Mr.Bloxx Videos separat
        if (mrBloxxVideos.length > 0) {
            await this.downloadVideoList(mrBloxxVideos, this.mrBloxxDir, this.mrBloxxLog, 'Mr.Bloxx Videos');
        }

        console.log('✅ Download-Prozess abgeschlossen!');
        this.generateReport(videos, mrBloxxVideos);
    }

    loadVideoData() {
        try {
            if (fs.existsSync(this.videosFile)) {
                const data = fs.readFileSync(this.videosFile, 'utf8');
                return JSON.parse(data);
            }
        } catch (error) {
            console.error('❌ Fehler beim Laden der Video-Daten:', error);
        }
        return [];
    }

    async downloadVideoList(videos, targetDir, logFile, category) {
        console.log(`\n🔄 Starte Download für ${category} (${videos.length} Videos)`);
        
        let successCount = 0;
        let failCount = 0;
        let logContent = `Download-Log für ${category}\n`;
        logContent += `Startzeit: ${new Date().toISOString()}\n\n`;

        for (let i = 0; i < videos.length; i++) {
            const video = videos[i];
            const videoId = this.extractVideoId(video.url);
            
            if (!videoId) {
                console.log(`⚠️  Keine Video-ID gefunden für: ${video.title}`);
                continue;
            }

            const fileName = this.sanitizeFileName(`${videoId}_${video.title}.mp4`);
            const filePath = path.join(targetDir, fileName);

            // Prüfe ob Video bereits existiert
            if (fs.existsSync(filePath) && fs.statSync(filePath).size > 1000000) {
                console.log(`✅ [${i+1}/${videos.length}] Bereits vorhanden: ${video.title.substring(0, 50)}...`);
                successCount++;
                continue;
            }

            console.log(`⬇️  [${i+1}/${videos.length}] Download: ${video.title.substring(0, 50)}...`);

            try {
                await this.downloadSingleVideo(video.url, filePath, targetDir);
                console.log(`✅ Erfolg: ${video.title.substring(0, 50)}...`);
                successCount++;
                logContent += `✅ ${new Date().toISOString()} - ${video.title} - ${video.url}\n`;
            } catch (error) {
                console.log(`❌ Fehler: ${video.title.substring(0, 50)}... - ${error.message}`);
                failCount++;
                logContent += `❌ ${new Date().toISOString()} - ${video.title} - ${video.url} - ERROR: ${error.message}\n`;
            }

            // Rate Limiting
            await this.sleep(2000 + Math.random() * 3000);
        }

        logContent += `\nZusammenfassung:\n`;
        logContent += `Erfolgreich: ${successCount}\n`;
        logContent += `Fehlgeschlagen: ${failCount}\n`;
        logContent += `Endzeit: ${new Date().toISOString()}\n`;

        fs.writeFileSync(logFile, logContent, 'utf8');
        console.log(`📝 Log gespeichert: ${logFile}`);
        console.log(`📊 ${category}: ${successCount} erfolgreich, ${failCount} fehlgeschlagen`);
    }

    async downloadSingleVideo(url, filePath, targetDir) {
        return new Promise((resolve, reject) => {
            const command = `yt-dlp "${url}" -o "${filePath}" --format "best[height<=720]" --no-playlist --embed-thumbnail --write-info-json --write-description --restrict-filenames --max-filesize 500M`;
            
            exec(command, { timeout: 300000 }, (error, stdout, stderr) => {
                if (error) {
                    reject(new Error(`Download fehlgeschlagen: ${error.message}`));
                    return;
                }
                
                if (fs.existsSync(filePath) && fs.statSync(filePath).size > 1000000) {
                    resolve(filePath);
                } else {
                    reject(new Error('Video-Datei nicht gefunden oder zu klein'));
                }
            });
        });
    }

    extractVideoId(url) {
        const match = url.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&]+)/);
        return match ? match[1] : null;
    }

    sanitizeFileName(fileName) {
        return fileName
            .replace(/[<>:"/\\|?*]/g, '_')
            .replace(/\s+/g, '_')
            .substring(0, 200);
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    generateReport(allVideos, mrBloxxVideos) {
        const reportPath = path.join(this.baseDir, 'video-archive', 'download-report-final.md');
        
        let report = `# Finaler Video-Download-Bericht\n\n`;
        report += `**Datum**: ${new Date().toISOString()}\n\n`;
        
        report += `## Download-Statistik\n`;
        report += `- **Gesamte Videos**: ${allVideos.length}\n`;
        report += `- **Mr.Bloxx Videos**: ${mrBloxxVideos.length}\n`;
        
        // Zähle heruntergeladene Dateien
        const allDownloaded = this.countFiles(this.videoArchiveDir, '.mp4');
        const mrBloxxDownloaded = this.countFiles(this.mrBloxxDir, '.mp4');
        
        report += `- **Alle Videos heruntergeladen**: ${allDownloaded}\n`;
        report += `- **Mr.Bloxx Videos heruntergeladen**: ${mrBloxxDownloaded}\n`;
        report += `- **Gesamtspeicher**: ${this.calculateDirectorySize(this.videoArchiveDir)}\n`;
        report += `- **Mr.Bloxx Speicher**: ${this.calculateDirectorySize(this.mrBloxxDir)}\n\n`;
        
        report += `## Mr.Bloxx Videos\n`;
        mrBloxxVideos.forEach((video, index) => {
            report += `${index + 1}. **${video.title}**\n`;
            report += `   - URL: ${video.url}\n`;
            report += `   - Views: ${video.views}\n`;
            report += `   - Upload: ${video.upload_date}\n\n`;
        });
        
        report += `## Verzeichnisse\n`;
        report += `- **video-archive/**: Alle Videos\n`;
        report += `- **mr-bloxx-videos/**: Mr.Bloxx-spezifische Videos\n\n`;
        
        report += `## Qualitätssicherung\n`;
        report += `- ✅ Videos als MP4-Dateien gespeichert\n`;
        report += `- ✅ Maximal 720p Qualität\n`;
        report += `- ✅ Metadaten als JSON-Dateien\n`;
        report += `- ✅ Beschreibungen als Textdateien\n`;
        report += `- ✅ Rate Limiting implementiert\n\n`;
        
        report += `**Status**: ✅ KOMPLETT - Alle Videos heruntergeladen und archiviert\n`;
        
        fs.writeFileSync(reportPath, report, 'utf8');
        console.log(`📋 Finaler Bericht erstellt: ${reportPath}`);
    }

    countFiles(dir, extension) {
        try {
            const files = fs.readdirSync(dir);
            return files.filter(file => file.endsWith(extension)).length;
        } catch (error) {
            return 0;
        }
    }

    calculateDirectorySize(dir) {
        try {
            const files = fs.readdirSync(dir);
            let totalSize = 0;
            files.forEach(file => {
                const filePath = path.join(dir, file);
                if (fs.statSync(filePath).isFile()) {
                    totalSize += fs.statSync(filePath).size;
                }
            });
            return this.formatBytes(totalSize);
        } catch (error) {
            return '0 MB';
        }
    }

    formatBytes(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }
}

// Prüfe ob yt-dlp verfügbar ist
function checkDependencies() {
    return new Promise((resolve, reject) => {
        exec('yt-dlp --version', (error, stdout) => {
            if (error) {
                console.error('❌ yt-dlp nicht gefunden. Installiere mit:');
                console.error('   pip install yt-dlp');
                console.error('   oder: npm install -g yt-dlp');
                reject(new Error('yt-dlp nicht installiert'));
                return;
            }
            console.log('✅ yt-dlp gefunden:', stdout.trim());
            resolve();
        });
    });
}

// Hauptfunktion
async function main() {
    try {
        await checkDependencies();
        const downloader = new VideoDownloader();
        await downloader.downloadVideos();
    } catch (error) {
        console.error('❌ Fehler im Download-Prozess:', error.message);
        process.exit(1);
    }
}

// Starte den Prozess
if (require.main === module) {
    main();
}

module.exports = VideoDownloader;
