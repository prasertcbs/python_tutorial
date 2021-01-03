import pyodbc # pip install pyodbc
import os

con_string = 'driver=MySQL ODBC 5.3 Unicode Driver;server=192.168.9.10;database=testdb;uid=test1;pwd=test123'


def create_table():
    # tinyblob  : 255 characters
    # blob      : 64KB
    # mediumblob: 16MB
    # longblob  :  4GB
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
            CREATE TABLE media(
              id INT PRIMARY KEY AUTO_INCREMENT,
              descr VARCHAR(255),
              filetype VARCHAR(30),
              stream MEDIUMBLOB
            )
        """
        con.execute(sql_cmd)


def insert_data(params):
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
           INSERT INTO media(descr, filetype, stream) VALUES(?, ?, ?)
        """
        con.execute(sql_cmd, params)


def select_data(params, outfile=None):
    with pyodbc.connect(con_string) as con:
        sql_cmd = """
            SELECT stream, descr, filetype FROM media WHERE id = ?;
         """
        for row in con.execute(sql_cmd, params):
            if not (outfile):
                outfile = f'{row[1]}.{row[2]}'
            write_bin(outfile, row[0])


def read_bin(filename):
    with open(filename, mode='rb') as f:
        return f.read()


def write_bin(filename, data):
    with open(filename, mode='wb') as f:
        f.write(data)


def filename_ext(fullpath):
    # fullpath = r'Z:\prasert\Dropbox\PycharmProjects\mssql_mysql_tutor\product\mic.png'
    basename = os.path.basename(fullpath)  # return filename.ext (no path)
    filename, ext = os.path.splitext(basename)
    # print(f'filename = # filename}, ext = {ext}')
    return filename, ext[1:]


def insert_files_in_folder(folder, ext_filter):
    for basename in os.listdir(folder):
        if basename.endswith('.' + ext_filter):
            filename, ext = os.path.splitext(basename)
            # print(filename, ext[1:])
            # print(folder, basename)
            print(os.path.join(folder, basename))
            insert_data((filename, ext[1:], read_bin(os.path.join(folder, basename))))


if __name__ == '__main__':
    create_table()
    # insert_data(('microphone', 'png', read_bin(r'product/mic.png')))
    # insert_data(('big tablet', 'png', read_bin(r'product/tablet.png')))
    # insert_data(('simple text file', 'txt', read_bin(r'product/demo.txt')))
    # select_data(2, 'test1.png')
    # select_data(1)
    # select_data(14,'sample.jpg')
    # insert_files_in_folder(r'product', 'jpg')

