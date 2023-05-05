# 保留最后N个元素
# 在迭代操作或者其它操作的时候，怎样只保留最后有限内个元素的历史记录
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open(r'../file_1_3.txt') as f:
        for m_line, prev_lines in search(f, 'python', 5):
            for pline in prev_lines:
                print(pline, end='')
            print(m_line, end='')
            print('-'*20)
