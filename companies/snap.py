from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

import sys
# allows for getting files up a level when trying to run this file directly
sys.path.insert(0,'..')
from logic import process

def get_data():   
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    url = "https://www.snap.com/en-US/jobs?lang=en-US"
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()

    titles = set()
    elements = soup.select("th a")
    for element in elements:
        titles.add(element.contents[0])
    # for title in titles:
    #     print(title)
    jobs = process.process_job_titles(titles)
    if len(jobs) > 0:
        # update company in database to found
        pass
        
        
get_data()