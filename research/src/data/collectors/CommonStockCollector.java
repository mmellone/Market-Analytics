package data.collectors;

import data.storage.DBInstance;
import data.storage.SelectStmtBuilder;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashSet;
import java.util.Set;

public class CommonStockCollector {
    private final static String SYMBOL_COL = "Symbol";
    private final static String SYMBOL_TABLE = "SYMBOLS";

    /**
     * Gets all common stock symbols from SQL database
     *
     * @return Set of all symbols
     */
    public Set<String> getSymbols() {
        DBInstance stockdataDB = DBInstance.STOCKDATA;

        SelectStmtBuilder ssb = new SelectStmtBuilder(SYMBOL_TABLE);
        ssb.addColumn(SYMBOL_COL);
        ssb.addSimilarCondition("`Security Name`", "Common Stock");
        Set<String> symbols = new HashSet<>();

        try {
            ResultSet rs = stockdataDB.executeQuery(ssb.getStatement());
            while (rs.next()) {
                String sym = rs.getString(SYMBOL_COL);
                symbols.add(sym);
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Could not execute getSymbol query: " + e.getMessage());
        }

        return symbols;
    }
}
