from database.connect import connect
from database.create_table import create_tables


class Topic:

    def __init__(self, name):
        self.name = name

        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO topic VALUES (DEFAULT, '" + name + "')")
        cur.connection.commit()
        cur.close()


if __name__ == '__main__':
    create_tables()
    history = Topic("History")
    music = Topic("Music")
    cinema = Topic("Cinema")
    philosophy = Topic("Philosophy")
