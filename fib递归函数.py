# *coding:utf-8 *
def fib(n):  # 递归函数
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 20):
    print(fib(i),end=' ')
print('')

print('--------------2种方法的斐波那契数列-----------------------------')


def fib2(n):
    a, b = 0, 1
    while a < n:
        if a != 0:
            print(a, end=' ')
        a, b = b, a + b  # 同一个时间进行

    print()


fib2(9000)
