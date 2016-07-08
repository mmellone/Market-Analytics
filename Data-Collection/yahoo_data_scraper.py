from yahoo_finance import Share
from datetime import datetime


def out_file_name():
    ''' Returns a name for a file containing stock data in the Format
        'dd_mm_yyyy_stockdata.csv', where the date is the day that the
        data was taken from
    '''
    date = datetime.now()
    return '%s_%s_%s_stockdata.csv' % (date.day, date.month, date.year)


def info_string(sym, share):
    ''' Creates the csv info string to be written to the output file
        for each stock.

        Param sym - The stock symbol
        Param share - The yahoo_finance Share object referencing sym

        Returns a string in the format:
        'Stock_Symbol,Current_Price,P/E_Ratio'
    '''
    info = [sym, share.get_price(), share.get_price_earnings_ratio()]
    csv_info = ''
    for i, elem in enumerate(info):
        if elem is None:
            elem = ''
        csv_info += str(elem)
        if i != len(info)-1:
            csv_info += ','
    return csv_info


def main():
    ''' Reads from list of stock symbols and compiles basic data which it
        outputs to a file in the format described by the functions above
    '''
    with open('symbols.txt', 'r') as syms, open(out_file_name(), 'w') as out:
        info = ''
        for i, s in enumerate(syms):
            if i%50 == 0:
                print i, ' stocks processed'
            info += info_string(s.strip(), Share(s)) + '\n'
        out.write(info)


if __name__ == '__main__':
    main()
