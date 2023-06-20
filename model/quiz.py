from database.connect import connect


class Quiz:

    def __init__(self, name):
        self.name = name

        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO quiz VALUES (DEFAULT, '" + name + "') ON CONFLICT DO NOTHING")
        cur.connection.commit()
        cur.close()
