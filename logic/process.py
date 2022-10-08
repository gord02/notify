
def process_job_titles(titles):
    swe_intern_job = []
    for title in titles:
        job_name = title.contents[0]
        if wordScan(job_name):
            swe_intern_job.append(job_name)

def wordScan(title):
    if "Intern" in title and "Engineer" in title:
        return True

