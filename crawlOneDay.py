import requests
from bs4 import BeautifulSoup
import bs4


def crawler(elementTag : bs4.element.Tag):
    data = {
    'date' : None, # ngay thang
    'open' : None, # gia mo cua
    'highest' : None, # gia cao nhat
    'lowest' : None, # gia thap nhat
    'close' : None, # gia dong cua
    'change' : None, # gia thay doi
    'change_percentage' : None, # % gia thay doi
    'volume' : None # khoi luong giao dich
    }
    
    stock_data_list = [i.text for i in elementTag.contents]
    
    data['date'] = stock_data_list[0]
    data['open'] = float(stock_data_list[1].replace(',', ''))
    data['highest'] = float(stock_data_list[2].replace(',', ''))
    data['lowest'] = float(stock_data_list[3].replace(',', ''))
    data['close'] = float(stock_data_list[4].replace(',', ''))
    if stock_data_list[5] == '-':
        data['change'] = float(0)
        data['change_percentage'] = float(0)
    else:
        data['change'] = float(stock_data_list[5].replace('+', '').replace(',', ''))
        data['change_percentage'] = float(stock_data_list[6].replace('%', ''))
    data['volume'] = int(stock_data_list[7].replace(',', ''))
    
    return data