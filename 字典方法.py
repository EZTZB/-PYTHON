# *coding:utf-8 *
# 无序可变序列
# key:value key唯一

dit = {'1号': 100, '2号': 98, '3号': 55, }

print(dit)

print('获取键的值 键不存在报错\n', dit['1号'])  # 获取键的值 键不存在报错

print('键不存在返回None\n', dit.get('4号'))  # 键不存在返回None

print('查找的键不存在返回88\n', dit.get('4号', 88))  # 查找的键不存在返回88

print('-------------------------------')

print('1号' in dit)
print('1号' not in dit)

if '1号' in dit:
    del dit['1号']
print('删除键\n', dit)

dit['chen'] = 98  # 新增元素
print('新增元素\n', dit)
dit['chen'] = 100  # 修改元素
print('修改元素\n', dit)

print('-------------------------------')

keys = dit.keys()  # 获取键
print('获取键\n', keys)
print('转换为列表\n', list(keys))  # 转换为列表

val = list(dit.values())
print('获取值\n', val)  # 获取值

items = list(dit.items())  # 获取 键值
print('获取 键值\n', items)

print('-------------------------------')

print('遍历字典的键和值')
for i in dit:  # 遍历字典的键
    print(' ', i, dit[i])

print('-------------------------------')

it = ['1', '2', '3']
pri = [111, 222, 333]

dit = {x: y for x, y in zip(it, pri)}  # 表达式创建
print(dit)
