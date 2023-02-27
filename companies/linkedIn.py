from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from logic import process
from logic import notify
from logic import sqlQueries

def get_data(): 
    # company =  "Jane Street"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    jobs = []

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    # try:
    url = "https://www.linkedin.com/jobs/search/?currentJobId=3363564898&f_C=1337%2C39939%2C2587638%2C9202023&geoId=92000000&originToLandingJobPostings=3489403427%2C3496919775%2C3448033554%2C3396273093%2C3480292950%2C3395173747%2C3476414384%2C3474361857%2C3479858849&start=25"
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("a span")

    # have to parse through all linkedin pages !
    for element in elements:
        print(element.contents[0].strip())
  
    
    jobs = process.process_job_titles(jobs)
    # if len(jobs) > 0:
    #     # update company in database to found
    #     sqlQueries.update_company(company)

#    except Exception as e:
#         # send email about scrapping error
#         error=f"Exception parsing {company} "+ e
#         print(error)
#         notify.parsing_error(error)
#         return jobs
    
    
get_data()