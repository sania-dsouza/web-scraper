import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"

# get the page and scrape
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer").find('h1')

for i in results:
    print(i.text)

# some processing for example sorting desc by date of posting
# get number of results to decide columns
# push results to csv (method)


# parametrize the selector