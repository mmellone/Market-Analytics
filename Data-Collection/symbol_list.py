import ftplib


def get_symbols(name=file_name):
    ''' Creates file containing information on all stock symbols (just symbol,
        no financial data).

        Param name - The name of the file to output into (anything in file will
                     be overwritten)

        Format of outputed file (each line):
        Nasdaq Traded|Symbol|Security Name|Listing Exchange|Market Category|...
        ETF|Round Lot Size|Test Issue|Financial Status|CQS Symbol|...
        NASDAQ Symbol|NextShares
    '''
    # Open a file to place the raw stock symbol info in
    raw_index_list = open('raw_index_list.txt', 'wb')

    # Open a connection to the nasdaqtrader ftp server
    ftp = ftplib.FTP('ftp.nasdaqtrader.com', 'anonymous', 'user@domain.com')
    ftp.cwd('SymbolDirectory')
    ftp.retrbinary('RETR nasdaqlisted.txt', raw_index_list.write)
    ftp.close()
    raw_index_list.close()


def main():
    f_name = 'symbol_info.txt'
    get_symbols(f_name)

if __name__ == '__main__':
    main()
