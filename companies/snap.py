from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

import sys
# allows for getting files up a level when trying to run this file directly
sys.path.insert(0,'..')
from logic import process
from logic import sqlQueries
from logic import notify

def get_data():   
    company = "Snap"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")

    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
        url = "https://www.snap.com/en-US/jobs?lang=en-US"
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()

        titles = set()
        elements = soup.select("th a")
        for element in elements:
            titles.add(element.contents[0])
        # for title in titles:
        #     print(title)
        jobs = process.process_job_titles(titles)
        if len(jobs) > 0:
            # update company in database to found
            # update company in database to found
            sqlQueries.update_company(company)
            
        return jobs

    except Exception as e:
        # send email about scrapping error
        error=f"Exception parsing {company} "+ e
        print(error)
        notify.parsing_error(error)
        return jobs
    
# get_data()