import pyodbc


def execute_query(sql_cmd, con_string, params=None):
    try:
        with pyodbc.connect(con_string) as con:
            if params:
                return con.execute(sql_cmd, params)
            else:
                return con.execute(sql_cmd)
    except Exception as e:
        print(f'error -> {e}')


if __name__ == '__main__':
    # f-string (string interpolation Python 3.6
    driver = 'MySQL ODBC 5.3 Unicode Driver'
    host = '192.168.9.10'
    db = 'world'
    username = 'test1'
    password = 'test123'
    con_string = f'driver={driver};server={host};database={db};uid={username};pwd={password}'
    # cursor = execute_query('select * from city where population > 1000000 limit 10', con_string)
    cursor = execute_query(
        'SELECT * FROM city WHERE population > ?  AND population < ? ORDER BY population DESC LIMIT 10',
        con_string, [1000000, 5000000])
    for row in cursor:
        print(row)
