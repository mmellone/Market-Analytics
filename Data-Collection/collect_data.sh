#!/bin/bash
# Use -gt 1 to consume two arguments per pass in the loop (e.g. each
# argument has a corresponding value to go with it).
# Use -gt 0 to consume one or more arguments per pass in the loop (e.g.
# some arguments don't have a corresponding value to go with it such
# as in the --default example).
# note: if this is set to -gt 0 the /etc/hosts part is not recognized ( may be a bug )

DATABASE="testing"
HOSTNAME="testing.cjoerkhofog8.us-west-2.rds.amazonaws.com"
USER="testinguser"
PASSWORD="password"
FLATFILE=""


while [[ $# -gt 1 ]]
do
key="$1"


case $key in
    -h|--help)
    echo "DATA COLLECTION SCRIPT"
    echo "Version 0.1.0"; echo;
    echo "Arguments are as follows:"
    echo "-d|--database: Name of database to use (on AWS cluster)"
    echo "-f|--flatfile: Path to the data flat-file to use (with .csv suffix)"
    echo "-u|--user: Database username"
    echo "-p|--password: Database password"
    echo; echo;
    # shift # past argument
    ;;
    -d|--database)
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
echo FLATFILE = "$FLATFILE"

# setup
python setup_db.py $HOSTNAME $USER $PASSWORD $DATABASE $FLATFILE

# This imports a csv file into aws rds
mysqlimport --local --compress --user=$USER --password=$PASSWORD --host=$HOSTNAME --fields-terminated-by='|' --ignore-lines=2 $DATABASE $FLATFILE
