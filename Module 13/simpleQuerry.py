"""Program: driver
Author: Dylan Kennedy
Last date modified: 04/19/2021

The purpose of this program is to create an sql database and store python
obhects to a student and person table."""

import sqlite3
from sqlite3 import Error


def create_connection(db):
    """Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""

    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_tables(conn):
    """Create the person and student table
    :param conn sql database connection
    :returns none."""

    personTable = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    studentTable = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text default ENROLLED,
                                );"""
    try:
        cur = conn.cursor()
        cur.execute(personTable)
        cur.execute(studentTable)

    except Error as e:
        print(e)


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id"""

    statement = """INSERT INTO person(firstname,lastname)
              VALUES(?,?)"""
    cur = conn.cursor()
    cur.execute(statement, person)
    return cur.lastrowid


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return rows all rows in the person table"""

    query = """SELECT * FROM person"""
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    return rows


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id"""

    statement = """INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?)"""
    cur = conn.cursor()  # cursor object
    cur.execute(statement, student)


def select_all_students(conn):
    """Query all row in students table
    :param conn the connect object
    :return rows all rows in the student table."""

    query = """SELECT * FROM student"""
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    return rows


if __name__ == '__main__':
    conn = create_connection('people.db')
    create_tables(conn)

    with conn:
        person = ('Rob', 'Thomas')
        id = create_person(conn, person)
        student = (id, 'Songwriting', '2000-01-01')
        studentID = create_student(conn, student)

    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            print(row)

        rows = select_all_students(conn)
        for row in rows:
            print(row)
