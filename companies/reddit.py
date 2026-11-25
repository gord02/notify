from logic.process import process_job_titles
from logic.scrape import fetch_soup


COMPANY_NAME = "Reddit"
URL = "https://www.redditinc.com/careers/#job-info"


def get_data():
    soup = fetch_soup(URL)
    return process_job_titles(soup.select("div.job a div.job-title, a"), URL)
