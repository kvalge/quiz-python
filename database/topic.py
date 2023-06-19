import psycopg2
from database.config import config


class Topic:

    def __init__(self, name):
        self.name = name

        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("INSERT INTO topic VALUES (DEFAULT, '" + name + "')")
        cur.connection.commit()
        cur.close()


if __name__ == '__main__':
    history = Topic("History")
    music = Topic("Music")
