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
