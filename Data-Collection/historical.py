from yahoo_finance import Share
import pandas as pd
import os

""" A collection of functions to gather and perform basic processing on historical
stock data from Yahoo. Uses Pandas dataframes objects to organize data
"""

def generate_csv(symbol, start_date, end_date, file_name=''):
    """ Generates a csv of historical stock data for a given stock symbol and
    start and end date.
    symbol - string
    start_date - string, in date format (i.e. '2014-01-20')
    end_date - string, in date format (after start_date, i.e. 2015-02-21)
    file_name - string, name of file to output, automatically generated if no
                file is given

    returns - name of csv file that was created
    """
    stock_info = Share(symbol)
    historical_data = stock_info.get_historical(start_date, end_date)
    outputstring = 'Date,Open,Low,High,Close,Adj_Close,Volume\n'
    for day in historical_data:
        day_info = [day['Date'],day['Open'],day['Low'],day['High'],day['Close'],day['Adj_Close'],day['Volume']]
        outputstring += ','.join(day_info) + '\n'
    if file_name == '':
        file_name = '_'.join([symbol,start_date,end_date]) + '.csv'
    with open(file_name, 'w') as csv:
        csv.write(outputstring)
    return file_name


def get_dataframe(symbols, start_date, end_date, components=['Adj_Close']):
    """ Generates a dictionary of dataframe(s) with information about the
    stock symbols.
    symbols - list of strings, stock symbols to include in columns of dataframes
    start_date - string, in date format (i.e. '2014-01-20')
    end_date - string, in date format (after start_date, i.e. 2015-02-21)
    components - list of strings, data components to be included in dataframes,
                 one dataframe per component.
                 Default: ['Adj_Close']
    returns - a dictionary of components to their respective dataframe
    """
    # Initialize dataframes
    dates = pd.date_range(start=start_date, end=end_date)
    dfs = {}
    for comp in components:
        dfs[comp] = pd.DataFrame(index=dates)

    # Add SPY to symbols as base reference
    if 'SPY' not in symbols:
        symbols.append('SPY')

    # Create csv files for each symbol and load info into dataframes
    for symbol in symbols:
        # print "Collecting data for symbol", symbol
        csv = generate_csv(symbol, start_date, end_date)
        for component in components:
            df_temp = pd.read_csv(csv, index_col='Date', parse_dates=True, usecols=['Date', component])
            df_temp = df_temp.rename(columns={component: symbol})
            dfs[comp] = dfs[comp].join(df_temp)
            if symbol == 'SPY':
                dfs[comp] = dfs[comp].dropna(subset=['SPY'])
        os.remove(csv)
    return dfs
