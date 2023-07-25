from bs4 import BeautifulSoup
from selenium import webdriver
# from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.common.exceptions import WebDriverException


import sys
sys.path.insert(0,'..') #this works relative to where to program was run from 

from logic import process
from logic import notify
from logic import sqlQueries

def get_data(): 
    company =  "Apple"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    # access will be blocked without this user agent
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36" 
    opts.add_argument("user-agent=%s" % user_agent) 

    jobs = []
    url = "https://jobs.apple.com/en-us/search?location=united-states-USA+canada-CANC&team=internships-STDNT-INTRN"
    success = True
    
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
        
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()

        # allows us to traverse pages 
        page = soup.find(id="page-number")
        page1 =  (int)(page['value'])
        pages = soup.select("span.pageNumber")
        endPage = (int)(pages[1].contents[0])
        pageNum = "&page="
        
        while page1 <= endPage:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
            newUrl = url + pageNum + str(page1)
            driver.get(newUrl)
            content = driver.page_source
            soup = BeautifulSoup(content, "lxml")
            elements = soup.select("a.table--advanced-search__title")
            for element in elements:
                jobs.append(element.contents[0])
            page1+=1   
                
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