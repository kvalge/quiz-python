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

    q1 = Question("{}".format(dataframe.get("question_name")[0]),
                  "{}".format(dataframe.get("question_content")[0]),
                  "{}".format(dataframe.get("question_rank")[0]),
                  "{}".format(dataframe.get("topic")[0]))
    q2 = Question("{}".format(dataframe.get("question_name")[3]),
                  "{}".format(dataframe.get("question_content")[3]),
                  "{}".format(dataframe.get("question_rank")[3]),
                  "{}".format(dataframe.get("topic")[3]))
    q3 = Question("{}".format(dataframe.get("question_name")[6]),
                  "{}".format(dataframe.get("question_content")[6]),
                  "{}".format(dataframe.get("question_rank")[6]),
                  "{}".format(dataframe.get("topic")[6]))
    q4 = Question("{}".format(dataframe.get("question_name")[9]),
                  "{}".format(dataframe.get("question_content")[9]),
                  "{}".format(dataframe.get("question_rank")[9]),
                  "{}".format(dataframe.get("topic")[9]))

    r1q1 = Response("{}".format(dataframe.get("response_content")[0]),
                    "{}".format(dataframe.get("response_correct")[0]),
                    "{}".format(dataframe.get("question_name")[0]))
    r2q1 = Response("{}".format(dataframe.get("response_content")[1]),
                    "{}".format(dataframe.get("response_correct")[1]),
                    "{}".format(dataframe.get("question_name")[1]))
    r3q1 = Response("{}".format(dataframe.get("response_content")[2]),
                    "{}".format(dataframe.get("response_correct")[2]),
                    "{}".format(dataframe.get("question_name")[2]))
    r1q2 = Response("{}".format(dataframe.get("response_content")[3]),
                    "{}".format(dataframe.get("response_correct")[3]),
                    "{}".format(dataframe.get("question_name")[3]))
    r2q2 = Response("{}".format(dataframe.get("response_content")[4]),
                    "{}".format(dataframe.get("response_correct")[4]),
                    "{}".format(dataframe.get("question_name")[4]))
    r3q2 = Response("{}".format(dataframe.get("response_content")[5]),
                    "{}".format(dataframe.get("response_correct")[5]),
                    "{}".format(dataframe.get("question_name")[5]))
    r1q3 = Response("{}".format(dataframe.get("response_content")[6]),
                    "{}".format(dataframe.get("response_correct")[6]),
                    "{}".format(dataframe.get("question_name")[6]))
    r2q3 = Response("{}".format(dataframe.get("response_content")[7]),
                    "{}".format(dataframe.get("response_correct")[7]),
                    "{}".format(dataframe.get("question_name")[7]))
    r3q3 = Response("{}".format(dataframe.get("response_content")[8]),
                    "{}".format(dataframe.get("response_correct")[8]),
                    "{}".format(dataframe.get("question_name")[8]))
    r1q4 = Response("{}".format(dataframe.get("response_content")[9]),
                    "{}".format(dataframe.get("response_correct")[9]),
                    "{}".format(dataframe.get("question_name")[9]))
    r2q4 = Response("{}".format(dataframe.get("response_content")[10]),
                    "{}".format(dataframe.get("response_correct")[10]),
                    "{}".format(dataframe.get("question_name")[10]))
    r3q4 = Response("{}".format(dataframe.get("response_content")[11]),
                    "{}".format(dataframe.get("response_correct")[11]),
                    "{}".format(dataframe.get("question_name")[11]))

    history_quiz = Quiz("History quiz")
    cinema_quiz = Quiz("Cinema quiz")

    add_question_to_quiz(history_quiz.name, q1.name)
    add_question_to_quiz(history_quiz.name, q2.name)
    add_question_to_quiz(history_quiz.name, q3.name)
    add_question_to_quiz(cinema_quiz.name, q4.name)

    get_question_by_topic(history.name)

    get_questions_by_quiz(history_quiz.name)

