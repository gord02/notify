from logic.process import process_job_titles
from logic.scrape import fetch_soup


COMPANY_NAME = "Snap"
URL = "https://www.snap.com/en-US/jobs?lang=en-US"


def get_data():
    soup = fetch_soup(URL)
    return process_job_titles(soup.select("th a"), URL)
