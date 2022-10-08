from importlib import import_module
from logic import sqlQueries as queries
from logic import notify

def check_on():
    sql_company_data = queries.get_companies()
    company_files_names = []
    
    # vector of vectors where each vector is a newly found company with job postings which we'll render in frontend
    to_render = []
    
    # gets filenames of companies that haven't been found yet
    for row in sql_company_data:
        company_files_names.append(row[1])
        
    for file in company_files_names:
        # removing file extension
        name = file.split('.')[0]
       
        # from the file name, get the file and import as module then access the getData() function which is the function name for scrapping all company webpages
        module = import_module("companies." +name)
        jobs = module.get_data()
        
        jobs.insert(0, name)
        to_render.append(jobs)   

    # if to_render is non empty, send email and render in frontend
    # if len(to_render) > 0:
        # notify.send_email(to_render)
    if True:
        exec(open("app.py").read())
    
check_on()
