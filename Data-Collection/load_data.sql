# Loads data from dailystockdata.csv file in working directory into compiled_data table

USE stockdata;

LOAD DATA LOCAL INFILE 'dailystockdata.csv'
INTO TABLE compiled_data
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 2 LINES;
