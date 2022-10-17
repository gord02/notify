from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

import time
import sys
# allows for getting files up a level when trying to run this file directly
sys.path.insert(0,'..')

from logic import process

def get_data():  
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")

    start_time = time.time()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    url = "https://careers.twosigma.com/careers/SearchJobs/Intern?2047=%5B9813555%5D&2047_format=1532&listFilterMode=1"
    
    try:
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()

        print(soup)
        # firstLink = soup.select_one("a.paginationLink").get("href")
        firstLink = soup.select_one("a.paginationLink")
    
        # return
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
            print("p: ", curLink)
            driver.get(curLink)
            content = driver.page_source
            soup = BeautifulSoup(content, "lxml")
            driver.quit()
            
            elements = soup.select("a.mobileShow")    

            for element in elements:
                titles.add(element.contents[0])
            
            paginationLinks = soup.select("a.paginationLink")
            
            for link in paginationLinks:
                urlLink = link.get("href")
                
                if urlLink not in urlSet:
                    q.insert(0, urlLink)
                    urlSet.add(curLink)
        
        
        print("first link: ", firstLink)
        print("minutes: ", (time.time() - start_time)/60)
                
        # print("found jobs: ", len(jobs))
        # for job in jobs:
        #     print(job)
            
        jobs = process.process_job_titles(titles)
        if len(jobs) > 0:
            # update company in database to found
            pass
        
        return jobs
    except:
        return jobs
        
get_data()