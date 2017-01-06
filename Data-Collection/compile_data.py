import sys
import MySQLdb as sql

def main():
    ''' Places 
        arg1 = hostname of database
        arg2 = username
        arg3 = password for user
        arg4 = name of database
        arg5 = input file (.csv, should have column names as first row, types second row)
    '''
    db = sql.connect(host=sys.argv[1], user=sys.argv[2],
                     passwd=sys.argv[3], db=sys.argv[4])
    cursor = db.cursor()
    cursor.execute('USE %s;' % sys.argv[4])
    tablename = sys.argv[5].split('.')[0]
    make_table = 'CREATE TABLE %s (' % tablename
    with open(sys.argv[5], 'r') as data:
        cols = data.readline().strip().split('|')
        types = data.readline().strip().split('|')
        for i, (c, t) in enumerate(zip(cols, types)):
            make_table += c + ' ' + t
            if i != len(cols)-1:
                make_table += ', '
            else:
                make_table += ');'
    print make_table
    cursor.execute(make_table)

if __name__ == '__main__':
    main()
