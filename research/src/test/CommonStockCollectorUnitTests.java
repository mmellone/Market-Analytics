package test;

import data.collectors.CommonStockCollector;
import org.junit.jupiter.api.Test;

import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertTrue;

class CommonStockCollectorUnitTests {

    @Test
    void getSymbolsTest() {
        CommonStockCollector csc = new CommonStockCollector();
        Set<String> symbols = csc.getSymbols();
        System.out.println("Total Number of Symbols: " + symbols.size());
        assertTrue(symbols.contains("AAPL"));
    }
}
