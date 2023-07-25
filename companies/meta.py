from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.common.exceptions import WebDriverException

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
    success = True
    
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
            print(x.contents[0])
            jobs.append(x.contents[0])

    
            # this is an exception caused by abnormal circumstances
    except WebDriverException as wbe:
        error=f"Exception parsing {company} "+ repr(wbe)
        # print(error)
        print("An exception occurred:", type(wbe).__name__) # An exception occurred: ZeroDivisionError
        # send email about scrapping error
        notify.parsing_error(error)
        
    # this is most likely an error caused by computer not being fully awake when code is run leading to max retry or ConnectionError error
    except ConnectionError as e:
        print("An exception occurred:", type(e).__name__) # An exception occurred: ZeroDivisionError
        # print("e: ", repr(e))
        # we want to retry when computer is fully awake
        success = False
        
    jobs = process.process_job_titles(jobs)
    
    if len(jobs) > 0:
        # update company in database to found
        sqlQueries.update_company(company)
    
    jobs.insert(0, url)
    return(jobs, success)

# get_data()

