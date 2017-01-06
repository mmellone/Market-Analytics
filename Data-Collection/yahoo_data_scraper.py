from yahoo_finance import Share
from datetime import datetime
from flat_file_name import out_file_name
import flat_file_name


def info_string(sym, share):
    ''' Creates the csv info string to be written to the output file
        for each stock.

        Param sym - The stock symbol
        Param share - The yahoo_finance Share object referencing sym

        Returns a string in the format:
        'Stock_Symbol|Current_Price|PE_Ratio|PB_Ratio|PS_Ratio|50_DayMA|200_DayMA|Market_Cap|Book_Value|EBITDA|Dividend_Yield|Year_High|Year_Low|Date'
    '''
    date = datetime.now().strftime("%Y-%m-%d")
    info = [sym, share.get_price(), share.get_price_earnings_ratio(),
            share.get_price_book(), share.get_price_sales(),
            share.get_50day_moving_avg(), share.get_200day_moving_avg(),
            share.get_market_cap(), share.get_book_value(), share.get_ebitda(),
            share.get_dividend_yield(), share.get_year_high(),
            share.get_year_low(), date]

    # Replace mktcap, bookvalue, and ebitda string values with numbers
    for i in [7, 9]:
        if info[i] is None:
            continue
        if info[i][len(info[i])-1] == 'M':
            info[i] = float(info[i][:len(info[i])-1])*1000000.0
        elif info[i][len(info[i])-1] == 'B':
            info[i] = float(info[i][:len(info[i])-1])*1000000000.0

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
    output_file = 'flatfiles/' + out_file_name()
    with open('symbols.txt', 'r') as syms, open(output_file, 'w') as out:
        info = "ID|Stock_Symbol|Current_Price|PE_Ratio|PB_Ratio|PS_Ratio|50_DayMA|200_DayMA|Market_Cap|Book_Value|EBITDA|Dividend_Yield|Year_High|Year_Low|Datestamp\n"
        info += "INT|VARCHAR(8)|DECIMAL(12,2)|DECIMAL(12,2)|DECIMAL(12,2)|DECIMAL(12,2)|DECIMAL(12,2)|DECIMAL(12,2)|DECIMAL(20,2)|DECIMAL(20,2)|DECIMAL(20,2)|DECIMAL(12,2)|DECIMAL(12,2)|DECIMAL(12,2)|DATE\n"
        errors = []
        for i, s in enumerate(syms):
            data = ""
            if i % 50 == 0:
                print i, 'symbols processed'
            try:
                data = info_string(s.strip(), Share(s.strip()))
            except:
                print "There was an exception in iteration: ", i, ", symbol: ", s.strip()
                errors.append((i, s.strip()))
                data = "|||||||||||||"
            info += 'NULL|' + data + '\n'
        while len(errors) > 0:
            print "retrying errors"
            errors2 = []
            for e in errors:
                data = ''
                i = e[0]
                s = e[1]
                try:
                    data = info_string(s.strip(), Share(s.strip()))
                    info = info.replace('\n' + str(i) + '||||||||||||||', '\n' + str(i) + '|' + data)
                    print i, 'replaced'
                except:
                    print "There was an exception in iteration: ", i, ", symbol: ", s.strip()
                    errors2.append((i, s))
                    print 'there was another error'
            errors = errors2

        out.write(info)

    print output_file


if __name__ == '__main__':
    main()
