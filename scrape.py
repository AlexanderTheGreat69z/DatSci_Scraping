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

headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://www.boxofficemojo.com/year/world/'
response = re.get(url,headers=headers)
soup = bs(response.text, "html.parser")

# Get data keys
headers = soup.find_all('th')
data_keys = [h.get_text() for h in headers]
print(data_keys)

db_data = {}
for key in data_keys: db_data[key] = list()

row = soup.find_all('tr')
for r in row:
    data = r.find_all('td')
    for d in data:
        element = d.get_text()
        # print(element)
        if element == '-':
            element = 'NULL'
        db_data[data_keys[data.index(d)]].append(element)
    #  print('\n=========================================\n')

# for key in db_data.keys():
#     print(len(db_data[key]))
i = 1
for k in db_data['Foreign']:
    print(k, i)
    i+=1
# %%
