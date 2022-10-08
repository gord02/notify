import requests 
from logic import process
from bs4 import BeautifulSoup

def get_data():  
    url = "https://careers.twosigma.com/careers/SearchJobs/Intern?2047=%5B9813555%5D&2047_format=1532&listFilterMode=1"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    firstLink = soup.select_one("a.paginationLink").get("href")

    # set for urls and jobs
    urlSet = set()
    titles = set()

    # Create queue to store urls
    q = []

    if(firstLink):
        q.append(firstLink)
        
    # For each page, first push current to set, get all links for other pages, and if not in set, push to queue
    while len(q) > 0:
        curLink = q.pop()
        urlSet.add(curLink)
        
        response = requests.get(curLink)
        soup = BeautifulSoup(response.text, "lxml")
        
        elements = soup.select("a.mobileShow")    

        for element in elements:
            titles.add(element.contents[0])
        
        paginationLinks = soup.select("a.paginationLink")
        
        for link in paginationLinks:
            urlLink = link.get("href")
            
            if urlLink not in urlSet:
                q.insert(0, urlLink)
                urlSet.add(curLink)
                
    # print("found jobs: ", len(jobs))
    # for job in jobs:
    #     print(job)
        
    jobs = process.process_job_titles(titles)
    if len(jobs) > 0:
        # update company in database to found
        pass