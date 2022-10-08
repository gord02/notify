from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from logic import process

opts = Options()
# so that browser instance doesn't pop up
opts.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = opts)
url = "https://www.deepmind.com/careers/jobs?teams=Engineering&sort=newest_first"
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, "lxml")
driver.quit()
titles = set()
elements = soup.select("tr.jobs-table-row")
for element in elements:
    jobs.add(element.contents[0].contents[0])

jobs = process.process_job_titles(titles)
if len(jobs) > 0:
    # update company in database to found
    pass