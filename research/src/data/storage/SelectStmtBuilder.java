package data.storage;

import java.util.LinkedList;
import java.util.List;

/**
 * Builds a select statement
 */
public class SelectStmtBuilder implements StmtBuilder {
    private String table;
    private List<String> columns;
    private List<String> conditions; // TODO add support for multiple conditions

    /**
     * Constructs a select statement builder
     *
     * @param table The name of the table to query
     */
    public SelectStmtBuilder(String table) {
        this.table = table;
        this.columns = new LinkedList<>();
        this.conditions = new LinkedList<>();
    }

    /**
     * Adds a column to return in the query
     *
     * @param colName The name of the column (surrounded by '' if it contains a space)
     */
    public void addColumn(String colName) {
        columns.add(colName);
    }

    /**
     * Adds a check for similarity of the substring in the column
     *
     * @param column The name of the column to use (surrounded by `` if it contains a space)
     * @param substring The substring to match
     */
    public void addSimilarCondition(String column, String substring) {
        // todo add `` automatically
        conditions.add(column + " like '%" + substring + "%'");
    }

    @Override
    public String getStatement() {
        StringBuilder stmt = new StringBuilder();
        stmt.append("SELECT ");
        if (columns.isEmpty()) {
            stmt.append("*");
        } else {
            stmt.append(String.join(", ", columns));
        }
        stmt.append(" FROM ");
        stmt.append(table);
        if (!conditions.isEmpty()) {
            stmt.append(" WHERE ");
            stmt.append(conditions.get(0)); // only works for a single condition now
        }
        stmt.append(";");
        return stmt.toString();
    }
}
