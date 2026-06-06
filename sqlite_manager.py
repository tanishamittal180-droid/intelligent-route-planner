import sqlite3


class DatabaseManager:

    def __init__(self):

        self.conn = sqlite3.connect(
            "routes.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS routes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            source TEXT,

            destination TEXT,

            algorithm TEXT,

            distance REAL,

            eta REAL
        )
        """)

        self.conn.commit()

    def save_route(
        self,
        source,
        destination,
        algorithm,
        distance,
        eta
    ):

        self.cursor.execute("""

        INSERT INTO routes(
        source,
        destination,
        algorithm,
        distance,
        eta
        )

        VALUES(?,?,?,?,?)

        """,

        (
            source,
            destination,
            algorithm,
            distance,
            eta
        ))

        self.conn.commit()

    def get_routes(self):

        self.cursor.execute(
            "SELECT * FROM routes"
        )

        return self.cursor.fetchall()