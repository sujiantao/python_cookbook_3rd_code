# # 1. 在Python中，所有的数据都是对象，无论是数字，字符串，还是自定义类型。而变量则是指向对象的引用
# x = 3
# y = x
# print(id(x))
# print(id(y))

# # 1. 在Python中，所有的数据都是对象，无论是数字，字符串，还是自定义类型。而变量则是指向对象的引用
# x = 3
# print(id(x))
# x = 4
# print(id(x))

# # 2. 在Python中，所有的数据都是对象，无论是数字，字符串，还是自定义类型。而变量则是指向对象的引用, 但是对数字，有优化，同一值指向同一空间
# # https://www.zhihu.com/question/334916499/answer/2804364678?utm_id=0
# x = 30000000
# y = 30000000
# print(id(x))
# print(id(y))

# # 3. 不可变对象str同理
# x = "123"
# y = "123"
# print(id(x))
# print(id(y))

# # 4. 对于可变对象，我们即可改变对象自身，也可以改变变量所指向的对象。
# x = [1, 2, 3]
# print(id(x))
# x.append(4)
# print(id(x))
# x = [1, 2, 3, 4]
# print(id(x))

# 参数传递机制，在Python中，函数参数传递遵循"传对象引用"的方式。对于不可变对象和可变对象，表现出来的效果类似传值和传引用

# # 不可变对象作为参数传递给函数时，函数内部无法改变这个对象自身。函数如果对这个参数进行改变，实际是创建了一个新的对象,原对象并没有改变
# def change(n):
#     print(id(n))
#     n = 1000
#     print(id(n))
#
#
# x = 3
# print(id(x))
# change(x)
# print(x)

# # 可变对象的参数传递，当我们将一个可变对象作为参数传递给函数时，函数内部可以改变这个对象自身。
# def change(n):
#     print(id(n))
#     n.append(4)
#     print(id(n))
#
#
# x = [1, 2, 3]
# print(id(x))
# change(x)
# print(x)

# 函数参数传递机制的实际应用

# # 1. 我们知道一个函数内部会改变传入的可变对象，我们可能需要在传入参数之前先创建一个副本。
# def change(n):
#     print(id(n))
#     n.append(4)
#     print(id(n))
#
#
# x = [1, 2, 3]
# print(id(x))
# change(x[:])
# print(id(x))
# print(x)

# lambda
# square = lambda x: x ** 2
# print(square(5))
#
# data = [{'name': 'Alan', 'age': 20}, {'name': 'Lisa', 'age': 18}, {'name': 'Tom', 'age': 22}]
# data.sort(key=lambda x: x['age'])
# print(data)

# 函数式编程工具
# Python 提供了一些内建函数，用于支持函数式编程，如map()，filter()和reduce()等。这些函数可以用来对列表或其它可迭代对象进行操作，而无需编写循环

# # 1.map()函数：map()函数接收一个函数和一个可迭代对象作为参数，并将该函数应用于可迭代对象的每个地元素，然后返回一个新的可迭代对象
# nums = [1, 2, 3, 4, 5]
# squares = map(lambda x: x**2, nums)
# print(list(squares))

# # 2. filter() 函数接收一个函数和一个可迭代对象作为参考，并返回一个个新的可迭代对象，该对象包含所有使该函数返回True的元素
# nums = [1, 2, 3, 4, 5]
# evens = filter(lambda x: x % 2 == 0, nums)
# print(list(evens))


# 高阶函数
# 在Python中，函数是第一类对象，这意味着我们可以将函数作为参数传递给基它函数，也可以让函数返回另一个函数。这样的函数，我们通常称之为高阶函数
# 高阶函数是函数式编程中的重要概念

# # 1 函数作为参数
# def apply_func(func, x):
#     return func(x)
#
#
# def square(x):
#     return x ** 2
#
#
# print(apply_func(square, 5))

# 2 函数作为返回值
def get_func(power):
    def power_func(x):
        return x ** power
    return power_func


square = get_func(3)

print(square(5))
