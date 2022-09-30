from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

opts = Options()
# so that browser instance doesn't pop up
opts.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
url = "https://www.redditinc.com/careers/#job-info"
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, "lxml")
driver.quit()
jobs = set()
elements = soup.select("div.job a div.job-title")
for element in elements:
    jobs.add(elements[0].contents[0])

for title in jobs:
    print(title)