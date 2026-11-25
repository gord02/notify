from logic.process import process_job_titles
from logic.scrape import fetch_soup


COMPANY_NAME = "Google DeepMind"
URL = "https://www.deepmind.com/careers/jobs?teams=Engineering&sort=newest_first"


def get_data():
    soup = fetch_soup(URL)
    return process_job_titles(soup.select("tr.jobs-table-row a, a"), URL)
