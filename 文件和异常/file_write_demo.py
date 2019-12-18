file_name = 'program.txt'
with open(file_name, 'w') as file_object:
    file_object.write('hello python')

# w方式打开文件，会把之前的文件覆盖掉
with open(file_name, 'w') as file_object:
    file_object.write('I will use you\n')



# a 方式打开文件，附加模式
with open(file_name, 'a') as file_object:
    file_object.write('I like you')