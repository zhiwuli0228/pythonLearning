from typing import Dict

# 初始化方式1
dict1 = {}

# 初始化方式2
dict2 = dict()

dict1['语文'] = 100
dict1['数学'] = 101
dict1['英语'] = 105

print(dict1)

for k, v in dict1.items():
    print(k, v)

dict3: Dict[int, str] = {1: '张三', 2: 'lisi'}
dict3.setdefault(4, 'wangwu')
print(dict3)
