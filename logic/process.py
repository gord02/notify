"""Shared helpers for extracting and filtering job listings."""

from urllib.parse import urljoin


def wordScan(title: str) -> bool:
    """Keep the project's original focus on software engineering internships."""
    normalized = title.casefold()
    return "intern" in normalized and "engineer" in normalized


def listing_from_element(element, base_url: str) -> dict | None:
    """Convert a BeautifulSoup node into a title/link pair."""
    title = element.get_text(" ", strip=True)
    if not title:
        return None

    link = element if getattr(element, "name", None) == "a" else element.find_parent("a")
    if link is None:
        link = element.find("a")
    href = link.get("href") if link else None
    return {"title": title, "url": urljoin(base_url, href) if href else base_url}


def process_job_titles(titles, base_url: str = "") -> list[dict]:
    """Return unique qualifying listings, accepting strings or HTML elements."""
    jobs = []
    seen = set()
    for item in titles:
        if isinstance(item, str):
            title, url = item.strip(), base_url
        elif isinstance(item, dict):
            title, url = item.get("title", "").strip(), item.get("url") or base_url
        else:
            listing = listing_from_element(item, base_url)
            if listing is None:
                continue
            title, url = listing["title"], listing["url"]

        key = (title.casefold(), url)
        if title and key not in seen and wordScan(title):
            seen.add(key)
            jobs.append({"title": title, "url": url or base_url})
    return jobs
