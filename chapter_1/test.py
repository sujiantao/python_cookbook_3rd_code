from collections import defaultdict


d_dict = defaultdict(set)
for str_key in ["key1", "key2"]:
    d_dict[str_key].add("1")

print(d_dict)
