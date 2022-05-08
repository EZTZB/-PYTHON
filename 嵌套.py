# *coding:utf-8 *
for y in range(1, 10):
    for x in range(1, y+1):
        print(str(x) + '*' + str(y) + '=' + str(y * x), end='\t')
    print()
