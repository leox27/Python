import sqlite3

class Database:
    def __init__(self, db_name="bank.db"):
        """Initialize the database connection and create the table."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the accounts table if it does not exist."""
        query = """
        CREATE TABLE IF NOT EXISTS accounts (
            account_number TEXT PRIMARY KEY,
            customer_name TEXT NOT NULL,
            balance REAL NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def execute_query(self, query, params=()):
        """Execute a query that modifies data (INSERT, UPDATE, DELETE)."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def fetch_one(self, query, params=()):
        """Fetch a single record from the database."""
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetch_all(self, query):
        """Fetch all records from the database."""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()