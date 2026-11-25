from logic.process import process_job_titles
from logic.scrape import fetch_soup


COMPANY_NAME = "Coinbase"
URL = "https://www.coinbase.com/careers/positions?department=Engineering"


def get_data():
    soup = fetch_soup(URL)
    return process_job_titles(soup.select("div.kOaGIY a, a"), URL)
