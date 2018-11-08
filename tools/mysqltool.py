
from pymysql import *

class Mysqltool:
    def __init__(self,database,host="localhost",user="root",password="123456",charset="utf8",port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port
    # 创建数据库连接和游标对象
    def open(self):
        self.db = connect(host=self.host,user=self.user,password=self.password,database=self.database,charset=self.charset,port=self.port)
        self.cursor = self.db.cursor()

    # 关闭游标和数据库连接
    def close(self):
        self.cursor.close()
        self.db.close()
    # 增删改操作
    def insert_update_delete(self,sql,l=None):
        if l is None:
            l=[]
        try:
            self.open()
            self.cursor.execute(sql,l)
            self.db.commit()
        except Exception as e:
            print("执行失败",e)
            self.db.rollback()
        self.close()
    # 查询语句
    def all(self,sql,l=None):
        if l is None:
            l=[]
        self.open()
        self.cursor.execute(sql,l)
        return self.cursor.fetchall()

if __name__ == "__main__":
    msqt = Mysqltool("db5")
    msqt.open()
    try:
        # msqt.insert_update_delete("insert into t1(name,score) values('小明',99)")
        # msqt.insert_update_delete("delete from t1 where name='小明'")
        print(msqt.all("select * from t1"))
        print("成功")
    except Exception as e:
        print("失败",e)
    













