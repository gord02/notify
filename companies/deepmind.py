from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

import sys
sys.path.insert(0,'..') #this works relative to where to program was run from 

from logic import process
from logic import notify
from logic import sqlQueries

def get_data():
    company = "Deepmind"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    jobs = []
    
    success = True
    
    url = "https://www.deepmind.com/careers/jobs?teams=Engineering&sort=newest_first"
    
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()
        elements = soup.select("tr.jobs-table-row td")
        for element in elements:
            if len(element.contents) > 0:
                jobs.append(element.contents[0])

        jobs = process.process_job_titles(jobs)

    
    except Exception as e:
        # send email about scrapping error
        error=f"Exception parsing {company} "+ repr(e)
        print(error)
        notify.parsing_error(error)
        success = False
        
    if len(jobs) > 0:
        # update company in database to found
        sqlQueries.update_company(company)
        
    jobs.insert(1, url)
   return(jobs, success)
# get_data()