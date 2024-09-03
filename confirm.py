import pymysql

import config

db_config = config.get_config("db")
# 打开数据库连接
db = pymysql.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    port=db_config['port'],
    database=db_config['database'],
    cursorclass=pymysql.cursors.DictCursor
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
cursor.execute("SELECT * FROM customer "
               "where `name` not in ('滴滴-汇嘉旧','滴滴-汇嘉新') "
               "and `status` = 10 ")
customer_list = cursor.fetchall()
cursor.execute("SELECT * FROM corp_info ")
mysql_corp_list = cursor.fetchall()
