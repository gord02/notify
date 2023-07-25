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

def get_data():
    company = "Jump Trading"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)

    url = "https://www.jumptrading.com/careers/?locations=Chicago+New-York&titleSearch=campus+intern"
    jobs = []
    success = True
    

    try:
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()
        elements = soup.select("a > div > div > p")

        # for i, element in enumerate(elements):
        i=0
        # each p tag is the job name and the following p tag is the location 
        while i+1 < len(elements):
            jobs.append(elements[i].contents[0] + ": " + elements[i+1].contents[0])
            # skips to the next job title
            i = i + 2
    
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