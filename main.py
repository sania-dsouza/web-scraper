import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime


def main():

    # URL to scrape
    url = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"

    # get the page and scrape
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find_all(id="ResultsContainer")

    titles = []
    descs = []
    dates = []
    for x in result:
        title = x.find("h1")
        desc = x.find('p')
        date = x.find("p", {"id" : "date"})
        titles.append(title.text)
        descs.append(desc.text)
        date = datetime.strptime(date.text.split(' ')[1], '%Y-%m-%d').date()
        dates.append(date)

    # get number of results to decide columns
    header = ["title", "description", "date"]

    # push results to csv (method)
    filename = "scrap_" + str(date.today()) + ".csv"
    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # get data to write
        for r in zip(titles, descs, dates):
            row = list(r)
            # write the data
            writer.writerow(row)

    return 0
