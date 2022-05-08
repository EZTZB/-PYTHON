# *coding:utf-8 *
import string
print(string.digits)
# 0123456789
print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ


def check(arg):
    if arg in string.ascii_letters:
        print('输入符合要求')
    else:
        print('输入不符合要求')
