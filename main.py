"""Run each company scraper independently and build the public results page."""

from __future__ import annotations

import importlib
import logging
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


ROOT = Path(__file__).resolve().parent
COMPANIES_DIR = ROOT / "companies"
OUTPUT_FILE = ROOT / "site" / "index.html"

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def collect_company_results() -> list[dict]:
    """Run every company scraper; an import or scrape failure only skips that company."""
    results = []
    for path in sorted(COMPANIES_DIR.glob("*.py")):
        name = path.stem
        if name.startswith("_"):
            continue

        try:
            module = importlib.import_module(f"companies.{name}")
            scrape = getattr(module, "get_data", None)
            if not callable(scrape):
                logger.info("Skipping %s: no get_data() scraper", name)
                continue
            jobs = scrape()
            if not jobs:
                logger.info("No matching listings for %s", name)
                continue
            results.append({"name": getattr(module, "COMPANY_NAME", name), "jobs": jobs})
            logger.info("Collected %d listing(s) for %s", len(jobs), name)
        except Exception:
            # Keep diagnostics in the Actions log, but never put errors on the public page.
            logger.exception("Scraper failed for %s; omitting its results", name)

    return results


def render_page(results: list[dict], updated_at: datetime) -> None:
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("webpage.html")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        template.render(companies=results, updated_at=updated_at),
        encoding="utf-8",
    )


def main() -> None:
    results = collect_company_results()
    render_page(results, datetime.now(timezone.utc))
    logger.info("Wrote %s with %d company section(s)", OUTPUT_FILE, len(results))


if __name__ == "__main__":
    main()
