from ctypes import sizeof
import requests 

from bs4 import BeautifulSoup

url = "https://addepar.com/careers"
# url = "https://addepar.com/careers#engineering"

print("execute")
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# job_titles = soup.find_all("p", class_ ="f4")
# job_titles = soup.find_all("a")
# job_titles = soup.find_all("a", class_ ="engineering")
# job_titles = soup.find_all("p")
# job_titles = soup.select("p.f4")
# print("size: " , sizeof(job_titles))
# for title in job_titles:
#     print (str(title))
print(soup)


