# Creates table for all compiled stock data

USE stockdata;
CREATE TABLE compiled_data (
  ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  Stock_Symbol VARCHAR(8),
  Current_Price DECIMAL(12,2),
  PE_Ratio DECIMAL(12,2),
  PB_Ratio DECIMAL(12,2),
  PS_Ratio DECIMAL(12,2),
  50_DayMA DECIMAL(12,2),
  200_DayMA DECIMAL(12,2),
  Market_Cap DECIMAL(20,2),
  Book_Value DECIMAL(12,2),
  EBITDA DECIMAL(20,2),
  Dividend_Yield DECIMAL(12,2),
  Year_High DECIMAL(12,2),
  Year_Low DECIMAL(12,2),
  Datestamp DATE
);

CREATE INDEX symIndex on compiled_data (Stock_Symbol);
CREATE INDEX dateIndex on compiled_data (Datestamp);
