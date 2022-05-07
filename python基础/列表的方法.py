# *coding:utf-8 *

# 列表元素按顺序有序排序
# 索引映射唯一一个数据
# 列表可以存储重复数据
# 任意数据类型混存
# 根据需要动态分配和回收内存
#


list_ = ['hello', 'word', 98, '666']
list_2 = [111, 222]

print('获取一个元素的第一索引\n', list_.index('hello'), '\n',
      '指定列表范围查找元素的索引\n', list_.index(98, 2, 4))

list_.append('元素')
print('添加一个元素\n', list_)

list_.append(list_2)
print('将列表作为元素加到列表内\n', list_)

list_.extend(list_2)
print('添加多个元素\n', list_)

list_.insert(1, '999')
print('指定位置添加元素\n', list_)

list_.remove('元素')
print('删除\n', list_)

list_.pop(0)
# 用索引删除元素，不指定索引删除最后一个元素
print('删除索引0\n', list_)

list_.clear()
print('列表清空\n', list_)


print('----------------下面切片------------------------')


list_ = [10, 20, 30, 40, 50, 60, 70, 80]
print('list_\n', list_)
print('用索引获取元素\n', list_[0])

list_2 = list_[3:6:1]   # 开始：结束：步长，取一部分元素作为新列表
print('list2\n', list_2)

list_[6:] = list_2      # 2个列表的重组
print('列表的重组\n', list_)

print('获取列表索引0的数据\n', list_[0])         # 获取列表的索引数据

print('倒序获取列表的索引数据\n', list_[-1])        # 倒序获取列表的索引数据

print('列表切片显示\n', list_[1::2])      # 列表切片,空 代表到底或从头

list_[0] = 100                  # 修改元素
print('用索引修改元素\n', list_)
list_[1:3] = []                 # 删除一段元素 不改变列表id
print('用索引删除1:3元素\n', list_)
list_[1:3] = [44, 55]   # 替换范围内的元素，元素数量可以多
print('用索引修改元素\n', list_)

print('负数步长，输出倒序\n', list_[::-1])      # 负数步长，输出倒序


list_.sort()               # 进行升序排序
print('升序排序\n', list_)
list_.sort(reverse=True)   # 降序排序
list_3 = sorted(list_)     # 排序之后产生新列表id
print('排序之后产生新列表id\n', id(list_3), id(list_))

print('判断100 in 列表\n', 100 in list_)
print('判断100 not in 列表\n', 100 not in list_)

x = len(list_)
print('列表的元素个数\n', x)

print('遍历输出列表元素：')
for i in list_:
    print(i, end=' ')
print('')


print('----------------列表生成式-------------------')

list_4 = [i for i in range(1, 10)]
print(list_4)

list_5 = [i * 2 for i in range(1, 10)]
print(list_5)
