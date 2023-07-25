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
    company =  "LinkedIn"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    jobs = []
    success = True
    
    
    url = "https://www.linkedin.com/jobs/search/?currentJobId=3502921259&f_C=1337&f_TPR=r86400&geoId=92000000"
    

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    try:
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()
        
        # Not reliable scrap since we cannot navigate through linkedin page results but the filters for above 
        # link(posted in last 24 hours) will help keep results limited to one page
        elements = soup.select("a span")
        
        for element in elements:
            jobs.append(element.contents[0].strip())
            # print(element.contents[0].strip())
    
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