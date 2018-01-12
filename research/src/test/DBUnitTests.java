package test;

import data.storage.DBInstance;
import org.junit.jupiter.api.Test;

class DBUnitTests {

    @Test
    void testSymbolsConnection() {
        DBInstance db = DBInstance.STOCKDATA;
    }
}
