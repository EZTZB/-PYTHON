# *coding:utf-8 *
import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
con.execute('create table table_name(id,name,age,local)')
con.execute('insert into table_name (id,name,age,local) values(1,"chen",18,"shanghai")')
con.execute('select * from table_name where id = 1')
con.execute('update table_name set age = 20 where id =1')
con.execute('delete from table_name where id =1')
sql = 'insert into table_name (id,name,age,local) values(?,?,?,?)'
data = [(2, "jack", 18, "shanghai"),
        (3, "peta", 19, "shanghai"),
        (4, "alice", 20, "shanghai"),
        (5, "python", 21, "shanghai"),
        ]
con.executemany(sql, data)
res = con.execute('select * from table_name')


def fun_s(__i):
    __lst = []
    for __x in __i:
        __lst.append(__x)
    return __lst


def fun_1(__i):
    __lst = []
    for __x in __i:
        __y = fun_s(__x)
        __lst.append(__y)
    return __lst


lst = fun_1(res)
# 2个for循环叠加 不能转为 列表套列表 分开调用可以
for i in lst:
    print(i)


con.commit()
cur.close()
con.close()
