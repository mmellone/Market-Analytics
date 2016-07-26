#!/bin/bash
# Use -gt 1 to consume two arguments per pass in the loop (e.g. each
# argument has a corresponding value to go with it).
# Use -gt 0 to consume one or more arguments per pass in the loop (e.g.
# some arguments don't have a corresponding value to go with it such
# as in the --default example).
# note: if this is set to -gt 0 the /etc/hosts part is not recognized ( may be a bug )

DATABASE=""
HOSTNAME=""
USER=""
PASSWORD=""
FLATFILE=""
SCRAPE_DATA=false


while [[ $# -gt 1 ]] # ??? not sure what this does, must test
do
key="$1"


case $key in
    -h|--help)
    echo "DATA COLLECTION SCRIPT"
    echo "Version 0.2.0"; echo;
    echo "Arguments are as follows:"
    echo "-d|--database: Name of database to use (on AWS cluster)"
    echo "-f|--flatfile: Path to the data flat-file to use (with .csv suffix)"
    echo "-u|--user: Database username"
    echo "-p|--password: Database password"
    echo "-D|--getdata: (no parameters) Tells the script to scrape stock data from yahoo finance"
    echo; echo;
    # shift # past argument
    ;;
    -d|--database)
    DATABASE="$2"
    if [ "$2" = "testing" ]; then
      HOSTNAME="testing.cjoerkhofog8.us-west-2.rds.amazonaws.com"
      USER="testinguser"
    elif [ "$2" = "stockdata" ]; then
      HOSTNAME="stockdata.cjoerkhofog8.us-west-2.rds.amazonaws.com"
      USER="stockdatauser"
    fi
    DATABASE="$2"
    shift # past argument
    ;;
    -f|--flatfile)
    FLATFILE="$2"
    shift # past argument
    ;;
    -u|--user)
    USER="$2"
    shift
    ;;
    -p|--password)
    PASSWORD="$2"
    shift
    ;;
    -D|--getdata)
    SCRAPE_DATA=true
    shift
    ;;
    --default)
    DEFAULT=YES
    ;;
    *)
            # unknown option
    ;;
esac
shift # past argument or value
done

echo DATABASE  = "$DATABASE"
echo USER = "$USER"
echo PASSWORD = "$PASSWORD"

if [ "$SCRAPE_DATA" = true ]; then
  echo Getting list of all stock symbols
  python symbol_list.py
  echo Scraping financial data from yahoo
  FLATFILE="$(python yahoo_data_scraper.py )"
fi

echo FLATFILE = "$FLATFILE"

# setup
python setup_db.py $HOSTNAME $USER $PASSWORD $DATABASE $FLATFILE

# This imports a csv file into aws rds
mysqlimport --local --compress --user=$USER --password=$PASSWORD --host=$HOSTNAME --fields-terminated-by='|' --ignore-lines=2 $DATABASE $FLATFILE
