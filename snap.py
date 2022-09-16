import requests 

from bs4 import BeautifulSoup

url = "https://www.snap.com/en-US/jobs?lang=en-US"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

print(soup)
