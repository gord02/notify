from bs4 import BeautifulSoup
from selenium import webdriver
# from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from selenium.common.exceptions import WebDriverException

import sys
sys.path.insert(0,'..') #this works relative to where to program was run from 

from logic import process
from logic import notify
from logic import sqlQueries


def get_data(): 
    company =  "Uber"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    jobs = []
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    url = "https://www.uber.com/ca/en/careers/list/?department=University&team=University&team=Engineering"
    success = True

    try:
        # https://www.uber.com/ca/en/careers/list/?location=CAN-Ontario-Toronto&location=USA-Illinois-Chicago&location=USA-California-San%20Fransisco&location=USA-New%20York-New%20York%20City&department=University&team=University&team=Engineering
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()
        
        
        elements = soup.select("a.css-bNzNOn")
        # locations = soup.select("div > div > div > span.css-dCwqLp")
       
        for element in elements:
            jobs.append(element.contents[0])
        
        # for loc in locations:
        #     print(loc.contents[0])
        
    
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
    return (jobs, success)
    
# get_data()