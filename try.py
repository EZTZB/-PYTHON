# *coding:utf-8 *
try:
    pass   # 执行命令
except BaseException as err:
    print(err)    # 命令有报错 就会执行
else:
    pass    # 命令没有报错 就会执行

try:
    x = int(input('输入选择的数字'))
except BaseException as err:  # 获取未知的错误
    print(err)
    pass
else:
    pass
finally:
    print('无论是否产生异常，都会执行的代码')
