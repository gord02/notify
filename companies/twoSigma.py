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

def get_data():  
    company =  "twoSigma"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")

    start_time = time.time()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    url = "https://careers.twosigma.com/careers/SearchJobs/Intern?2047=%5B9813555%5D&2047_format=1532&listFilterMode=1"
    jobs = []
    try:
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()

        page = soup.select_one("a.paginationLink")
        # print("first linK attrs: ", firstLink.attrs)
        firstLink= page.attrs['href']

        # set for urls and jobs
        urlSet = set()
        titles = set()

        # Create queue to store urls
        q = []

        if(firstLink):
            q.append(firstLink)
            
            
        # For each page, first push current to set, get all links for other pages, and if not in set, push to queue
        while len(q) > 0:
            curLink = q.pop()
            urlSet.add(curLink)
            
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)

            driver.get(curLink)
            content = driver.page_source
            soup = BeautifulSoup(content, "lxml")
            driver.quit()
            
            elements = soup.select("a.mobileShow")    
            # print("elements: ", elements)

            for element in elements:
                titles.add(element.contents[0])
            
            paginationLinks = soup.select("a.paginationLink")
            # print("paginationLinks: ", paginationLinks)
            
            for link in paginationLinks:
                urlLink = link.get("href")
                
                if urlLink not in urlSet:
                    q.insert(0, urlLink)
                    urlSet.add(curLink)
        
        
        # print("titles: ", titles)
        jobs = process.process_job_titles(titles)

        if len(jobs) > 0:
            # update company in database to found
            sqlQueries.update_company(company)
            pass

        return jobs
    except Exception as e:
        # send email about scrapping error
        print("error: ", e)
        # notify.parsing_error(company)
        return jobs
        
# get_data()

