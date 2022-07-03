# Import required libraries
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Selenium local webdriver configurations
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'normal'
chrome_options.add_argument("--start-maximized")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open card page
driver.get("https://buschland.eu/A/ABC_Seeds/Chunk_44/ABC_Seeds__Chunk_44.html")

# Stop card motion
driver.execute_script("turnOffHoloCard();")

# Add some delay
sleep(3)

# Increase the card size
driver.execute_script("document.getElementsByTagName('html')[0].style.zoom=1.5")

# Add some delay
sleep(3)

# Magic spell to open next card
driver.execute_script("""
function nextCard(){
    var array = cards;
    let direction = 1;
    let rotationY = '+=180';

    turnOffHoloCard();

    TweenMax.to(array[currentVisible], 2, {css:{rotationY:rotationY}, ease:Power2.easeInOut});
    TweenMax.to(array[currentVisible], 1, {css:{z:"-=190"}, yoyo:true, repeat:1, ease:Power2.easeIn});

    currentVisible = (cards.length + currentVisible + direction) % cards.length;

    TweenMax.to(array[currentVisible], 2, {css:{rotationY:rotationY}, ease:Power2.easeInOut});
    TweenMax.to(array[currentVisible], 1, {css:{z:"-=190"}, yoyo:true, repeat:1, ease:Power2.easeIn});
}

function sleep(s) {
  return new Promise(resolve => setTimeout(resolve, s*1000));
}

await (sleep(3)); nextCard(); await (sleep(3)); nextCard(); await (sleep(3)); nextCard(); await (sleep(3)); nextCard(); await (sleep(3)); nextCard(); await (sleep(3)); nextCard();

""")

# Following line of code is used to move to the next card with 3 seconds delay. 
  # await (sleep(3)); nextCard();

# It's added six times in line number 47 to move to the next card.
# Add it to the line 47 the number of times you want to move to the next card. 

# Add some delay
sleep(10)

# Finally close
driver.quit()