#! /Users/gordon/UpdateProject/update/updateEnv/bin/python3
import os
from datetime import date

from importlib import import_module
from logic import sqlQueries as queries
from logic import notify

import time

from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()


def addepar():
    company =  "Addepar"
    jobs = []
    url = "https://addepar.com/careers#engineering"
    # success = True

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()

    elements = soup.select("p.f4")
    for element in elements:
        jobs.append(element.contents[0])
        print(element.contents[0])
    
    return jobs
    # return jobs    

def akunaCapital():
    company =  "Akuna Capital"
    jobs = []
    url = "https://akunacapital.com/careers?experience=intern"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("a > h2")
    locations = soup.select("a > h4")

    i = 0
    while i < len(elements):
        jobs.append(elements[i].contents[0] + " (" + locations[i].contents[0] + ")")
        # skip to next job title 
        i = i+ 1
        
    return jobs
    # return jobs

def apple():
    company =  "Apple"
    # access will be blocked without this user agent
    # user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36" 
    # opts.add_argument("user-agent=%s" % user_agent) 

    jobs = []
    url = "https://jobs.apple.com/en-us/search?location=united-states-USA+canada-CANC&team=internships-STDNT-INTRN"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()

    # allows us to traverse pages 
    page = soup.find(id="page-number")
    page1 =  (int)(page['value'])
    pages = soup.select("span.pageNumber")
    endPage = (int)(pages[1].contents[0])
    pageNum = "&page="
    
    while page1 <= endPage:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
        newUrl = url + pageNum + str(page1)
        driver.get(newUrl)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        elements = soup.select("a.table--advanced-search__title")
        for element in elements:
            jobs.append(element.contents[0])
        page1+=1   

    return jobs
    
def arrowstreet():
    company =  "Arrowstreet Capital"
    jobs = []
    
    url = "https://arrowstreetcapital.wd5.myworkdayjobs.com/en-US/Arrowstreet?q=intern&ref=levels.fyi"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)

    # wait for the specifc component with this class name to rendered before scraping
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-19uc56f")))

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("h3 > a")
    for element in elements:
        jobs.append(element.contents[0])

    return (jobs)

def asana(): 
    company =  "Asana"
    jobs = []
    
    url = "https://asana.com/jobs/all"
    
    success = True

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("div.jobs-listing-title > strong")
    locations = soup.select("div.jobs-listing-location")

    i = 0
    while i < len(elements):
        jobs.append(elements[i].contents[0] + " (" + locations[i].contents[0] + ")")
        # skip to next job title 
        i = i+ 1

    return jobs

def block():  
    url = "https://block.xyz/careers?types=Intern"
    jobs = []
    success = True
    
    company =  "Block"

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()

    elements = soup.select("div.JobList_titleColumn__3oZrC")
    
    for x in elements:
        # print(x.contents[0])
        jobs.append(x.contents[0])
        
    return jobs


def bloomberg():
    jobs = []
    company = "Bloomberg"
    url = "https://careers.bloomberg.com/job/search?el=Internships"
    success = True

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    # print(soup)
    elements = soup.select("a.js-display-job")

    for element in elements:
        jobs.append(element.contents[0])
       
    return jobs    

def citadel():
    company = "Citadel"
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )

    url = "https://www.citadel.com/careers/open-opportunities/students/internships/"
    jobs = []
    success = True

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("span > a")

    for element in elements:
        # print(element.contents[0])
        jobs.append(element.contents[0])
    
    return jobs    

def ctc(): 
    company =  "Chicago Trading Company"
    jobs = []
    
    url = "https://www.chicagotrading.com/search"
    success = True

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("div.title > h3")
    # locations = soup.select("div.job-meta > span")

    for element in elements:
        # print(element)
        jobs.append(element.contents[0])
            
    return jobs

def databricks(): 
    company =  "Databricks"
    jobs = []

    url = "https://www.databricks.com/company/careers/open-positions"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("a span")
    
    i = 0
    # there will be a second a span for every span which is its location
    while i+1 < len(elements):
        jobs.append(elements[i].contents[0] + " (" + elements[i+1].contents[0] + ")")
        # skip to next job title 
        i = i +2;  
        
    return jobs

def deepmind():
    company = "Deepmind"
    jobs = []
    
    success = True
    
    url = "https://www.deepmind.com/careers/jobs?teams=Engineering&sort=newest_first"
    

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("tr.jobs-table-row td")
    for element in elements:
        if len(element.contents) > 0:
            jobs.append(element.contents[0])

    return jobs

def drw():
    company =  "DRW"
    jobs = []
    url = "https://drw.com/work-at-drw/category/campus/"
    success = True
    

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("a > div > h3")
    locations = soup.select("a > div > p")
    for i, element in enumerate (elements):
        jobs.append(element.contents[0] + " (" + locations[i].contents[0]+ ")")
                     

    return jobs

def figma(): 
    company =  "Figma"
    jobs = []
    url = "https://www.figma.com/careers/#job-openings"
    success = True
    

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    # print(soup)
    driver.quit()

    
    elements = soup.select("div.figma-cn3xcj a")
    for element in elements:
        # titles.add(element.contents[0])
        jobs.append(element.contents[0])
        
    return jobs    
    
def fiveRings(): 
    company =  "Five Rings"
    jobs = []
    url = "https://fiverings.avature.net/careers"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("h3 > a")
    for element in elements:
        jobs.append(element.contents[0].strip())
        # print(element.contents[0].strip())

    return jobs 

def google(): 
    company =  "Google"
    jobs = []
    url = "https://careers.google.com/jobs/results/?degree=BACHELORS&distance=50&employment_type=INTERN&jex=ENTRY_LEVEL&location=United%20States&location=Canada"
    # url ="https://www.google.com/about/careers/applications/jobs/results/?distance=50&location=United%20States&location=Canada&degree=BACHELORS"
    success = True
    
    i = 1
    # 1000 is an arbitrary number of pages that Google might have for jobs in the worst case we would have to go through
    while i<= 1000:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
        newUrl = url + "&page=" + str(i)
        driver.get(newUrl)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        
        # this is a check to make sure there are still jobs left in current tab
        shownPages = soup.find('div', jsname = "uEp2ad")

        if(shownPages is None):
            # print("finished all pages at i equal to : ", i-1)
            break
        
        elements = soup.select("div h3")
        # print(elements)
        for element in elements:
            jobs.append(element.contents[0])
            # print(element.contents[0])
        i+=1   
        # print("===========")
            
    return jobs    

def hrt(): 
    company =  "Hudson River Trading"
    jobs = []
    
    url = "https://www.hudsonrivertrading.com/careers/?ref=levels.fyi&_4118765=Internship&_offices=Chicago%2CLondon%2CNew+York"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")

    driver.quit()
    elements = soup.select("span.job-title")
    for element in elements:
        jobs.append(element.contents[0])
    
    return jobs

def imc(): 
    company =  "IMC"
    jobs = []
    
    url = "https://imc.wd5.myworkdayjobs.com/en-US/invitation/jobs/details/Quant-Trader-Intern---Summer-2023_REQ-01963?workerSubType=71540894c45741dfba126cdff9489e52"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    # wait for the specifc component with this class name to rendered before scraping
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-129m7dg")))
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("h3 > a")

    i = 0
    while i < len(elements):
        jobs.append(elements[i].contents[0])
        # skip to next job title 
        i = i+ 1
        
    return jobs

def janeStreet():  
    company =  "Jane Street"
    jobs = []
    
    url = "https://www.janestreet.com/join-jane-street/open-roles/?type=internship&location=all-locations"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    
    elements = soup.select("div.position p")
    for element in elements:
        # positions dont have intern in them but they are intern roles
        jobs.append(element.contents[0]+ " Intern")
        
    return jobs    
    
def jumpTrading():
    company = "Jump Trading"
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )

    url = "https://www.jumptrading.com/careers/?locations=Chicago+New-York&titleSearch=campus+intern"
    jobs = []
    success = True
    
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("a > div > div > p")

    # for i, element in enumerate(elements):
    i=0
    # each p tag is the job name and the following p tag is the location 
    while i+1 < len(elements):
        jobs.append(elements[i].contents[0] + ": " + elements[i+1].contents[0])
        # skips to the next job title
        i = i + 2
    
    return jobs    


def linkedIn(): 
    company =  "LinkedIn"
    jobs = []
    success = True
    
    
    url = "https://www.linkedin.com/jobs/search/?currentJobId=3502921259&f_C=1337&f_TPR=r86400&geoId=92000000"
    

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    
    # Not reliable scrap since we cannot navigate through linkedin page results but the filters for above 
    # link(posted in last 24 hours) will help keep results limited to one page
    elements = soup.select("a span")
    
    for element in elements:
        jobs.append(element.contents[0].strip())
        # print(element.contents[0].strip())
    
    return jobs    
    

def meta():  
    company =  "Meta"

    start_time = time.time()

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    #driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    url = "https://www.metacareers.com/jobs?leadership_levels[0]=Individual%20Contributor&teams[0]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design"
    jobs = []      
    success = True
    
    # does not work for multiple pages results
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    # print(soup)
    driver.quit()
    
    elements = soup.select("div._8sel")
    # elements = soup.select("div._8se1 _97f")
    # pages= soup.find("div",  {"class": ["_8se1", "_97f"]})
    # pageText = pages.contents[0]
    # bounds = pageText.split()
    # start = bounds[3]
    # end = bounds[5]
    # page = 1

    for x in elements:
        print(x.contents[0])
        jobs.append(x.contents[0])

    return jobs

def netflix():  
    company =  "Netflix"
    jobs = []
    url = "https://jobs.netflix.com/search?team=Data%20Science%20and%20Engineering"
    success = True

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )

    driver.get(url)
    # wait for the specifc component with this class name to rendered before scraping
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "e1rpdjew0")))

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")

    driver.quit()
    elements = soup.select("h4.e1rpdjew0")
    for element in elements:
        jobs.append(element.contents[0])

    return jobs

def nuro():
    company =  "Nuro"
    jobs = []
    success = True
    url = "https://www.nuro.ai/careers#careers-listing"

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("a.job-title")
    for element in elements:
        jobs.append(element.contents[0])

    return jobs

def openAi(): 
    company =  "OpenAi"
    jobs = []
    url = "https://openai.com/careers/search"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("a > h3")

    for element in elements:
        jobs.append(element.contents[0])
                     
    return jobs

def optiver():  
    company =  "Optiver"
    jobs = []
    url = "https://optiver.com/working-at-optiver/career-opportunities/?_gl=1*14qqpxn*_up*MQ..*_ga*Nzk0MDYzODM5LjE2NzgwNTExMDM.*_ga_YMLN3CLJVE*MTY3ODA1MTEwMS4xLjAuMTY3ODA1MTEwMS4wLjAuMA..&numberposts=10"
    success = True

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("h5 > a")
    locations = soup.select("p.text-s")
    for i, element in enumerate (elements):
        jobs.append(element.contents[0] + ": (" + locations[i].contents[2].strip() + ")")

    return jobs

def pathAi(): 
    # Could use Wo 
    company =  "PathAi"
    jobs = []
    start = time.time()
    url = "https://www.pathai.com/careers/"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    # wait for the specifc component with this class name to rendered before scraping
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "s-careers-usa")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ResourceCard__Title-sc-x9mf40-1")))
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    # print(soup)
    elements = soup.select("h3.ResourceCard__Title-sc-x9mf40-1")
    
    # locations = soup.select("a > h4")
    # print(len(elements))
    i = 0
    while i < len(elements):
        # jobs.append(elements[i].contents[0] + " (" + locations[i].contents[0] + ")")
        jobs.append(elements[i].contents[0])
        # print(elements[i])
        # skip to next job title 
        i = i+ 1

    return jobs

def reddit():
    company = "Reddit"
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )

    url = "https://www.redditinc.com/careers/#job-info"
    jobs = []
    success = True

    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("div.job a div.job-title")

    for element in elements:
        if len(element.contents) != 0:
            # print(element.contents[0])
            jobs.append(element.contents[0])

    return jobs    

def rippling(): 
    company =  "Rippling"
    
    opts.add_argument("--headless")
    # so that browser instance doesn't pop up
    
    opts.add_argument("--window-size=1920,1080")
    
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36" 
    opts.add_argument("user-agent=%s" % user_agent) 
    url = "https://www.rippling.com/careers/open-roles"
    success = True
    # ---

    jobs = []
    start = time.time()

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    # wait for the specifc component with this class name to rendered before scraping
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "s-careers-usa")))
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "w-22")))
    # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "s-careers-usa")))
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    # print(soup)
    elements = soup.select("a > p")
    locations = soup.select("div.md\:pl-16 > p.pl-8") 
    
    i = 0
    pl = 0
    # print(len(elements))
    # print(len(locations))
    while i < len(elements):
        # print(elements[i].contents[0] + " (" + locations[pl].contents[0] + ")")
        jobs.append(elements[i].contents[0] + " (" + locations[pl].contents[0] + ")")
        # skip to next job title 
        i = i+ 2
        pl += 1
            
    return jobs

def schonfeld(): 
    company =  "Schonfeld"
    jobs = []
    
    url = "https://boards.greenhouse.io/schonfeld?ref=levels.fyi"
    success = True

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("div.opening a")
    locations = soup.select("span.location")

    i = 0
    while i < len(elements):
        jobs.append(elements[i].contents[0] + " (" + locations[i].contents[0] + ")")
        # skip to next job title 
        i = i+ 1
        
    return jobs

def sig(): 
    company =  "SIG"
    jobs = []
    start = time.time()
    url = "https://careers.sig.com/search-results?keywords=intern&ref=levels.fyi"
    success = True
    
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("div.job-title > span")
    next = soup.select_one("a.next-btn")
    for element in elements:
        jobs.append(element.contents[0])
    
    while(True):
        # if(next != None and 'href' not in next.attrs):
        # print(next)
        # print("next: ", next.attrs )
        # print("next: ", next.contents )
        
        if('href' not in next.attrs):
            # print("not found")
            break
        
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
        driver.get(next['href'])   
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()
        elements = soup.select("div.job-title > span")
        for element in elements:
            jobs.append(element.contents[0])
            
        next = soup.select_one("a.next-btn")
            
    return jobs


def snowflake():
    company =  "Snowflake"
    jobs = []
    
    url = "https://careers.snowflake.com/us/en/search-results?rk=l-university-recruiting&sortBy=Most%20relevant"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )

    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("div.job-title > span")
    locations = soup.select("span.job-location")

    for i, element in enumerate (elements):     
        job= element.contents[0]
        if(len(locations[i].contents) >=9):
            job = job + " (" + locations[i].contents[8].strip()+ ")"
        # print(job)
        jobs.append(job)
         

    return jobs
    

def snap():   
    company = "Snapchat"
    jobs = []
    url = "https://www.snap.com/en-US/jobs?lang=en-US"
    success = True

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    print(soup)
    driver.quit()

    elements = soup.select("th a")
    for element in elements:
        jobs.append(element.contents[0])

    return jobs   

def snowflake():
    company =  "Snowflake"
    jobs = []
    
    url = "https://careers.snowflake.com/us/en/search-results?rk=l-university-recruiting&sortBy=Most%20relevant"
    success = True
    
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("div.job-title > span")
    locations = soup.select("span.job-location")

    for i, element in enumerate (elements):     
        job= element.contents[0]
        if(len(locations[i].contents) >=9):
            job = job + " (" + locations[i].contents[8].strip()+ ")"
        # print(job)
        jobs.append(job)
        
    return job

def stripe():  
    company =  "Stripe"
    jobs = []
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    url = "https://stripe.com/jobs/search"
    success = True
    
    # more specific link
    # https://stripe.com/jobs/search?teams=University&office_locations=North+America--Chicago&office_locations=North+America--Mexico+City&office_locations=North+America--New+York&office_locations=North+America--Seattle&office_locations=North+America--South+San+Francisco&office_locations=North+America--Toronto
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()

    elements = soup.select("a.JobsListings__link")
    for element in elements:
        jobs.append(element.contents[0])
         
    return jobs

def twitch():  
    company =  "Twitch"
    jobs = []
    url = "https://www.twitch.tv/jobs/en/careers/"
    success = True
    

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    driver.get(url)
    
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
    elements = soup.select("div.py-4 > div > a")
    
    for element in elements:
        if(len(element.contents) > 0):
            jobs.append(element.contents[0])
                     
    return jobs

def twoSigma():
    company =  "twoSigma"

    start_time = time.time()
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    url = "https://careers.twosigma.com/careers/SearchJobs/Intern?2047=%5B9813555%5D&2047_format=1532&listFilterMode=1"
    jobs = []
    success = True
    
    # set for urls and jobs
    urlSet = set()
    titles = set()

    # Create queue to store urls
    q = []


    q.append(url)   
    urlSet.add(url)
        
    # For each page, first push current to set, get all links for other pages, and if not in set, push to queue
    while len(q) > 0:
        curLink = q.pop()
        urlSet.add(curLink)
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
        driver.get(curLink)
        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()
        
        elements = soup.select("a.mobileShow")    

        for element in elements:
            titles.add(element.contents[0])
        
        paginationLinks = soup.select("a.paginationLink")
        # print("paginationLinks: ", paginationLinks)
        
        for link in paginationLinks:
            urlLink = link.get("href")
            # print("urlLink: ", urlLink)
            if urlLink not in urlSet:
                q.insert(0, urlLink)
                urlSet.add(curLink)
        
    return jobs   

def uber():
    company =  "Uber"
    jobs = []
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    url = "https://www.uber.com/ca/en/careers/list/?department=University&team=University&team=Engineering"
    success = True

    # https://www.uber.com/ca/en/careers/list/?location=CAN-Ontario-Toronto&location=USA-Illinois-Chicago&location=USA-California-San%20Fransisco&location=USA-New%20York-New%20York%20City&department=University&team=University&team=Engineering
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()
        
    elements = soup.select("a.css-bNzNOn")
    # locations = soup.select("div > div > div > span.css-dCwqLp")
    
    for element in elements:
        jobs.append(element.contents[0])
        
    return jobs

def yelp():
    company = "Yelp"
    
    start_time = time.time()
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    start = time.time()
    jobs = []
    
    url = "https://www.yelp.careers/us/en/search-results"
    success = True
    
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()

    titles = set()

    # Page has pagination
    usedLinks = set()
    q = []
    # skipping the prev button, there is hidden prev link that will be first in the list so skip to index 1
    firstLink = soup.select("ul.pagination li a")[1]['href']

    q.append(firstLink)
    while len(q) > 0:
        link = q.pop()
        usedLinks.add(link)
        # have to re-initialize new web driver for new calls
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
        driver.get(link)
        page = driver.page_source
        driver.quit()
        soup = BeautifulSoup(page, "lxml") 
        
        jobTitles =  soup.select("div.job-title span")
        for jobT in jobTitles:
            titles.add(jobT.contents[0])
        
        links = soup.select("ul.pagination li a")
        for newLink in links:
            urlLink =  newLink['href'] 
            if urlLink not in usedLinks and len(urlLink) > 0:
                    q.insert(0, urlLink) 
                    # prevents repeated addition of the same url to the q
                    usedLinks.add(urlLink)
                        
    return jobs   

def zoom(): 
    company =  "Zoom"
    jobs = []
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
    url = "https://careers.zoom.us/global-emerging-talent"
    
    success = True
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    driver.quit()

    elements = soup.select("td.job-title a")
    for element in elements:
        jobs.append(element.contents[0])
            
    return jobs

companies = [addepar, akunaCapital, apple, arrowstreet, asana, block, bloomberg, citadel,ctc, databricks, deepmind, drw, figma, fiveRings, google, hrt, imc, janeStreet, jumpTrading, linkedIn, meta, netflix, nuro, openAi, optiver, pathAi, reddit, rippling, schonfeld, sig, snap, snowflake, stripe, twitch, twoSigma, uber, yelp, zoom]


# def check_on():
    
#     today = date.today()
#     d2 = today.strftime("%B %d, %Y")
#     t = time.localtime()
#     current_time = time.strftime("%H:%M:%S", t)
    
#     print( "======================  ", "date: ", d2," time: ", current_time ,"  ======================")
#     sql_company_data = queries.get_companies()
#     company_files_names = []
    
#     maxRetries = 3
#     tryCount = dict()
    
#     # vector of vectors where each vector is a newly found company with job postings which we'll render in frontend
#     to_render = []
    
#     # gets filenames of companies that haven't been found yet
#     for row in sql_company_data:
#         company_files_names.append(row[1])

#     start_time = time.time()
#     for file in company_files_names:
#         # removing file extension
#         name = file.split('.')[0]
#         # print("==========start=========")
#         try: 
#             # from the file name, get the file and import as module then access the getData() function which is the function name for scrapping all company webpages
#             module = import_module("companies." +name)
#             ret_tuple = module.get_data()
#             jobs = ret_tuple[0]
#             success = ret_tuple[1]
                         
#             # failed likely due to bad connection
#             if (success == False):     
#                 print("failure on ", name)  
#                 # add file to try count
#                 if name not in tryCount.keys():
#                     tryCount[name] = 1
#                     print("adding to map")
#                 else:
#                     tryCount[name] = tryCount[name] + 1
#                     print("incr count")
                    
                
#                 if tryCount[name] < 3:
#                     # add to set again and retry company 
#                     company_files_names.append(file) 
#                     print("re adding")
#                 else:
#                     print(f"max retries reached for {name}")
#             jobs.insert(0, name)
            
#             if(len(jobs) > 2):
#                 print(name)
#                 to_render.append(jobs) 
#         except Exception as e:
#             print(f"Exception when getting data from company: {name}: ", e)
#             print("The exception type:", type(e).__name__) 
#             # call to error email 
#         # print("===========end=========")
  
#     print("minutes: ", (time.time() - start_time)/60)
#     if len(tryCount) != 0:
#         print("retries: ", tryCount)
#     # if to_render is non empty, send email and render in frontend
#     if len(to_render) > 0:
#         print("Companies with job postings: " , len(to_render))
#         notify.send_email(to_render)
#         # exec(open("app.py").read())

# check_on()


def update():
    
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    start_time = time.time()
    
    print( "======================  ", "date: ", d2," time: ", current_time ,"  ======================")
    sql_company_data = queries.get_companies()
    company_files_names = []

    
    # gets filenames of companies that haven't been found yet
    for row in sql_company_data:
         # removing file extension
        name = row[1].split('.')[0]
        company_files_names.append(name)

    # counts number of retries per company function
    tryCount = dict()
    
    # vector of vectors where each vector is a newly found company with job postings which we'll render in frontend
    to_render = []
    
    for company in companies:
        jobs = []
        maxRetries = 3
        try:
            jobs = company()
    
        # this is an exception caused by abnormal circumstances
        except WebDriverException as wbe:
            error=f"Exception parsing {company} "+ repr(wbe)
            # print(error)
            print("WebDriverException exception occurred:", type(wbe).__name__) # An exception occurred: ZeroDivisionError
            # send email about scrapping error
            notify.parsing_error(error)
            
        # this is most likely an error caused by computer not being fully awake when code is run leading to max retry or ConnectionError error
        except ConnectionError as e:
            print("ConnectionError error occurred:", type(e).__name__) # An exception occurred: ZeroDivisionError
            # print("e: ", repr(e))
            # we want to retry when computer is fully awake
            success = False
            
        except error as e:
            print("An exception occurred:", type(e).__name__)
          
        jobs = process.process_job_titles(jobs)  
        if len(jobs) > 0:
            # update company in database to found
            sqlQueries.update_company(company)
            
            # you hvae jobs, therefore set up jobs array to store necessary data for email 
        
            jobs.insert(1, url) 
            jobs.insert(1, url) 
            
            
            
    

    for file in company_files_names:
       
        # print("==========start=========")
        try: 
            # from the file name, get the file and import as module then access the getData() function which is the function name for scrapping all company webpages
            module = import_module("companies." +name)
            ret_tuple = module.get_data()
            jobs = ret_tuple[0]
            success = ret_tuple[1]
                         
            # failed likely due to bad connection
            if (success == False):     
                print("failure on ", name)  
                # add file to try count
                if name not in tryCount.keys():
                    tryCount[name] = 1
                    print("adding to map")
                else:
                    tryCount[name] = tryCount[name] + 1
                    print("incr count")
                    
                
                if tryCount[name] < 3:
                    # add to set again and retry company 
                    company_files_names.append(file) 
                    print("re adding")
                else:
                    print(f"max retries reached for {name}")
            jobs.insert(0, name)
            
            if(len(jobs) > 2):
                print(name)
                to_render.append(jobs) 
        except Exception as e:
            print(f"Exception when getting data from company: {name}: ", e)
            print("The exception type:", type(e).__name__) 
            # call to error email 
        # print("===========end=========")
  
    print("minutes: ", (time.time() - start_time)/60)
    if len(tryCount) != 0:
        print("retries: ", tryCount)
    # if to_render is non empty, send email and render in frontend
    if len(to_render) > 0:
        print("Companies with job postings: " , len(to_render))
        notify.send_email(to_render)
        # exec(open("app.py").read())