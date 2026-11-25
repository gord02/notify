# Internship openings

This project checks company career pages for software engineering internship listings and publishes the successful results as a static website.

## How it works

Each Python file in `companies/` with a `get_data()` function is treated as a company scraper. The workflow calls each scraper independently. A failed import or scrape is recorded in the GitHub Actions log and that company's results are omitted; other scrapers continue. The public page shows only successful matching results and does not display scraper errors.

The generated page includes the company, job title, link to the original listing, and time of the latest scan. Each successful deployment replaces the previous page with that run's results. No database or prior-result storage is used.

## Run locally

Requires Python 3.12, Google Chrome or Chromium, and network access to the company career sites.

```sh
python -m pip install -r requirements.txt
python main.py
```

The generated page is `site/index.html`. Selenium Manager locates or downloads a compatible browser driver when needed.

## Scheduled and manual runs

The GitHub Actions workflow runs daily at noon America/Toronto time. To run it immediately, open the repository's **Actions** tab, select **Scrape listings and publish page**, then choose **Run workflow**.

The workflow runs the scrapers, renders `site/index.html`, and deploys that directory to GitHub Pages. GitHub Pages must be enabled with **Settings → Pages → Build and deployment → Source: GitHub Actions**. After the first successful deployment, the page is available at `https://gord02.github.io/notify/`.

## Adding a company scraper

Add a Python module under `companies/` and implement `get_data()`. Return a list of dictionaries with `title` and `url` fields. Use `logic.process.process_job_titles()` to keep the existing software-engineering-internship filter and normalize the results. The runner discovers modules automatically; no separate company list is required.
