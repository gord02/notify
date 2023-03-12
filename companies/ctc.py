from bs4 import BeautifulSoup
from selenium import webdriver
# from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import sys
import time
sys.path.insert(0,'..') #this works relative to where to program was run from 

from logic import process
from logic import notify
from logic import sqlQueries

def get_data(): 
    company =  "Chicago Trading Company"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    jobs = []

    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
        url = "https://www.chicagotrading.com/search"
        driver.get(url)
        
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()
        elements = soup.select("div.title > h3")
        # locations = soup.select("div.job-meta > span")
 
        for element in elements:
            # print(element)
            jobs.append(element.contents[0])
            
        jobs = process.process_job_titles(jobs)
        if len(jobs) > 0:
            # update company in database to found
            sqlQueries.update_company(company)
        return jobs
        
    except Exception as e:
        # send email about scrapping error
        error=f"Exception parsing {company} "+ repr(e)
        print(error)
        notify.parsing_error(error)
        return jobs
        
# get_data()