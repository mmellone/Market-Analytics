import ftplib


def get_symbols(name):
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
    output_file = open(name, 'wb')

    # Open a connection to the nasdaqtrader ftp server
    ftp = ftplib.FTP('ftp.nasdaqtrader.com', 'anonymous', 'user@domain.com')
    ftp.cwd('SymbolDirectory')
    ftp.retrbinary('RETR nasdaqtraded.txt', output_file.write)
    ftp.close()
    output_file.close()


def main():
    ''' Writes detailed stock symbol info to a file and simple symbols to
        another file (1 symbol per line)
    '''
    # Open raw_symbol_info file (from ftp.nasdaqtrader)
    in_name = 'raw_symbol_info.txt'
    get_symbols(in_name)
    raw_syms = open(in_name, 'r')

    # Open a new file to place common stock symbols in
    out_name = 'symbols.txt'
    common_stock_syms = open(out_name, 'w')
    out_string = '' # used to place all the symbols to be written to the file

    # Add every common stock into the new common_stock_symbols file
    for line in raw_syms:
        if line.find('Common Stock') != -1:
            out_string += line.split('|')[1] + '\n'
    raw_syms.close()
    common_stock_syms.write(out_string)
    common_stock_syms.close()


if __name__ == '__main__':
    main()
