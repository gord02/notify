from urllib.parse import urljoin

from logic.process import process_job_titles
from logic.scrape import fetch_soup


COMPANY_NAME = "Yelp"
URL = "https://www.yelp.careers/us/en/search-results"


def get_data():
    queue = [URL]
    visited = set()
    listings = []

    while queue and len(visited) < 20:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        soup = fetch_soup(current)
        listings.extend(soup.select("div.job-title span, a.job-title"))
        for link in soup.select("ul.pagination li a[href]"):
            target = urljoin(current, link["href"])
            if target not in visited and target not in queue:
                queue.append(target)

    return process_job_titles(listings, URL)
