from database.connect import connect


class Topic:

    def __init__(self, name):
        self.name = name

        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO topic VALUES (DEFAULT, '" + name + "') ON CONFLICT DO NOTHING")
        cur.connection.commit()
        cur.close()
