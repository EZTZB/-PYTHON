# *coding:utf-8 *
import sqlite3


# conn = sqlite3.connect(':memory:')
# cur = conn.cursor()
#

def create():
    con = sqlite3.connect('str.db')
    cur = con.cursor()
    cur.execute('''create table user(
                    id integer primary key not null,
                    str text,
                    int integer,
                    float real,
                    bytes blob,
                    none null
                    )''')
    cur.close()
    con.close()


def clear():
    con = sqlite3.connect('str.db')
    cur = con.cursor()
    cur.execute('DROP TABLE user')
    con.commit()
    cur.close()
    con.close()


def insert():
    con = sqlite3.connect('str.db')
    cur = con.cursor()
    sql = 'insert into user (id,str,int,float,bytes,none) values (?,?,?,?,?,?)'
    cur.execute(sql, (1, "chen", 38, 0.1, '0215977', None))       # 单条数据插入

    cur.executemany(sql, [(2, "路飞", 18, 0.12, 0x010101, None),
                          (3, "鸣人", 20, 0.13, 0o010101, None),
                          (4, "佐助", 21, 0.14, 0o010101, None)])

    # ^多条数据插入
    cur.close()
    con.commit()
    con.close()


def update():
    con = sqlite3.connect('str.db')
    cur = con.cursor()
    try:

        cur.execute('update user set int = ? where id = ?', (99, 20))
        cur.execute('update user set id = ? where str = ?', (33, 'pip'))
        con.commit()
    except BaseException as e:
        con.rollback()
        print(e)
        print('操作失败')

    cur.execute('select * from user ')
    res = cur.fetchall()
    print(res)
    cur.close()
    con.close()


def show():
    con = sqlite3.connect('str.db')
    cur = con.cursor()
    cur.execute('select * from user ')
    res = cur.fetchall()
    row = 0
    for i in res:
        row += 1
    print('-------------------------------')
    print('查询的行数：', str(row))
    for i in res:

        print(i)
    cur.execute('select * from user where str =?', ('chen',))
    # 查询可以不是关键字
    res = cur.fetchall()
    print('-----------查询的str--------------------')
    print(res)

    cur.close()
    con.commit()
    con.close()


def delete():
    con = sqlite3.connect('str.db')
    cur = con.cursor()
    __x = int(input('输入删除的id：'))
    cur.execute('delete from user where id=?', (__x,))
    cur.close()
    con.commit()
    con.close()





def menu():
    print('1.创建数据库')
    print('2.插入数据')
    print('3.查询数据库')
    print('4.删除数据')
    print('5.更新数据')
    print('9.清除表')
    print('0.退出')


if __name__ == '__main__':
    while 1:
        menu()
        try:
            x = int(input('输入选择：'))
        except BaseException:
            continue

        if x == 0:
            break

        elif x == 1:
            create()

        elif x == 2:
            insert()

        elif x == 3:
            show()

        elif x == 4:
            delete()
        elif x == 5:
            update()
        elif x == 9:
            clear()

        else:
            print('输入错误')
            continue
