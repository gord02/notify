from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

import undetected_chromedriver as uc

# options = webdriver.ChromeOptions() 
# driver.get('https://bet365.com')

opts = Options()
# so that browser instance doesn't pop up
opts.add_argument("--headless")
opts.add_argument("start-maximized")

driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
url = "https://www.coinbase.com/careers/positions?department=Engineering"
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, "lxml")
driver.quit()
jobs = set()
print(soup)
elements = soup.select("div.kOaGIY")
for element in elements:
    print(element)
    # jobs.add(element.contents)

for title in jobs:
    print(title)