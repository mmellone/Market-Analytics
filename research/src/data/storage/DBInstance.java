package data.storage;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * Created by mitchell on 7/20/17.
 */
public enum DBInstance {
    STOCKDATA(Hostnames.STOCKDATA, "stockdata");

    private enum Hostnames {
        STOCKDATA("jdbc:mysql://localhost:3306/stockdata");

        private String hostname;

        Hostnames(String hostname) {
            this.hostname = hostname;
        }

        public String getHostname() {
            return hostname;
        }
    }
    private static final String JDBC_DRIVER_CLASS = "com.mysql.jdbc.Driver";
    private static final String DEFAULT_USERNAME = "root";
    private static final String DEFAULT_PASSWORD = "14jd3kpb";

    private Connection m_connection;

    DBInstance(Hostnames hostname, String dbName) {
        this(hostname, dbName, DEFAULT_USERNAME, DEFAULT_PASSWORD);
    }

    DBInstance(Hostnames hostname, String dbName, String username, String password) throws IllegalStateException {
        try {
            Class.forName(JDBC_DRIVER_CLASS);
            m_connection = DriverManager.getConnection(hostname.getHostname(), username, password);
            executeQuery("USE " + dbName + ";");
        } catch (SQLException e) {
            throw new IllegalStateException("Cannot connect to the database!", e);
        } catch (ClassNotFoundException e) {
            throw new IllegalStateException("Class not found: " + e.getMessage());
        }
        System.out.println("Connected");
    }

    /**
     * Executes a query and returns the ResultSet
     *
     * @param query The sql query statement
     * @return The ResultSet describing the data returned from the query
     */
    public ResultSet executeQuery(String query) {
        try {
            Statement stmt = m_connection.createStatement();
            return stmt.executeQuery(query);
        } catch (SQLException e) {
            throw new IllegalArgumentException("Cannot execute statement: " + e.getMessage());
        }
    }
}