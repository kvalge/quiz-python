from database.connect import connect


class Question:

    def __init__(self, content, rank, topic_name):
        self.content = content
        self.rank = rank
        self.topic_name = topic_name

        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO question VALUES "
            "(DEFAULT, '" + content + "', '" + rank + "', '" + topic_name + "')")
        cur.connection.commit()
        cur.close()
