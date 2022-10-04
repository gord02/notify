import sqlQueries as queries

def check_on():
    sql_company_data = queries.get_companies()
    company_files = []
    
    # vector of vectors where each vector is a newly found company with job postings which we'll render in frontend
    to_render = []
    
    # gets filenames of companies that haven't been found yet
    for row in sql_company_data:
        company_files.append(row[1])
        
    for file in company_files:
        # removing file extension
        name = file.split('.')[0]
       
        # from the file name, get the file and import as module then access the getData() function which is the function name for scrapping all company webpages
        module = __import__(name)
        jobs = module.get_data()
        
        jobs.insert(0, name)
        to_render.append(jobs)   

    # if to_render is non empty, send email and render in frontend
check_on()
