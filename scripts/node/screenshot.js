const puppeteer = require('puppeteer');

(async () => {
  const url = 'https://example.com'; // Replace with your URL
  const output = 'screenshot.png';

  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.setViewport({
    width: 1920,
    height: 1080, // Initial height; irrelevant when using fullPage
  });

  await page.goto(url, { waitUntil: 'networkidle2' });

  await page.screenshot({
    path: output,
    fullPage: true
  });

  await browser.close();
})();
