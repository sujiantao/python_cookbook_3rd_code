# 问题：怎样找出一个序列中出现次数最多的元素呢？

# 解决方案：collections.Counter类就是专门为这类问题而设计的
# 它甚至有一个有用的most_common()方法直接给了你答案。
# 为了演示，先假设你有一个单词列表并且找出哪个单词出现频率最高。你可以这样做：

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

# 讨论：作为输入，Counter对象可以接受任意的由可哈希望（hashable）元素构成的序列对象。
# 在低层实现上，一个Counter对象就是一个字典，将元素映射到它出现的次数上。比如：

print(word_counts['not'])
print(word_counts['eyes'])
