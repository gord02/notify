from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from logic.process import process_job_titles


COMPANY_NAME = "Two Sigma"
URL = "https://careers.twosigma.com/careers/SearchJobs/Intern?2047=%5B9813555%5D&2047_format=1532&listFilterMode=1"


def get_data():
    session = requests.Session()
    queue = [URL]
    visited = set()
    listings = []

    while queue and len(visited) < 20:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        response = session.get(current, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        listings.extend(soup.select("a.mobileShow"))

        for link in soup.select("a.paginationLink[href]"):
            target = urljoin(current, link["href"])
            if target not in visited and target not in queue:
                queue.append(target)

    return process_job_titles(listings, URL)
