bicycles = ['trek', 'redline', 'cannondale', 'specialized']
print(bicycles)

# 末尾添加元素
bicycles.append("haha")
print(bicycles)

# 插入值
bicycles.insert(1,'你好')
print(bicycles)

# 删除
del bicycles[1]
print(bicycles)

pop_bicycle = bicycles.pop()
print(pop_bicycle)
print(bicycles)

bicycles.remove('redline')
print(bicycles)

# 排序 sort()永久性地修改了列表元素的排列顺序
