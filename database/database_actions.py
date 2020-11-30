from database.login import Login_Database

login_database = Login_Database('dota_heroes')


def get_connection():
    conn = login_database.conn

    return conn


def get_cursor():
    cursor = login_database.conn.cursor()

    return cursor


def update_query(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query)

    cursor.close()
    conn.commit()


def execute_query(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()

    return result
