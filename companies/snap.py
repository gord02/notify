from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from wordScan import wordScan

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

    jobs = []
    titles = soup.select("th a")
    
    # abstract below logic !!!
    for title in titles:
        job_name = title.contents[0]
        if wordScan(job_name):
            
            # update company in database to found
            
            
            jobs.append(job_name)
        # print(title['href'])
    # for job in jobs:
    #     print(job)
        
get_data()