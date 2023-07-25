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

companies = [addepar, akunaCapital, apple, arrowstreet, asana, block, bloomberg, citadel, databricks, deepmind, drw, figma, fiveRings, google, hrt, imc, janeStreet, jumpTrading, linkedIn, meta, netflix, nuro, openAi, optiver, pathAi, reddit, rippling, schonfeld, sig, snowflake, stripe, twitch, twoSigma, uber, yelp, zoom]

def addepar():
    company =  "Addepar"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
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
        
    jobs = process.process_job_titles(jobs)
    return jobs
    # return (jobs, success)    

def akunaCapital():
    company =  "Akuna Capital"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
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
    # return(jobs, success)

def apple():
    company =  "Apple"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    # access will be blocked without this user agent
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36" 
    opts.add_argument("user-agent=%s" % user_agent) 

    jobs = []
    url = "https://jobs.apple.com/en-us/search?location=united-states-USA+canada-CANC&team=internships-STDNT-INTRN"
    success = True
    
    try:
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
                
    # this is an exception caused by abnormal circumstances
    except WebDriverException as wbe:
        error=f"Exception parsing {company} "+ repr(wbe)
        # print(error)
        print("An exception occurred:", type(wbe).__name__) # An exception occurred: ZeroDivisionError
        # send email about scrapping error
        notify.parsing_error(error)
        
    # this is most likely an error caused by computer not being fully awake when code is run leading to max retry or ConnectionError error
    except ConnectionError as e:
        print("An exception occurred:", type(e).__name__) # An exception occurred: ZeroDivisionError
        # print("e: ", repr(e))
        # we want to retry when computer is fully awake
        success = False
        
    jobs = process.process_job_titles(jobs)
    if len(jobs) > 0:
        # update company in database to found
        sqlQueries.update_company(company)
        
    jobs.insert(0, url) 
    return(jobs, success)
    
def arrowstreet():
    company =  "Arrowstreet Capital"
    opts = Options()
    # so that browser instance doesn't pop up
    opts.add_argument("--headless")
    jobs = []
    
    url = "https://arrowstreetcapital.wd5.myworkdayjobs.com/en-US/Arrowstreet?q=intern&ref=levels.fyi"
    success = True
    

    try:
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options )
        driver.get(url)

        # wait for the specifc component with this class name to rendered before scraping
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-19uc56f")))

        content = driver.page_source
        soup = BeautifulSoup(content, "lxml")
        driver.quit()
        elements = soup.select("h3 > a")
        for element in elements:
            jobs.append(element.contents[0])
        
    # this is an exception caused by abnormal circumstances
    except WebDriverException as wbe:
        error=f"Exception parsing {company} "+ repr(wbe)
        # print(error)
        print("An exception occurred:", type(wbe).__name__) # An exception occurred: ZeroDivisionError
        # send email about scrapping error
        notify.parsing_error(error)
        
    # this is most likely an error caused by computer not being fully awake when code is run leading to max retry or ConnectionError error
    except ConnectionError as e:
        print("An exception occurred:", type(e).__name__) # An exception occurred: ZeroDivisionError
        # print("e: ", repr(e))
        # we want to retry when computer is fully awake
        success = False
        
        
    jobs = process.process_job_titles(jobs)
    if len(jobs) > 0:
        # update company in database to found
        sqlQueries.update_company(company)
    
    jobs.insert(0, url)
    return(jobs, success)

def asana(): 
def block(): 
def bloomberg():
def citadel():
def databricks():
def deepmind():
def drw():
def figma():
def fiveRings():
def google():
def hrt():
def imc():
def janeStreet(): 
def jumpTrading():
def linkedIn(): 
def meta(): 
def netflix(): 
def nuro():
def openAi():
def optiver(): 
def pathAi(): 
def reddit():
def rippling():
def schonfeld():
def sig():
    def snowflake():
def stripe(): 
def twitch(): 
    def twoSigma():
def uber():
def yelp():
def zoom():



def check_on():
    
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    
    print( "======================  ", "date: ", d2," time: ", current_time ,"  ======================")
    sql_company_data = queries.get_companies()
    company_files_names = []
    
    maxRetries = 3
    tryCount = dict()
    
    # vector of vectors where each vector is a newly found company with job postings which we'll render in frontend
    to_render = []
    
    # gets filenames of companies that haven't been found yet
    for row in sql_company_data:
        company_files_names.append(row[1])

    start_time = time.time()
    for file in company_files_names:
        # removing file extension
        name = file.split('.')[0]
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

check_on()



    # if len(jobs) > 0:
    #     # update company in database to found
    #     sqlQueries.update_company(company)
        
    # jobs.insert(1, url) 
    
    
    #     # this is an exception caused by abnormal circumstances
    # except WebDriverException as wbe:
    #     error=f"Exception parsing {company} "+ repr(wbe)
    #     # print(error)
    #     print("An exception occurred:", type(wbe).__name__) # An exception occurred: ZeroDivisionError
    #     # send email about scrapping error
    #     notify.parsing_error(error)
        
    # # this is most likely an error caused by computer not being fully awake when code is run leading to max retry or ConnectionError error
    # except ConnectionError as e:
    #     print("An exception occurred:", type(e).__name__) # An exception occurred: ZeroDivisionError
    #     # print("e: ", repr(e))
    #     # we want to retry when computer is fully awake
    #     success = False
        

    # jobs = process.process_job_titles(jobs)
    # if len(jobs) > 0:
    #     # update company in database to found
    #     sqlQueries.update_company(company)
        
    # jobs.insert(0, url)