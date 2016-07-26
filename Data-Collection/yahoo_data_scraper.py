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
        'Stock_Symbol|Current_Price|P_E_Ratio|P_B_Ratio|P_S_Ratio|50_DayMA|200_DayMA|Market_Cap|Book_Value|EBITDA|Dividend_Yield|Year_High|Year_Low|Date'
    '''
    date = datetime.now().strftime("%Y-%m-%d")
    info = [sym, share.get_price(), share.get_price_earnings_ratio(),
            share.get_price_book(), share.get_price_sales(),
            share.get_50day_moving_avg(), share.get_200day_moving_avg(),
            share.get_market_cap(), share.get_book_value(), share.get_ebitda(),
            share.get_dividend_yield(), share.get_year_high(),
            share.get_year_low(), date]
    csv_info = ''
    for i, elem in enumerate(info):
        if elem is None:
            elem = ''
        csv_info += str(elem)
        if i != len(info)-1:
            csv_info += '|'
    return csv_info


def main():
    ''' Reads from list of stock symbols and compiles basic data which it
        outputs to a file in the format described by the functions above
    '''
    output_file = out_file_name()
    with open('symbols.txt', 'r') as syms, open(output_file, 'w') as out:
        info = "ID|Stock_Symbol|Current_Price|P_E_Ratio|P_B_Ratio|P_S_Ratio|50_DayMA|200_DayMA|Market_Cap|Book_Value|EBITDA|Dividend_Yield|Year_High|Year_Low|Date\n"
        info += "INT NOT NULL AUTO_INCREMENT PRIMARY KEY|VARCHAR(8)|DECIMAL(10,2)|DECIMAL(8,2)|DECIMAL(8,2)|DECIMAL(8,2)|DECIMAL(10,2)|DECIMAL(10,2)|VARCHAR(16)|VARCHAR(16)|VARCHAR(16)|DECIMAL(6,2)|DECIMAL(10,2)|DECIMAL(10,2)|DATE\n"
        for i, s in enumerate(syms):
            info += str(i) + '|' + info_string(s.strip(), Share(s)) + '\n'
        out.write(info)
    print output_file


if __name__ == '__main__':
    main()
