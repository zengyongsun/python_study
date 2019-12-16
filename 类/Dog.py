class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name + '正在蹲下')

    def roll_over(self):
        """模拟小狗被命令时翻滚"""
        print(self.name+'在翻滚')


my_dog = Dog('willie',6)
print('my dog name is '+my_dog.name.title()+'.')
print('my dog age is '+str(my_dog.age)+'.')