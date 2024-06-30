import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table (example assumes there's only one table)
    table = soup.find('table')
    if table is None:
        return None

    # Extract table rows
    rows = table.find_all('tr')
    
    # Extract data from rows
    data = []
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    return data

# URLs to scrape
urls = [
    'https://results.eci.gov.in/PcResultGenJune2024/index.htm',
    'https://results.eci.gov.in/AcResultGenJune2024/index.htm',
    'https://results.eci.gov.in/AcResultByeJune2024/',
    'https://results.eci.gov.in/AcResultGen2ndJune2024/index.htm'
]

# Scrape data from each URL and store in DataFrames
dfs = {}
for url in urls:
    table_data = scrape_data(url)
    if table_data:
        df = pd.DataFrame(table_data[1:], columns=table_data[0])
        dfs[url] = df

# Save data to CSV files for further analysis
for url, df in dfs.items():
    filename = url.split('/')[-2] + '.csv'
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
