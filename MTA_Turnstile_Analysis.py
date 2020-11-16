import urllib
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

url='http://web.mta.info/developers/turnstile.html'
r=requests.get(url)
soup=BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())


# Get urls
for u in soup.find_all('a'):
    print (u.get('href'))


# Create list of urls containing txt data
base_url='http://web.mta.info/developers/'
links=[]

for u in soup.find_all('a', attrs={'href': re.compile("^data.*txt$")}):
    links.append(base_url+u.get('href'))
print (*links[:10], sep='\n')


# Specify data sets for year 2020
year_2020=[]
for link in range(len(links)):
    if '_20' in links[link]:
        year_2020+=[links[link]]
print (len(year_2020))
print (*year_2020, sep='\n')


# Preview one day data
df_preview = pd.read_csv(year_2020[-1])
print(df_preview.dtypes)
df_preview.head(10)


# Merge Multiple Data sets
chars = ['\\r', '\\n', '\n', 'b\'', ' ','\'','"']
total_records=[]
for file in year_2020:
    with urllib.request.urlopen(file) as response:
        new_records = []
        for line in response:
            for c in chars:
                line = str(line).replace(c, "")
            if line != 'C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS':
                new_records.append(line.split(','))
        for record in new_records:
            total_records.append(record)

df = pd.DataFrame(total_records, columns=['C/A','UNIT','SCP','STATION','LINENAME','DIVISION','DATE','TIME','DESC','ENTRIES','EXITS'])
df.shape # 9556799 rows x 11 columns

# Convert Columns' Data Types
df['DATE']=pd.to_datetime(df['DATE'])
df['EXITS']=df['EXITS'].astype('int64')
df['ENTRIES']=df['ENTRIES'].astype('int64')
df.dtypes

df.sort_values(by='DATE')
df['DATE'].unique()

# Station with the most number of units

# Total number of entries & exits across the subway system as of 2020