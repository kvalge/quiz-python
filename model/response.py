from database.connect import connect


class Response:

    def __init__(self, content, correct, question_name: str):
        self.content = content
        self.correct = correct
        self.question_name = question_name

        conn = connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO response VALUES "
            "(DEFAULT, '" + content + "', '" + correct + "', '" + question_name + "') ON CONFLICT DO NOTHING")
        cur.connection.commit()
        cur.close()
