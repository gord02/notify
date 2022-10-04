from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from wordScan import wordScan

def get_data():  
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
    url = "https://addepar.com/careers#engineering"
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()

    # jobs contains the jobs I am interested, intern roles
    jobs = []
    titles = soup.select("p.f4")
    for title in titles:
        job_name = title.contents[0]
        if wordScan(job_name):
            jobs.append(job_name)
    return jobs