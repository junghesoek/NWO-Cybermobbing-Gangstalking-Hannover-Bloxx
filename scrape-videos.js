const puppeteer = require('puppeteer');

async function scrapeVideos() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  try {
    console.log('Navigating to channel videos sorted by oldest...');
    await page.goto('https://www.youtube.com/@PUSHITHTOWN/videos?view=0&sort=dd&shelf_id=0', { waitUntil: 'networkidle2' });
    
    console.log('Scrolling to load all videos...');
    let previousHeight;
    let currentHeight = await page.evaluate(() => document.body.scrollHeight);
    let scrollCount = 0;
    
    while (scrollCount < 200) {
      previousHeight = currentHeight;
      await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
      await page.waitForTimeout(3000);
      currentHeight = await page.evaluate(() => document.body.scrollHeight);
      scrollCount++;
      
      if (currentHeight === previousHeight && scrollCount > 10) {
        break;
      }
      
      console.log(`Scroll ${scrollCount}: ${currentHeight}px`);
    }
    
    console.log('Extracting video data...');
    const videos = await page.evaluate(() => {
      const videoData = [];
      const videoLinks = document.querySelectorAll('a[href*="/watch?v="]');
      
      videoLinks.forEach(link => {
        const url = link.href;
        if (url.includes('/watch?v=') && !videoData.some(v => v.url === url)) {
          const container = link.closest('ytd-rich-grid-media') || link.closest('#dismissible');
          const titleElement = container?.querySelector('h3 a, #video-title-link, yt-formatted-string');
          const metadata = container?.querySelectorAll('#metadata-line span');
          
          let title = '';
          let views = 'Unknown';
          let uploadDate = 'Unknown';
          
          if (titleElement) {
            title = titleElement.textContent?.trim() || '';
          }
          
          if (metadata && metadata.length >= 2) {
            views = metadata[0]?.textContent?.trim() || 'Unknown';
            uploadDate = metadata[metadata.length - 1]?.textContent?.trim() || 'Unknown';
          }
          
          if (title) {
            videoData.push({
              url: url,
              title: title,
              views: views,
              upload_date: uploadDate
            });
          }
        }
      });
      
      return videoData;
    });
    
    console.log(`Found ${videos.length} videos`);
    
    // Save to file
    const fs = require('fs');
    const path = require('path');
    const filePath = path.join(__dirname, 'videos', 'pushit-videos.json');
    fs.writeFileSync(filePath, JSON.stringify(videos, null, 2));
    console.log('Saved to videos/pushit-videos.json');
    
  } catch (error) {
    console.error('Error:', error);
  } finally {
    await browser.close();
  }
}

scrapeVideos();
