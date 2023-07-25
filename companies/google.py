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
    company =  "Google"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    jobs = []
    url = "https://careers.google.com/jobs/results/?degree=BACHELORS&distance=50&employment_type=INTERN&jex=ENTRY_LEVEL&location=United%20States&location=Canada"
    # url ="https://www.google.com/about/careers/applications/jobs/results/?distance=50&location=United%20States&location=Canada&degree=BACHELORS"
    success = True
    
    try:
        i = 1
        # 1000 is an arbitrary number of pages that Google might have for jobs in the worst case we would have to go through
        while i<= 1000:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
            newUrl = url + "&page=" + str(i)
            driver.get(newUrl)
            content = driver.page_source
            soup = BeautifulSoup(content, "lxml")
            
            # this is a check to make sure there are still jobs left in current tab
            shownPages = soup.find('div', jsname = "uEp2ad")

            if(shownPages is None):
                # print("finished all pages at i equal to : ", i-1)
                break
            
            elements = soup.select("div h3")
            # print(elements)
            for element in elements:
                jobs.append(element.contents[0])
                # print(element.contents[0])
            i+=1   
            # print("===========")
            
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
        print("error e is: ", repr(e))
        # we want to retry when computer is fully awake
        success = False
        
        
    jobs = process.process_job_titles(jobs)
    
    if len(jobs) > 0:
        # update company in database to found
        sqlQueries.update_company(company)
    
    jobs.insert(0, url)
    return (jobs, success)    

# get_data()


            # newUrl = "https://careers.google.com/jobs/results/?degree=BACHELORS&distance=50&employment_type=INTERN&jex=ENTRY_LEVEL&location=United%20States&location=Canada" + pageNum + str(i)


# google updated code, below is no longer applicable
       # getting the number of job pages to search over 
        # pagesRange = soup.select("div.gc-p-results__pagination p")
        # print("here 2")
        # print(pagesRange)
        # res = str(pagesRange[0].contents[0])
        # print("here 3")
        # print("res: ", res)
        
        # x = res.split()
        # range = []
        # for n in x:
        #     if(n.isnumeric()):
        #         range.append(int(n))
                
        # pageNum = "&page="
        # i = range[0]
        # print(range[0], range[1])