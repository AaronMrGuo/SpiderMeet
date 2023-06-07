import pymysql
import pandas as pd
from tabulate import tabulate
import logging


class Database:
    def __init__(self, host, user, password, database):
        self.host = host  # 数据库主机地址
        self.user = user  # 数据库登录用户名
        self.password = password  # 数据库登录密码
        self.database = database  # 数据库名称
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                          database=self.database)  # 连接数据库
        self.cursor = self.connection.cursor()  # 创建游标
        self.logger = logging.getLogger('database_logger')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def execute_query(self, query):
        try:
            self.cursor.execute(query)  # 执行查询语句
            return self.cursor.fetchall()  # 返回查询结果
        except Exception as e:
            self.logger.error(f"An error occurred while executing query: {query}\nError message: {str(e)}")

    def execute_insert_query(self, query, values):
        try:
            self.cursor.execute(query, values)  # 执行插入语句
            self.connection.commit()  # 提交事务
            return self.cursor.lastrowid  # 返回插入的最后一行ID
        except Exception as e:
            self.logger.error(f"An error occurred while executing insert query: {query}\nError message: {str(e)}")

    def execute_update_query(self, query, values):
        try:
            self.cursor.execute(query, values)  # 执行更新语句
            self.connection.commit()  # 提交事务
            return self.cursor.rowcount  # 返回更新的行数
        except Exception as e:
            self.logger.error(f"An error occurred while executing update query: {query}\nError message: {str(e)}")

    def execute_delete_query(self, query, values):
        try:
            self.cursor.execute(query, values)  # 执行删除语句
            self.connection.commit()  # 提交事务
            return self.cursor.rowcount  # 返回删除的行数
        except Exception as e:
            self.logger.error(f"An error occurred while executing delete query: {query}\nError message: {str(e)}")

    def create_table(self, table_name, columns):
        try:
            query = "CREATE TABLE IF NOT EXISTS {} {}".format(table_name, columns)  # 创建表的SQL语句
            self.cursor.execute(query)  # 执行创建表语句
            self.connection.commit()  # 提交事务
        except Exception as e:
            self.logger.error(f"An error occurred while creating table: {table_name}\nError message: {str(e)}")

    def drop_table(self, table_name):
        try:
            query = "DROP TABLE IF EXISTS {}".format(table_name)  # 删除表的SQL语句
            self.cursor.execute(query)  # 执行删除表语句
            self.connection.commit()  # 提交事务
        except Exception as e:
            self.logger.error(f"An error occurred while dropping table: {table_name}\nError message: {str(e)}")

    def insert_data_from_df(self, table_name, df):
        # for i in range(df.shape[0]):
        #     query = "SELECT COUNT(*) FROM {} WHERE {}".format(table_name, df.loc[i, 'title'])  # 查询是否存在相同数据的SQL语句
        for _, row in df.iterrows():
            query = "SELECT COUNT(*) FROM {} WHERE {}".format(table_name, ' AND '.join(
                [f"{column}='{value}'" for column, value in row.items()]))  # 查询是否存在相同数据的SQL语句
            # print(query)
            self.cursor.execute(query)  # 执行查询语句
            if self.cursor.fetchone()[0] == 0:  # 如果不存在相同数据
                columns = ', '.join(list(row.index))
                values = tuple(row)
                placeholders = ', '.join(['%s'] * len(values))  # 使用占位符 %s
                query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, columns, placeholders)
                self.execute_insert_query(query, values)  # 执行插入数据语句

# if __name__ == '__main__':
#     # 初始化数据库连接
#     db = Database(host='localhost', user='root', password='369369', database='meeting')
#
#     # 创建测试数据
#     # data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35], 'gender': ['F', 'M', 'M']}
#     # df = pd.DataFrame(data)
#
    # # 创建表
    # table_name = "test_meet"
    # columns = "(id INT AUTO_INCREMENT PRIMARY KEY, source VARCHAR(255), date_time VARCHAR(255), title VARCHAR(255), url VARCHAR(500), state INT,claw_date VARCHAR(255))"
    # db.create_table(table_name, columns)
#
#     # 向表中插入数据
#     db.insert_data_from_df(table_name, df)
#
#     # 查询数据
#     query = "SELECT * FROM {}".format(table_name)
#     result = db.execute_query(query)
#     print(tabulate(result, headers='keys', tablefmt='psql'))
#     # print(result)
#
#     # 更新数据
#     # query = "UPDATE {} SET age=%s WHERE name=%s".format(table_name)
#     # values = (40, 'Bob')
#     # rows_updated = db.execute_update_query(query, values)
#     # print("{} rows updated.".format(rows_updated))
#
#     # 删除数据
#     # query = "DELETE FROM {} WHERE name=%s".format(table_name)
#     # values = ('Charlie',)
#     # rows_deleted = db.execute_delete_query(query, values)
#     # print("{} rows deleted.".format(rows_deleted))
#
#     # 删除表
#     # db.drop_table(table_name)
#
    # # 关闭数据库连接
    # db.connection.close()
