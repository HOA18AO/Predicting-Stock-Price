import requests
import bs4
import pandas

import crawlOneDay

def crawler(soup : bs4.BeautifulSoup, df : pandas.core.frame.DataFrame):
    rows = soup.find_all('tr', {'class': 'simplize-table-row simplize-table-row-level-0'})
    for row in rows:
        data = crawlOneDay.crawler(row)
        newRow = pandas.DataFrame(data, index=[0])
        df = pandas.DataFrame([df, newRow], ignore_index=True)
    
    return df
        