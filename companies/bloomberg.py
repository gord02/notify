from logic.process import process_job_titles
from logic.scrape import fetch_soup


COMPANY_NAME = "Bloomberg"
URL = "https://careers.bloomberg.com/job/search?el=Internships"


def get_data():
    soup = fetch_soup(URL)
    return process_job_titles(soup.select("div.kOaGIY a, a"), URL)
