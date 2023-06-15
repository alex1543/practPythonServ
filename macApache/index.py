#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

# работа с базой данных MySQL через mysql.connector.
import mysql.connector
myconn = mysql.connector.connect(host = '127.0.0.1', port = '3306', user = 'root', passwd = '', db = 'test', charset='utf8', use_unicode = True)
cur = myconn.cursor()
cur.execute("SET NAMES utf8")
cur.execute("USE test")

import os
query_string = os.environ['QUERY_STRING']
if 'col1' in query_string:
    import urllib.parse
    d = urllib.parse.parse_qs(query_string)
    col1 = d.get('col1', [''])[0]
    col2 = d.get('col2', [''])[0]
    col3 = d.get('col3', [''])[0]
    sql = "INSERT INTO myarttable (text, description, keywords) VALUES ('"+col1+"', '"+col2+"', '"+col3+"')"
    cur.execute(sql)
    myconn.commit()

# отправка в браузер.
print("Content-Type: text/html\n")

with open('select.html') as file:
    for line in file:

        if ("@tr" not in line) and ("@ver" not in line):
            print(line)

        if ("@tr" in line):
            # формирование заголовка таблицы.
            cur.execute("SHOW COLUMNS FROM myarttable")
            print("<table><tr>")
            result = cur.fetchall()
            for line in result:
                print('<td>'+str(line[0])+'</td>')
            print("</tr>")
            # формирование строк таблицы.
            cur.execute("SELECT * FROM myarttable WHERE id>14 ORDER BY id DESC")
            result = cur.fetchall()
            for row in result:
                print("<tr>")
                for cell in row:
                    print("<td>"+str(cell)+"</td>")
                print("</tr>")

        if ("@ver" in line):
            cur.execute("SELECT VERSION() AS ver")
            result = cur.fetchall()
            print(str(result[0][0]))
