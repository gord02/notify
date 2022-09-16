import requests 
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# opts = Options()
# opts.add_argument(‘ — headless’)
# opts.add_argument(" — headless")
opts = Options()
opts.add_argument('--disable-blink-features=AutomationControlled')
serviceObj = Service("/Users/gordon/Downloads/chromedriver")
# driver = webdriver.Chrome("/Users/gordon/Downloads/chromedriver")
driver = webdriver.Chrome(service=serviceObj,  options = opts)
# driver = webdriver.Chrome("/Users/gordon/Downloads/chromedriver", options=opts)

url = "https://www.quora.com/careers/engineering"
# url = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq"

# url = "https://www.adamchoi.co.uk/teamgoals/detailed"
# url = "https://pynishant.github.io/", execute javascript works with this link
 

# url = "https://groceries.asda.com/search/yoghurt"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "lxml")

# driver = webdriver.Chrome(‘chromedriver’, options=opts)

driver.implicitly_wait(7)

driver.get(url)
driver.implicitly_wait(7)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")
pageSource = driver.execute_script("return document.body.innerHTML;")
content = driver.page_source
# time.sleep(10) # Let the user actually see something!

# soup = BeautifulSoup(content, "lxml")
soup = BeautifulSoup(pageSource , "lxml")
print(soup)
# print(pageSource)

driver.quit() 


