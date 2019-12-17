# 代开文件 open() 函数  关键字 with 在不需要访问文件后将其关闭
with open('pi_digits.txt') as file_object:
    # read()读取文件的全部内容
    contents = file_object.read()
    print(contents)

# 按行读取，对文件对象使用for循环
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())


# 文件内容存储到列表中
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("end")