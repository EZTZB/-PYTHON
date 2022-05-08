# *coding:utf-8 *
print('000', '111', '222', end='', sep=' K ')
# end=末尾加空，sep=间隔加k

print('')

print('999\n', '888\t', '666')

x = []
print(type(x))
# type 类型

print(dir(print))
# dir 内容

x = "helloword"
print(x[0], x[1], x[-1])

print(x[:-4], x[2:4], x[5:])
# 字符串切片

len_ = len(x)
print(len_)


# 获取长度


def fun_1(_x, _y, _z=60):  # _z=60 设置缺省值
    pass
    _x = _y + _z
    return _x  # 返回一个对象


# 定义一个函数

name = ['1', '2', '3']
sign = ['1', '2', '3']
x = dict(zip(name, sign))
y = list(zip(name, sign))
print('zip：打包为对应组合的元祖\n', x, y)
