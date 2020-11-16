# 🚂 MTA Subway Analysis 🚂  
<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/><img src="https://img.shields.io/badge/pandas%20-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" />
> *"Stand clear of the closing doors please..."  
> -Charlie Pellett (I actually met this guy)*  

New Yorkers spend a significant amount of their lives riding the MTA. This project looks to analyze public MTA data to understand how New York's present day system operates and how ridership is affected by Covid-19.

## Data Source
Data is scraped from [MTA Website's Turnstile Data.](http://web.mta.info/developers/turnstile.html)  
The focus of the analysis is to compare passenger behavior pre and post Covid-19 quarantine. For this purpose, we will examine 2020's turnstile data. Please note the following:
 - The first case of Covid-19 confirmed on 3/1/2020  
 - Closing of non-essential businesses was announced March 20, 2020  

## Column Information
```
C/A      = Control Area (A002)
UNIT     = Remote Unit for a station (R051)
SCP      = Subunit Channel Position represents an specific address for a device (02-00-00)
STATION  = Represents the station name the device is located at
LINENAME = Represents all train lines that can be boarded at this station
           Normally lines are represented by one character.  LINENAME 456NQR repersents train server for 4, 5, 6, N, Q, and R trains.
DIVISION = Represents the Line originally the station belonged to BMT, IRT, or IND   
DATE     = Represents the date (MM-DD-YY)
TIME     = Represents the time (hh:mm:ss) for a scheduled audit event
DESc     = Represent the "REGULAR" scheduled audit event (Normally occurs every 4 hours)
           1. Audits may occur more that 4 hours due to planning, or troubleshooting activities. 
           2. Additionally, there may be a "RECOVR AUD" entry: This refers to a missed audit that was recovered. 
ENTRIES  = The comulative entry register value for a device
EXIST    = The cumulative exit register value for a device
```
####  IRT vs. BMT vs. IND Lines  
Interborough Rapid Transit Company (IRT), Brooklyn-Manhattan Transit (BMT), and Independent Subway (IND) lines have a long history that you can [read about here](https://www.nycsubway.org/wiki/Subway_FAQ:_Which_Lines_Were_Former_IRT,_IND,_BMT#:~:text=The%20trains%20of%20the%20BMT,car%20to%20platform%20is%20unsafe.). In short, the city's IND took over bankrupt BMT and IRT companies June 1, 1940 and unified the transit systems into our modern day train system.