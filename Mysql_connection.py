
# coding: utf-8

import requests
import pymysql
import pymysql.cursors


connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db = 'TESTDB',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
cursor.execute(sql, ('webmaster2@python.org', 'very-secret2'))

connection.commit()

sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
cursor.execute(sql, ('webmaster@python.org',))
result = cursor.fetchone()
print(result)

