import pymysql


class Mysql():

    def __init__(self):
        # 1). ************************链接数据库**********************************
        self.conn=pymysql.connect(
                    host='localhost',
                    user='root',
                    password='123456',
                    db='test',
                    charset='utf8',
        )
        self.cur=self.conn.cursor()  #开启游标

    def create(self,table_name,key):
        # 2). ************************创建数据表**********************************
        # 示例： create table test_mysql (id int, name varchar(30));
        # 需要创建表名，创建的健值
        try:
            create_sqli = "create table {} {};".format(table_name,key)
            self.cur.execute(create_sqli)
        except Exception as e:
            print("创建数据表失败:", e)
        else:
            print("创建数据表成功;")

    def insert(self,table,value):
        # 3). *********************插入数据****************************
        #示例：        insert into hello values(2,'dfgdfg')
        # 需要表名，value值
        try:
            insert_sqli = "insert into {} values{};".format(table,value)
            self.cur.execute(insert_sqli)
        except Exception as e:
            print("插入数据失败:", e)
        else:
            # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
            self.conn.commit()
            print("插入数据成功;")

    def delete(self,table,dl):
        # 4). *********************删除数据****************************
        #示例：        DELETE FROM hello WHERE id = 3
        # 需要表名，查询条件
        try:
            delete_sqli = "DELETE FROM {} WHERE id = {}".format(table,dl)
            self.cur.execute(delete_sqli)
        except Exception as e:
            print("删除数据失败:", e)
        else:
            self.conn.commit()
            print("删除数据成功;")



if __name__ == '__main__':
    list=[(9,'dfgf'),(10,'kljg')]

    list_dl=[7,8]

    # Mysql().create("hello_test","(id int,name varchar(30))") #新增 表

    # try:
    #     for i in list_dl:
    #         print(i)
    #         Mysql().delete("hello",i)  #循环删除表
    #
    # except Exception as e:
    #     print(e)


    # # 批量插入数据
    # for j in list:
    #     Mysql().insert("hello",j)