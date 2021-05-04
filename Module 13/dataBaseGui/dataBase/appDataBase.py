import sqlite3
from sqlite3 import Error


class AppDataBase:
    def __init__(self, file):
        self.__conn = None
        self.__cur = None

        __personTable = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

        __studentTable = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    firstName text NOT NULL,
                                    lastName text NOT NULL,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text default ENROLLED
                                );"""

        try:
            self.__conn = sqlite3.connect(file)
            self.__cur = self.__conn.cursor()
            self.__cur.execute(__studentTable)
            self.__cur.execute(__personTable)

        except Error as e:
            print(e)
            return None

    def select_all_students(self):
        query = """SELECT * FROM student"""
        with self.__conn:
            self.__cur.execute(query)
            return self.__cur.fetchall()

    def create_student(self, firstName, lastName, major, startDate):
        statement = """INSERT INTO student(firstname, lastname, major, begin_date)
                        VALUES(?,?,?,?)"""
        student = (firstName, lastName, major, startDate)
        with self.__conn:

            self.__cur.execute(statement, student)
        return f"{firstName} {lastName} has a major of {major} and started {startDate}"

    def select_all_persons(self):
        query = """SELECT * FROM person"""
        with self.__conn:
            self.__cur.execute(query)
            return self.__cur.fetchall()

    def create_person(self, firstName, lastName):
        statement = """INSERT INTO person(firstname, lastname)
                    VALUES(?,?)"""
        person = (firstName, lastName)

        with self.__conn:
            self.__cur.execute(statement, person)

        return f"{firstName} {lastName}"
