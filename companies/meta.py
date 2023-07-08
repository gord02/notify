from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

import time
import sys
# allows for getting files up a level when trying to run this file directly
sys.path.insert(0,'..') #this works relative to where to program was run from 

from logic import process
from logic import notify
from logic import sqlQueries

from selenium import webdriver

def get_data():  
    company =  "Meta"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")

    start_time = time.time()

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    url = "https://www.metacareers.com/jobs?leadership_levels[0]=Individual%20Contributor&teams[0]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design"
    jobs = []      
    
    try:
        
        # does not work for multiple pages results
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        # print(soup)
        driver.quit()
        
        elements = soup.select("div._8sel")
        # elements = soup.select("div._8se1 _97f")
        # pages= soup.find("div",  {"class": ["_8se1", "_97f"]})
        # pageText = pages.contents[0]
        # bounds = pageText.split()
        # start = bounds[3]
        # end = bounds[5]
        # page = 1
   
        for x in elements:
            # print(x.contents[0])
            jobs.append(x.contents[0])

    
    except Exception as e:
        # send email about scrapping error
        error=f"Exception parsing {company} "+ repr(e)
        print(error)
        notify.parsing_error(error)
        
    jobs = process.process_job_titles(jobs)
    
    if len(jobs) > 0:
        # update company in database to found
        sqlQueries.update_company(company)
    return jobs
        
# get_data()

