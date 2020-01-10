# request
import requests
from bs4 import BeautifulSoup
url='http://web.mta.info/developers/turnstile.html'
r=requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

# get urls
for u in soup.find_all('a'):
    print (u.get('href'))

# create list of urls containing txt data
import re
base_url='http://web.mta.info/developers/'
links=[]

for u in soup.find_all('a', attrs={'href': re.compile("^data")}):
    links.append(base_url+u.get('href'))
print (*links, sep='\n')

# specify data sets for year 2013
year_2013=[]
for link in range(len(links)):
    if '_13' in links[link]:
        year_2013+=[links[link]]
print (year_2013)
len(year_2013)
print (*year_2013, sep='\n')


# creating dataframe
import urllib
import pandas as pd
import numpy as np

# preview
df1 = pd.read_csv(year_2013[-1], header=None)
df1

# creating data set
total_records = []
for file in year_2013:
    with urllib.request.urlopen(file) as response:
        new_records = []
        for line in response:
            line=str(line).replace(" ", "").replace("\\r\\n", "").replace("'","")
            row = line.split(',')
            first_three, remaining = row[:3], row[3:]
            n = 5
            new_record = [ first_three + remaining[i:i + n]
                           for i in range(0, len(remaining), n)]
            new_records += new_record
        total_records += (new_records)
df=pd.DataFrame(total_records, columns=["C/A","UNIT","SCP","DATE","TIME","DESC","ENTRIES","EXITS"])

#Get rid of leading zeros for Exits Column
df.head(100)
df.shape #(203114, 8)
df.sort_values(by='DATE')

x=df.to_csv(r'C:\Users\PrisR\Two Sigma\MTA_Turnstile.csv')
type(df.DATE[0])
print (df.DATE[0])

#reindex
#groupby5
print(year_2013)

# first_three = [a,b,c]
# units_of_5 = [[1,2,3,4,5],[1,2,3,4,5]..]
# new_record=[a,b,c,1,2,3,4,5]
# total_records = [[a,b,c,1,2,3,4,5], ...]

# C/A = Control Area (A002)
# UNIT = Remote Unit for a station (R051)
# SCP = Subunit Channel Position represents an specific address for a device (02-00-00)
# DATEn = Represents the date (MM-DD-YY)
# TIMEn = Represents the time (hh:mm:ss) for a scheduled audit event
# DEScn = Represent the "REGULAR" scheduled audit event (occurs every 4 hours)
# ENTRIESn = The comulative entry register value for a device
# EXISTn = The cumulative exit register value for a device

#############################################################
# Which station has the most number of units?
# Wall Street
df.loc[:,'UNIT'].mode()  #R043
df.UNIT.value_counts().idxmax() #R043
df.UNIT.value_counts().max()  #253221 occurrences

# What is the total number of entries & exits across the subway system for February 1, 2013?
df["DT"]=pd.to_datetime(df['DATE'] + ' ' + df['TIME'])
df.sort_values(by=['DT'], inplace=True, ascending=True)
df.head(10)
df.tail(10)
df.index = df['DT']
del df['DT']
df['2013']


df['2013'].ENTRIES.resample('M').sum()
df['2013'].EXITS.resample('M').sum()


# Let’s define the busy-ness as sum of entry & exit count. What station was the busiest on February 1, 2013? What turnstile was the busiest on that date?

# What stations have seen the most usage growth/decline in 2013?

# What dates are the least busy? Could you identify days on which stations were not operating at full capacity or closed entirely?

# Bonus:  What hour is the busiest for station CANAL ST in Q1 2013?



