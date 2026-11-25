from logic.process import process_job_titles
from logic.scrape import fetch_soup


COMPANY_NAME = "Addepar"
URL = "https://addepar.com/careers#engineering"


def get_data():
    soup = fetch_soup(URL)
    return process_job_titles(soup.select("p.f4, a"), URL)
