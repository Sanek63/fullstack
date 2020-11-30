import psycopg2
import database.config as config


class Login_Database:

    def __init__(self, name):
        self.dbname = name
        self.conn = psycopg2.connect(
            host="127.0.0.1",
            database=self.dbname,
            user="postgres",
            password="postgres"
        )
        self.cursor = self.conn.cursor()
        self.check_table(config.TABLE_NAME)

    def check_table(self, name_table):
        if self.is_table(name_table):
            pass
        else:
            self.cursor.execute(f"CREATE TABLE {name_table}("
                                f"id INT PRIMARY KEY,"
                                f"Name VARCHAR(30),"
                                f"Health INT(5),"
                                f"Damage INT(4),"
                                f"Mana INT(5),"
                                f"Attribute VARCHAR(15))"
                                )
            self.conn.commit()
            self.cursor.close()

    # checking for table available
    def is_table(self, table_name):
        query = f"SELECT * from information_schema.tables WHERE table_name='{table_name}';"
        cur = self.conn.cursor()
        cur.execute(query)
        result = bool(cur.rowcount)

        return result
