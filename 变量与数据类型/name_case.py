# 个性化消息： 将用户的姓名存到一个变量中，并向该用户显示一条消息。
# 显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。

name = 'eric'
print('Hello ' + name.title() + ',' + 'would you like to learn some Python today ?')


#调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
name = 'he zheng xiang'
print(name.lower())
print(name.upper())
print(name.title())

# 空白字符
name = '\t   zeng yong sun  \n '
print(name.lstrip())
print(name.rstrip())
print(name.strip())
