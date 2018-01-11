package test;

import data.storage.SelectStmtBuilder;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class StmtBuilderUnitTests {

    @Test
    void testSelectStmtBuilderNoColumn() {
        SelectStmtBuilder ssb = new SelectStmtBuilder("table_name");
        assertEquals("SELECT * FROM table_name;", ssb.getStatement());
    }

    @Test
    void testSelectStmtBuilderSingleColumn() {
        SelectStmtBuilder ssb = new SelectStmtBuilder("table_name");
        ssb.addColumn("col1");
        assertEquals("SELECT col1 FROM table_name;", ssb.getStatement());
    }

    @Test
    void testSelectStmtBuilderMultipleColumn() {
        SelectStmtBuilder ssb = new SelectStmtBuilder("table_name");
        ssb.addColumn("col1");
        ssb.addColumn("'column two'");
        assertEquals("SELECT col1, 'column two' FROM table_name;", ssb.getStatement());
    }

    @Test
    void testSelectStmtBuilderSimilarCond() {
        SelectStmtBuilder ssb = new SelectStmtBuilder("table_name");
        ssb.addColumn("col1");
        ssb.addSimilarCondition("'cond col'", "sub");
        assertEquals("SELECT col1 FROM table_name WHERE 'cond col' like '%sub%';", ssb.getStatement());
    }
}
