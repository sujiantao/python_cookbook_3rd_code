# 问题：
# 你构建了一个自定义容器对象，里面包含有列表、元组或其它可迭代对象。
# 你想直接在你的这个新容器对象上执行迭代操作。

# 解决方案：
# 实际上你只需要定义一个__iter__()方法，将迭代操作代理到容器内部的对象上去。
# 比如：

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def ___repr__(self):
        return 'Node({!r)'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

# 讨论
# Python的迭代器协议需要__iter__()方法返回了一个实现了__next__()方法的迭代器对象。
# 如果你只是迭代遍历其它容器的内容，你无须担心底层是怎样实现的。
# 你所要做的只是传递迭代请求即可。

# 这里的iter()函数的使用简化了代码，iter(s)只是简单的通过调用s.__iter__()方法来返回对应的迭代器对象，
# 就跟len(s)会调用s.__len__()原理是一样的
