# 排序不支持原生比较的对象

# 问题：你想排序类型相同的对象，但是它们不支持原生的比较操作。

# 解决方案：
# 内置的sorted()函数有一个关键字参数key，可以传入一个callable对象给它，
# 这个callable对象对每个传入的对象返回一个值，这个值会被sorted用来排序这些对象。
# 比如，如果你在一个应用程序里面有一个User实例序列，并且你希望通过他们的user_id属性进行排序，
# 你可以提供一个以User实例作为输入并输出相对应的user_id值的callable对象。比如：

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))

sort_notcompare()
