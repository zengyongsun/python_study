alien_0 = {'color':'green','points':5}
print(alien_0)

# 查看值
print(alien_0['color'])
# 增加值
alien_0['x_position'] = 0
alien_0['y_position'] = 0

print(alien_0)

# 删除
del alien_0['color']
print(alien_0)

# 遍历所有的键—值对
for key, value in alien_0.items():
    print(key+' = '+str(value))

# 遍历字典中的所有键
for key in alien_0.keys():
    print('key '+key)

# 遍历字典中的所有值
for value in alien_0.values():
    print('value '+str(value))

# set 集合中，不存在重复的元素