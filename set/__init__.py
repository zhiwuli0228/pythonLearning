set1 = set()

print(set1)

set2 = {1, 2, 3, 4, 5}

set3 = set()
set3.add(6)
set3.add(4)
set3.add(5)
set3.add(7)

print(set3)

# 并集
set4 = set2.union(set3)
print(set4)

# 差集
set5 = set2.difference(set3)
print(set5)

# 交集
set6 = set2.intersection(set3)
print(set6)
