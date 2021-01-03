import pyodbc
import random
con_string = 'driver=MySQL ODBC 5.3 Unicode Driver;server=192.168.9.10;database=testdb;uid=test1;pwd=test123'

def create_table():
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
            create table person(
              id int PRIMARY KEY AUTO_INCREMENT,
              gender char(1),
              weight float,
              height float
            )
        """
        con.execute(sql_cmd)

def insert_data():
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
           insert into person(gender, weight, height) VALUES('M', 54, 180)
        """
        con.execute(sql_cmd)

def insert_data2(params): # params -> tuple, list
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
           insert into person(gender, weight, height) VALUES(?, ?, ?)
        """
        con.execute(sql_cmd, params)

def execute_non_query(sql_cmd, con_string, params=None):
    with pyodbc.connect(con_string) as con:
        if params:
            con.execute(sql_cmd, params)
        else:
            con.execute(sql_cmd)

def select_data():
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
            select * from person;
         """
        for row in con.execute(sql_cmd):
            print(row)
            # print(row[2], row[3])

def create_data():
    sql_cmd = """
               insert into person(gender, weight, height) VALUES(?, ?, ?)
            """
    for _ in range(10):
        execute_non_query(sql_cmd, con_string, (random.choice('MF'), random.normalvariate(48, 6), random.normalvariate(165, 7)))
        # insert_data2((random.choice('MF'), random.normalvariate(48, 6), random.normalvariate(165, 7)))

if __name__ == '__main__':
    # create_table()
    # insert_data2(('F', 45, 175))
    # create_data()
    # execute_non_query('update person set weight = weight * 2.2', con_string)
    # execute_non_query('delete from person where height < 170', con_string)
    execute_non_query('delete from person where height < ?', con_string, [175])
    select_data()