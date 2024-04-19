import pandas as pd

def reading(csvFile : __file__) -> pd.DataFrame: # remain full records of data
    df = pd.read_csv(csvFile)
    # set 'date' column as index
    df['date'] = pd.to_datetime(df['date'])
    df.set_index(df['date'], inplace=True)
    # remove nonsense
    df.drop(['change', 'change_percentage'], axis=True, inplace=True)
    return df
    
    
def cleaning(df : pd.DataFrame):
    df.drop(['date'], axis=True, inplace=True)
    # today close is last day's tomorrow close ???
    df['tomorrow_close'] = df['close'].shift(1)
    # now, the latest row does not have value on "tomorrow_close"
    # drop it
    df.dropna(inplace = True)
    return df