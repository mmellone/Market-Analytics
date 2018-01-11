package test;

import data.storage.DBInstance;
import org.junit.jupiter.api.Test;

class DBUnitTests {

    @Test
    public void testSymbolsConnection() {
        DBInstance db = DBInstance.STOCKDATA;
    }
}
