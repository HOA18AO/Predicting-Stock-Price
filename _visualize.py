import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
#import os

# using 2 columns, 'close' and 'date'
def drawChart(df : pd.DataFrame, stock_name : str = None):
    df['date'] = pd.to_datetime(df['date'])
    df.set_index(df['date'], inplace=True)
    plt.figure(figsize=(30, 10))
    plt.ylim(0, df['close'].max() * 1.1)
    if stock_name != None and stock_name != "":
        plt.title(stock_name)
    plt.xlabel('Time')
    plt.ylabel('Price (VND)')
    sns.set_style('darkgrid')
    sns.lineplot(data = pd.DataFrame(df, columns=('date', 'close')))
    
# using 1 column, 'close' and the index (datetime)
def drawChart2(df: pd.DataFrame, stock_name: str = None):
    # index = datetime
    # generate chart using the index, no need for another 'date' column
    plt.figure(figsize=(30, 10))
    plt.ylim(0, df['close'].max()*1.1)
    if stock_name not in [None, ""]:
        plt.title(stock_name)
    sns.lineplot(
        data = df,
        x = df.index, # because index is datetime
        y = 'close',
        color = 'g',
        label = 'Close price'
    )
    plt.xlabel('Date')
    plt.ylabel('Price (VND)')
    plt.grid(True)
    
    plt.xticks(rotation = 45)
    plt.yticks(rotation = 90)
    
    plt.legend()
    plt.show()