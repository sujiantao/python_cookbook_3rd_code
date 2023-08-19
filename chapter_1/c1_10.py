# 删除序列相同的元素并保持顺序

# 如果序列上的值都是hashable类型，那么可以很简单的利用集合或者生成器来解决这个问题。比如：

# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
# a = [1, 5,  3, 1, 9, 1, 5, 10]
#
# print(list(dedupe(a)))

# 这个方法仅仅在序列中元素为hashable的时候才管用。
# 如果你想消除元素不可哈希（比如dict类型）的序列中重复元素的话，你需要闺怨上述代码稍微修改一下，就像这样：

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [
    {'x': 1,'y': 2},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4}]

print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
