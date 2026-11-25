"""Small shared helpers used by the Selenium-based company scrapers."""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def fetch_soup(url: str) -> BeautifulSoup:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1440,1200")
    driver = webdriver.Chrome(options=options)
    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
        return BeautifulSoup(driver.page_source, "lxml")
    finally:
        driver.quit()
