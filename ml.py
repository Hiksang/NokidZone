import pandas as pd
import pymysql
import logging
import sys

insta_db = pymysql.connect(
    user='root',
    passwd='Rlagmltkd1!',
    host='127.0.0.1',
    db='test',
    charset='utf8'
)
cursor = insta_db.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM 1_pre;"
cursor.execute(sql)
result = cursor.fetchall()

result = pd.DataFrame(result)
print(result)