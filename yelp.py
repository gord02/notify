import requests 

from bs4 import BeautifulSoup

url = "https://www.yelp.careers/us/en/search-results"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
spans = soup.select("span")
print(spans)
