def hello_word():
    """显示简单的打印问好"""
    print("hello_word")


hello_word();


def show_message(name, age):
    """有返回的打印"""
    # print("hello " + name + age)
    return name + age


show_message('zengyong', '25')
print(show_message('zhangsan',age='24'))

# *任意个参数 存成列表  **任意关键字个参数 字典
def show_name(name,age,*message):
    return message

print(show_name('zeng',24,'hello','world'))