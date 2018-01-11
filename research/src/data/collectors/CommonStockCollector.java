package data.collectors;

import data.storage.DBInstance;

import java.util.Set;

public class CommonStockCollector {
    /**
     * Gets all common stock symbols from SQL database
     *
     * @return Set of all symbols
     */
    private Set<String> getSymbols() {
        DBInstance stockdataDB = DBInstance.STOCKDATA;



//        stockdataDB.executeQuery();
        return null;
    }
}
