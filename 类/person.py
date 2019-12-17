class Person():
    '''定义人这个类'''

    def __init__(self, name, age):
        '''初始化属性，姓名 和 年龄'''
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃饭")

    def sleep(self):
        print(self.name + "在睡觉")


class Student(Person):
    '''定义学生类'''

    def __init__(self,name,age):
        '''现初始化父类'''
        super().__init__(name,age)

    def study(self):
        print(self.name+"在学习提升自己")