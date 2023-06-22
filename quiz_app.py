from database.connect import connect
from database.create_table import create_tables

from model.topic import Topic
from model.question import Question
from model.response import Response
from model.quiz import Quiz

import pandas as pd


def add_question_to_quiz(quiz_name, question_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO quiz_question VALUES "
                "(DEFAULT, '" + quiz_name + "', '" + question_name + "') ON CONFLICT DO NOTHING")
    cur.connection.commit()
    cur.close()


def get_question_by_topic(topic_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM question WHERE topic_name = '" + topic_name + "'")
    questions = cur.fetchall()
    for row in questions:
        print("{}: {}".format(topic_name, row[2]))

    cur.connection.commit()
    cur.close()


def get_questions_by_quiz(quiz_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT quiz_question.quiz_name, question.name "
                "FROM quiz_question "
                "INNER JOIN question "
                "ON quiz_question.question_name = question.name "
                "WHERE quiz_question.quiz_name = '" + quiz_name + "'")
    questions = cur.fetchall()
    for row in questions:
        print("{}: {}".format(quiz_name, row[1]))

    cur.connection.commit()
    cur.close()


if __name__ == '__main__':
    create_tables()

    history = Topic("History")
    music = Topic("Music")
    cinema = Topic("Cinema")
    philosophy = Topic("Philosophy")

    dataframe = pd.read_excel('data.xlsx')
    print(dataframe)

    q1 = Question("q1",
                  "{}".format(dataframe.get("question_content")[0]),
                  "1",
                  "History")
    q2 = Question("q2",
                  "{}".format(dataframe.get("question_content")[3]),
                  "3",
                  "History")
    q3 = Question("q3",
                  "{}".format(dataframe.get("question_content")[6]),
                  "3",
                  "History")
    q4 = Question("q4",
                  "{}".format(dataframe.get("question_content")[9]),
                  "1",
                  "Cinema")

    r1q1 = Response("{}".format(dataframe.get("response_content")[0]), "False", "q1")
    r2q1 = Response("{}".format(dataframe.get("response_content")[1]), "True", "q1")
    r3q1 = Response("{}".format(dataframe.get("response_content")[2]), "False", "q1")
    r1q2 = Response("{}".format(dataframe.get("response_content")[3]), "False", "q2")
    r2q2 = Response("{}".format(dataframe.get("response_content")[4]), "False", "q2")
    r3q2 = Response("{}".format(dataframe.get("response_content")[5]), "True", "q2")
    r1q3 = Response("{}".format(dataframe.get("response_content")[6]), "True", "q3")
    r2q3 = Response("{}".format(dataframe.get("response_content")[7]), "False", "q3")
    r3q3 = Response("{}".format(dataframe.get("response_content")[8]), "False", "q3")
    r1q4 = Response("{}".format(dataframe.get("response_content")[9]), "False", "q4")
    r2q4 = Response("{}".format(dataframe.get("response_content")[10]), "False", "q4")
    r3q4 = Response("{}".format(dataframe.get("response_content")[11]), "True", "q4")

    history_quiz = Quiz("History quiz")
    cinema_quiz = Quiz("Cinema quiz")

    add_question_to_quiz(history_quiz.name, q1.name)
    add_question_to_quiz(history_quiz.name, q2.name)
    add_question_to_quiz(history_quiz.name, q3.name)
    add_question_to_quiz(cinema_quiz.name, q4.name)

    get_question_by_topic(history.name)

    get_questions_by_quiz(history_quiz.name)

