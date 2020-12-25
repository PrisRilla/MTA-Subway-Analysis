from src import scrape_data
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


df = scrape_data.main()
df.shape

# Convert Columns' Data Types
df['DATE'] = pd.to_datetime(df['DATE'])
df['DATE'] = df['DATE'].dt.tz_localize('US/Eastern')
df.sort_values(by='DATE')

df['EXITS'] = df['EXITS'].astype('int64')
df['ENTRIES'] = df['ENTRIES'].astype('int64')
df.dtypes
