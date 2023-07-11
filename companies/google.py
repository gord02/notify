from bs4 import BeautifulSoup
from selenium import webdriver
# from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

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
    success = True
    

    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)

        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        print(soup)
        
        driver.quit()
        
        # getting the number of job pages to search over 
        pagesRange = soup.select("div.gc-p-results__pagination p")
    
        res = str(pagesRange[0].contents[0])
        x = res.split()
        range = []
        for n in x:
            if(n.isnumeric()):
                range.append(int(n))
                
        pageNum = "&page="
        i = range[0]
        # print(range[0], range[1])
        
        # false negative of no reuslts 
        while i<= range[1]:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
            newUrl = "https://careers.google.com/jobs/results/?degree=BACHELORS&distance=50&employment_type=INTERN&jex=ENTRY_LEVEL&location=United%20States&location=Canada" + pageNum + str(i)
            driver.get(newUrl)
            content = driver.page_source
            soup = BeautifulSoup(content, "lxml")
            print(soup)
            elements = soup.select("div h2")
            print(elements)
            for element in elements:
                # jobs.append(element.contents[0])
                print(element.contents[0])
            i+=1   
            

    except Exception as e:
        # send email about scrapping error
        error=f"Exception parsing {company} "+ repr(e)
        print(error)
        exc_type, exc_tb = sys.exc_info()
        print("exception type: ", exc_type, " excpetion line number", exc_tb )
        # notify.parsing_error(error)
        success = False
        
        
    jobs = process.process_job_titles(jobs)
    
    if len(jobs) > 0:
        # update company in database to found
        sqlQueries.update_company(company)
    
    jobs.insert(1, url)
    return (jobs, success)    

# get_data()