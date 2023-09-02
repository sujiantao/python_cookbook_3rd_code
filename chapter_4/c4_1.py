# 问题：你想遍历一个可迭代对象中的所有元素，但是确不想使用for循环。

# 解决方案：为了手动遍历可迭代对象，使用next()函数并在代友中捕获StopIteration异常。
# 比如，下面的例子手动读取一个文件中的所有行：

def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

def manual_iter_v2():
    with open('/etc/passwd') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


if __name__ == "__main__":
    manual_iter_v2()

# 讨论
# 大多数情况下，我们会使用for循环语句来遍历一个可迭代对象。
# 但是，偶尔也需要对迭代做更加精确的控制，这时候了解底层迭代机制就显得尤为重要了。
# 下面的交互示例向我们演示了迭代期间所发生的基本细节：

items = [1, 2, 3]
# get the iterator
it = iter(items)
# Run the iterator
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 本章接下来几小节会更深入的讲解迭代相关技术，前提是你先要理解基本的迭代协议机制。
# 所以确保你已经把这章的内容牢牢记在心中。
