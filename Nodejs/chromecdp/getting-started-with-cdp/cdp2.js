//DEBUG=* node cdp2.js 

const puppeteer = require('puppeteer');

(async() => {
  // Use Puppeteer to launch a browser and open a page.
  const browser = await puppeteer.launch({
      headless: false
      // userDataDir: "/home/w/.config/chromium/"
    });
  const page = await browser.newPage();

  // Create a raw DevTools protocol session to talk to the page.
  // Use CDP to set the animation playback rate.
  const session = await page.target().createCDPSession();
  await session.send('Animation.enable');
  await session.send('DOM.enable');
  
  session.on('Animation.animationCreated', () => {
    console.log('Animation created!');
  });
  session.on('DOM.shadowRootPushed', () => {
    console.log('DOM.shadowRootPushed');
  });
  session.on('DOM.shadowRootPopped', () => {
    console.log('DOM.shadowRootPopped');
  });

  await session.send('Animation.setPlaybackRate', {
    playbackRate: 2,
  });


  // Check it out! Fast animations on the "loading..." screen!
  // await page.goto('https://pptr.dev');
  await page.goto('https://www.google.com');
  // await page.goto(url, {waitUntil: "networkidle2"});
  await page.evaluate(() => {
    // this will be executed within the page, that was loaded before
    document.body.style.background = '#000';
  });
 
  await page.waitForXPath('//*[@id="SIvCob"]');
  //assuming it's the first element
  let [element] = await page.$x('//*[@id="SIvCob"]');
  let text = await page.evaluate(element => element.textContent, element);
  

  
  // await page.goto('https://www.amazon.com')
  // await page.type('#twotabsearchtextbox', 'nyan cat pullover')
  // await page.click('input.nav-input')
  // // await page.waitForSelector('#resultsCol')
  // await page.screenshot({ path: 'amazon_nyan_cat_pullovers_list.png' })
  // await page.click('#pagnNextString')
  // await page.waitForSelector('#resultsCol')
  // const pullovers = await page.$$('a.a-link-normal.a-text-normal')
  // await pullovers[2].click()
  // await page.waitForSelector('#ppd')
  // await page.screenshot({ path: screenshot })
  await browser.close()
    


  await wait(15000)
  console.log("Done")
})();

async function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}