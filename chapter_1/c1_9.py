# 查找两个字典的相同点

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# find keys in common
print(a.keys() & b.keys())
# find keys in a that are not in b
print(a.keys() - b.keys())
# find (key, value) pairs in common
print(a.items() & b.items())

# 修改或者过滤字典元素。
# 比如，假如你想以现有字典构造一个或几个排除几个指定键的新字典。下面利用字典推导来实现这样的需求：
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
