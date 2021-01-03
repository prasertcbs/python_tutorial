# CRUD (Create/Insert, Read/Select, Update, Delete)
import random
import sqlite3
def create_db():
    with sqlite3.connect("basic.sqlite") as con:
        sql_cmd = """
            create table person(
              id integer PRIMARY KEY AUTOINCREMENT,
              gender text,
              weight real,
              height real
            )
        """
        con.execute(sql_cmd)

def insert_demo():
    with sqlite3.connect("basic.sqlite") as con:
        sql_cmd = """
            insert into person(gender, weight, height) values('F', 45, 160);
        """
        con.execute(sql_cmd)
def insert_demo2(params):
    with sqlite3.connect("basic.sqlite") as con:
        sql_cmd = """
            insert into person(gender, weight, height) values(?, ?, ?);
        """
        con.execute(sql_cmd, params)
def update_demo():
    with sqlite3.connect("basic.sqlite") as con:
        sql_cmd = """
            update person set weight = weight * 2.2
        """
        con.execute(sql_cmd)
def delete_demo():
    with sqlite3.connect("basic.sqlite") as con:
        sql_cmd = """
            delete from person where gender = 'M'
        """
        con.execute(sql_cmd)
def select_demo():
    with sqlite3.connect("basic.sqlite") as con:
        sql_cmd = """
            select * from person
        """
        for row in con.execute(sql_cmd):
            print(row)


if __name__ == '__main__':
    # create_db()
    # insert_demo()
    # insert_demo2(('M', 70, 170))
    # for _ in range(10):
    #     g = random.choice('MF')
    #     w = random.randrange(35, 80)
    #     h = random.randrange(135, 180)
    #     insert_demo2((g, w, h))
    # update_demo()
    delete_demo()
    select_demo()