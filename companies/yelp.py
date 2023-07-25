from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.common.exceptions import WebDriverException

from logic import process
from logic import notify
from logic import sqlQueries

import time

def get_data():  
    company = "Yelp"
    
    start_time = time.time()
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    opts.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    start = time.time()
    jobs = []
    
    url = "https://www.yelp.careers/us/en/search-results"
    success = True
    
    try:
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()

        titles = set()

        # Page has pagination
        usedLinks = set()
        q = []
        # skipping the prev button, there is hidden prev link that will be first in the list so skip to index 1
        firstLink = soup.select("ul.pagination li a")[1]['href']

        q.append(firstLink)
        while len(q) > 0:
            link = q.pop()
            usedLinks.add(link)
            # have to re-initialize new web driver for new calls
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
            driver.get(link)
            page = driver.page_source
            driver.quit()
            soup = BeautifulSoup(page, "lxml") 
            
            jobTitles =  soup.select("div.job-title span")
            for jobT in jobTitles:
                titles.add(jobT.contents[0])
            
            links = soup.select("ul.pagination li a")
            for newLink in links:
                urlLink =  newLink['href'] 
                if urlLink not in usedLinks and len(urlLink) > 0:
                        q.insert(0, urlLink) 
                        # prevents repeated addition of the same url to the q
                        usedLinks.add(urlLink)
                        
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
    
    # print("minutes: ", (time.time() - start_time)/60)
    if len(jobs) > 0:
        # update company in database to found
        sqlQueries.update_company(company)
    
    jobs.insert(0, url) 
    return(jobs, success)   
# get_data()