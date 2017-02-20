"""
获取MySQL数据
"""

import pymysql.cursors

# 获取数据库链接
connection = pymysql.connect(host='localhost', user='root', password='88888888', database='wiki_url', charset='utf8mb4')

try:
    # 获取会话指针
    with connection.cursor() as cursor:

        # 查询语句
        sql = "select `urlname`,`urlhref` from `urls` where `id` is not null"

        # 数据库条数
        conut = cursor.execute(sql)
        print(conut)

        # 查询所有数据
        result = cursor.fetchall()
        print(result)

        # 查询3条数据
        # result = cursor.fetchmany(size=3)
        # print(result)

finally:
    connection.close()
