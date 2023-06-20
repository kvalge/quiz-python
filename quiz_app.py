from database.connect import connect
from database.create_table import create_tables
from model.topic import Topic
from model.question import Question
from model.response import Response
from model.quiz import Quiz


def add_question_to_quiz(quiz_name, question_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO quiz_question VALUES "
                "(DEFAULT, '" + quiz_name + "', '" + question_name + "') ON CONFLICT DO NOTHING")
    cur.connection.commit()
    cur.close()


if __name__ == '__main__':
    create_tables()

    history = Topic("History")
    music = Topic("Music")
    cinema = Topic("Cinema")
    philosophy = Topic("Philosophy")

    q1 = Question("q1",
                  "Which country was known as Rhodesia before gaining independence from the British in 1979?",
                  "1",
                  "History")
    q2 = Question("q2",
                  "Which country was unified by Giuseppe Garibaldi in 1851?",
                  "3",
                  "History")
    q3 = Question("q3",
                  "Which President was brought down by the Watergate Scandal?",
                  "3",
                  "History")
    q4 = Question("q4",
                  "Who directed Lost in Translation?",
                  "1",
                  "Cinema")

    r1q1 = Response("India", "False", "q1")
    r2q1 = Response("Zimbabwe", "True", "q1")
    r3q1 = Response("Sierra-Leone", "False", "q1")
    r1q2 = Response("Spain", "False", "q2")
    r2q2 = Response("Switzerland", "False", "q2")
    r3q2 = Response("Italy", "True", "q2")
    r1q3 = Response("Richard M. Nixon", "True", "q3")
    r2q3 = Response("George W. Bush", "False", "q3")
    r3q3 = Response("John F. Kennedy", "False", "q3")
    r1q4 = Response("Jodie Foster", "False", "q4")
    r2q4 = Response("Sally Potter", "False", "q4")
    r3q4 = Response("Sofia Coppola", "True", "q4")

    history_quiz = Quiz("History quiz")
    cinema_quiz = Quiz("Cinema quiz")

    add_question_to_quiz(history_quiz.name, q1.name)
    add_question_to_quiz(history_quiz.name, q2.name)
    add_question_to_quiz(history_quiz.name, q3.name)
    add_question_to_quiz(cinema_quiz.name, q4.name)
