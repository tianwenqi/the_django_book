# -*- coding:utf-8 -*-

import pymysql
pymysql.install_as_MySQLdb()

print("Content-Type: text/html\n")
print("<html><head><title>Books</title></head>")
print("<body>")
print("<h1>Books</h1>")
print("<ul>")

connection = pymysql.connect(host='localhost',port=3306,user='root',passwd='hello123',db='test',charset='utf8')
# select发生编码错误时，需要特别指定编码，在connection时完成
cursor = connection.cursor()
cursor.execute("SELECT bookname FROM tmpdoc ORDER BY ﻿bookid DESC LIMIT 10")

for row in cursor.fetchall():
    print("<li>%s</li>" % row[0])
    print("</ul>")
    print("</body></html>")

connection.close()
