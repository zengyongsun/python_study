# and or 连接判断语句

# 检查特定值是否包含在列表中 in   检查不在列表中 not in

list_1 = ['zhangsan','lisi','wangwu','zhaoliu']

print("zhangsan" in list_1)
print("zengyong" in list_1)

is_load = True

# if elif else
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

list_2 =[]
if list_2:
    print("列表有数据")
else:
    print("空列表")

for value in list_2:
    print(value)