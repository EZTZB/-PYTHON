# *coding:utf-8 *
# 无序不重复序列
# 用来去重复数据
# 交集&、并集|、差集-运算

set_ = {1, 2, 3}
set_.add(4)
print('集合添加一个元素：\n', set_)

set_.update({11, 22})
set_.update([33, 44])
set_.update((55, 66))
print('集合添加其他的数据类型：\n', set_)

set_.remove(55)
set_.discard(500)  # 元素不存在 不抛异常
print('删除元素55\n', set_)

set_.pop()  # 不能添加参数 删除一个元素
print('删除一个元素\n', set_)

set_.clear()
print('清除集合数据\n', set_)

set_ = {1, 2, 3}
set_2 = {3, 2, 1}
print('集合判断\n', set_ == set_2, set_ != set_2)

set_1 = {1, 2, 3}
set_2 = {4, 2, 1}
print('交集运算\n', set_1 & set_2)
print('并集运算\n', set_1 | set_2)
print('差集运算\n', set_1 - set_2)
print('差集运算\n', set_2 - set_1)
