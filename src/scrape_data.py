import urllib
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup


def main():
    print("Data retrieval started!")
    year_of_data = select_year(retrieve_data_sets())
    df = create_data_set(year_of_data)
    print("Done!")
    return df


def retrieve_data_sets():
    url = 'http://web.mta.info/developers/turnstile.html'
    base_url = 'http://web.mta.info/developers/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = []

    for u in soup.find_all('a', attrs={'href': re.compile("^data.*txt$")}):
        links.append(base_url + u.get('href'))

    return links


def select_year(links):
    input_year = input("Please enter 2 digit number for year in 2000s for data set retrieval: ")
    year = []
    for link in range(len(links)):
        if '_'+input_year in links[link]:
            year += [links[link]]
    print("Links for year 20"+input_year+" has been retrieved.")

    return year


def create_data_set(year):
    chars = ['\\r', '\\n', '\n', 'b\'', ' ', '\'', '"']
    total_records = []
    print("Creating dataframe...Please wait...")

    for file in year:
        with urllib.request.urlopen(file) as response:
            new_records = []
            for line in response:
                for c in chars:
                    line = str(line).replace(c, "")
                if line != 'C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS':
                    new_records.append(line.split(','))
            for record in new_records:
                total_records.append(record)

    df = pd.DataFrame(total_records,
                      columns=['C/A', 'UNIT', 'SCP', 'STATION', 'LINENAME', 'DIVISION', 'DATE', 'TIME', 'DESC',
                               'ENTRIES', 'EXITS'])

    return df


if __name__ == "__main__":
    main()