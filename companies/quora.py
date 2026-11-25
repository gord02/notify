from logic.process import process_job_titles
from logic.scrape import fetch_soup


COMPANY_NAME = "Quora"
URL = "https://www.quora.com/careers/engineering"


def get_data():
    soup = fetch_soup(URL)
    return process_job_titles(soup.select("td div, a"), URL)
