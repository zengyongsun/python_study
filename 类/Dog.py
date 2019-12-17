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
        print(self.name + '在翻滚')


class BigDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self):
        print(self.name+"在吃东西")

