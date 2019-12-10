list_name = {'zhangsan','lisi','wuwang','zhaoliao'};

for name in list_name:
    print(name)

# 函数range() 让你能够轻松地生成一系列的数字
for value in range(1,5):
    print(value)

print(range(1,5))

print(list(range(1,9)))

print(list(range(1,100,2)))

digits = range(1,15)
print(max(digits))
print(min(digits))
print(sum(digits))

list_p = [ value**2 for value in range(1,10)]
print(list_p)
