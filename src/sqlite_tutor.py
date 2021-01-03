import sqlite3

def demo_select():
    try:
        with sqlite3.connect("db.sqlite") as con:
            con.row_factory = sqlite3.Row
            # sql_cmd = "select * from person"
            sql_cmd = """
            select gender, height, weight, 
                  weight / ((height / 100) * (height / 100)) as bmi
                from person
                where gender = 'F' and bmi < 25
            """
            for row in con.execute(sql_cmd):
                # print(row)
                # print(row[1], row[2])
                print(row["gender"], row["height"], row["bmi"])
    except Exception as e:
        print('Error -> {}'.format(e))

def demo_select2():
    with sqlite3.connect("db.sqlite") as con:
        con.row_factory = sqlite3.Row
        sql_cmd = "select * from person2"
        for row in con.execute(sql_cmd):
            # print(row)
            # print(row[1], row[2])
            print(row["gender"], row["height"])

if __name__ == '__main__':
    demo_select()