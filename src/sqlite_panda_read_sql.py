import sqlite3
import random
import pandas as pd
import matplotlib.pyplot as plt


def create_table(db):
    try:
        with sqlite3.connect(db) as con:
            sql_cmd = '''
             DROP TABLE IF EXISTS person;
             CREATE TABLE person(
                 obs INTEGER PRIMARY KEY AUTOINCREMENT,
                 gender TEXT,
                 weight REAL,
                 height REAL);
             '''
            con.executescript(sql_cmd)
    except Exception as e:
        print('Error -> {}'.format(e))


def create_data(db, rows=10):
    data = [(
        random.choice('MF'),
        random.normalvariate(57, 4.5),
        random.normalvariate(160, 6),
    ) for _ in range(rows)]
    print(data)
    try:
        with sqlite3.connect(db) as con:
            sql_cmd = 'INSERT INTO person(gender, weight, height) VALUES (?, ?, ?);'
            con.executemany(sql_cmd, data)
    except Exception as e:
        print('Error -> {}'.format(e))


def pd_read_sql(db):
    with sqlite3.connect(db) as con:
        sql_cmd = '''
          SELECT obs, gender, weight, height 
            FROM person 
            ORDER BY height'''
        df = pd.read_sql(sql_cmd,
                         con, index_col='obs')
    print(df)
    df['bmi'] = df.weight / (df.height / 100) ** 2
    # df['height'].plot.hist(alpha=.7)
    # df.plot.bar(x=df.index, y='weight')
    df.plot.scatter(x='weight', y='height')
    print(f'mean(bmi) = {df.bmi.mean():.2f}')  # f-string in Python 3.6 (php: variable substitution, c#: string interpolation
    plt.show()


if __name__ == '__main__':
    db = 'sample.sqlite'
    create_table(db)
    create_data(db, 100)
    pd_read_sql(db)
