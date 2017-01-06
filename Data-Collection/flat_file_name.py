from datetime import datetime

def out_file_name():
    ''' Returns a name for a file containing stock data in the Format
        'dd_mm_yyyy_stockdata.csv', where the date is the day that the
        data was taken from
    '''
    date = datetime.now()
    return '%s_%s_%s_stockdata.csv' % (date.day, date.month, date.year)

if __name__ == '__main__':
    print out_file_name()
