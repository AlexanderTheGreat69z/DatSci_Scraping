#%%

'''SCRAPING DATA: TOP GAMES'''

from bs4 import BeautifulSoup as bs
import requests as re
import pandas as pd

# Download Website Data
headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://gaminganalytics.info/topplayed_last'
response = re.get(url,headers=headers)
soup = bs(response.text, "html.parser")

# Arrange Datakeys
data_keys = ['position', 'game-name', 'players', 'online-percentage', 'developer']
db_data = {}
for key in data_keys:
    db_data[key] = list()

# Store data
row = soup.find_all("tr")
for r in range(1, len(row)): 
    data = row[r].find_all("td")
    for d in data:
        element = d.get_text()
        if data.index(d) == 1:
            db_data[data_keys[0]].append(element)
        if data.index(d) == 2:
            db_data[data_keys[1]].append(element)
        if data.index(d) == 3:
            db_data[data_keys[2]].append(element)
        if data.index(d) == 4:
            db_data[data_keys[3]].append(element)
        if data.index(d) == 11:
            db_data[data_keys[4]].append(element)
        
# Create dataframe and CSV
df = pd.DataFrame(db_data)
df.to_csv('topgames.csv', index=False)

#%%

'''SCRAPING DATA: TOP GAMES'''

from bs4 import BeautifulSoup as bs
import requests as re
import pandas as pd

# Download Website Data
headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://www.boxofficemojo.com/year/world/'
response = re.get(url,headers=headers)
soup = bs(response.text, "html.parser")

# Get data keys
data_keys = ['rank', 'title', 'worldwide', 'domestic', 'dom%', 'foreign', 'for%']

# Arrange datakeys
db_data = {}
for key in data_keys: db_data[key] = list()

# Store data
row = soup.find_all('tr')
for r in range(1, 101):
    data = row[r].find_all('td')
    for d in data:
        element = d.get_text()
        if data_keys[data.index(d)] == 'worldwide' and element in db_data[data_keys[data.index(d)]]:
            continue
        db_data[data_keys[data.index(d)]].append(element)

# Minor adjustments (removing 'foreign and 'for%' as the data scrape got a little off)
db_data.pop('foreign')
db_data.pop('for%')

# Create dataframe and CSV
df = pd.DataFrame(db_data)
df.to_csv('topmovies.csv', index=False)
# %%
