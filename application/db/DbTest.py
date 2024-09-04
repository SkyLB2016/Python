import pymysql

host = '127.0.0.1'
port = '3306'
user = 'root'
passwd = '1qaz2wsx'
dbname = 'python'
charset = 'utf8mb4'
# 创建连接
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=dbname, charset=charset)

# 创建游标(查询数据返回为元组格式）
# cursor = conn.cursor()

# 创建游标（查询数据返回为字典格式）
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 1.执行 SQL 返回查询的行数
effect_row1 = cursor.execute('select * from USER')
# effect_row1 = cursor.execute("select * from USER")


