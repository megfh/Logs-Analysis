#! /usr/bin/env
# Udacity Full Stack Nanodegree Project: Logs Analysis

import psycopg2
import calendar
import time


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


q1_SQL = "select * from ArticleCount limit 3;"


def question1():
    conn = connect()
    cur = conn.cursor()
    cur.execute(q1_SQL)

    for record in cur:
        title = record[0]
        views = record[1]
        print('"%s" - %d views' % (title, views))

    cur.close()
    conn.close()
    return


q2_SQL = """select authorsWork.name, sum(ArticleCount.count) from ArticleCount
         inner join authorsWork on ArticleCount.title=authorsWork.title group
         by authorsWork.name order by sum desc;"""


def question2():
    conn = connect()
    cur = conn.cursor()
    cur.execute(q2_SQL)

    for record in cur:
        name = record[0]
        views = record[1]
        print("%s - %d views" % (name, views))

    cur.close()
    conn.close()
    return


q3_SQL = 'select * from percentError where percent_error>1;'


def question3():
    conn = connect()
    cur = conn.cursor()
    cur.execute(q3_SQL)

    for record in cur:
        month = calendar.month_name[int(record[0])]
        day = int(record[1])
        year = int(record[2])
        percent = record[3]

        print("%s %d, %d - %.1f%% errors " % (month, day, year, percent))

    cur.close()
    conn.close()
    return


print("\nReport generated on %s at %s" % (time.strftime("%d/%m/%Y"),
      time.strftime("%H:%M:%S")))

print("\nThe three most popular articles of all time are:")
question1()

print("\nThe most popular article authors of all time are:")
question2()

print("\nDay(s) when more than 1%s of server requests lead to errors:" % ("%"))
question3()

print("\n")
