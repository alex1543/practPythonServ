import http.server
import socketserver
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # работа с базой данных.
        import mysql.connector
        myconn = mysql.connector.connect(host = '127.0.0.1', port = '3306', user = 'root', passwd = '', db = 'test', charset='utf8', use_unicode = True)
        cur = myconn.cursor()
        cur.execute("SET NAMES utf8")
        cur.execute("USE test")

        if "form.html" in self.path:
            print(self.path)
            import urllib.parse
            d = urllib.parse.parse_qs(self.path)
            col1 = d.get('col1', [''])[0]
            col2 = d.get('col2', [''])[0]
            col3 = d.get('col3', [''])[0]
            print("col1=" + col1 + ", col2=" + col2 + ", col3=" + col3)
            sql = "INSERT INTO myarttable (text, description, keywords) VALUES ('"+col1+"', '"+col2+"', '"+col3+"')"
            cur.execute(sql)
            myconn.commit()

        #if self.path == '/':
        # формирование файла для отправки в браузер.
        file_out = open("out.html", "w")

        with open('select.html') as file:
            for line in file:

                if ("@tr" not in line) and ("@ver" not in line):
                    file_out.write(line)
                #    print(line.rstrip())

                if ("@tr" in line):
                    print("Getting a table from MySQL...")
                    # формирование заголовка таблицы.
                    cur.execute("SHOW COLUMNS FROM myarttable")
                    file_out.write("<table><tr>")
                    result = cur.fetchall()
                    for line in result:
                        file_out.write('<td>'+str(line[0])+'</td>')
                    file_out.write("</tr>")
                    # формирование строк таблицы.
                    cur.execute("SELECT * FROM myarttable WHERE id>14 ORDER BY id DESC")
                    result = cur.fetchall()
                    for row in result:
                        file_out.write("<tr>")
                        for cell in row:
                            sCellNew = str(cell).strip()
                            file_out.write("<td>"+sCellNew+"</td>")
                        file_out.write("</tr>")

                if ("@ver" in line):
                    cur.execute("SELECT VERSION() AS ver")
                    result = cur.fetchall()
                    file_out.write(str(result[0][0]))
        file_out.close()

        myconn.close()
        self.path = '/out.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = socketserver.TCPServer(('0.0.0.0', 8082), Handler)
print("serving at http://localhost:8082/")
server.serve_forever()
