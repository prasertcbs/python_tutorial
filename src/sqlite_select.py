import sqlite3

def demo_select1():
    try:
        with sqlite3.connect("db.sqlite") as con:
            con.row_factory = sqlite3.Row
            sql_cmd = """
            select * from person where gender = 'M'
            """
            cursor = con.execute(sql_cmd)
            for row in cursor:
                print("{} {} {} {}".format(row["obs"], row["gender"], row["height"], row["weight"]))
    except Exception as e:
        print('Error -> {}'.format(e))

def demo_select2(sex:str, h):
    try:
        with sqlite3.connect("db.sqlite") as con:
            con.row_factory = sqlite3.Row
            sql_cmd = """
            select * from person 
              where gender = ? and height > ?
            """
            # cursor = con.execute(sql_cmd, [sex, h])
            # cursor = con.execute(sql_cmd, (sex, h))
            # cursor = con.execute(sql_cmd, ('M', 180))
            # for row in cursor:
            for row in con.execute(sql_cmd, ('M', 180)):
                print("{} {} {} {}".format(row["obs"], row["gender"], row["height"], row["weight"]))
    except Exception as e:
        print('Error -> {}'.format(e))

if __name__ == '__main__':
    # demo_select1()
    demo_select2('F', 180)