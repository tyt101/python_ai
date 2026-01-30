
# 1. 利用封装和继承的特性完成如下操作：
# 小学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 打架
#
# 中学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 谈恋爱
#
# 大学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 打游戏

# 调用：
# 创建小学生对象
#    调用学习的方法
#    打印内容为： xx 学习的内容为：语文 数学 英语
#
# 创建中学生对象
#    调用学习的方法
#    打印内容为： xx 学习的内容为：语数外 生物化 史地政
#
# 创建大学生对象
#    调用学习的方法：
#    打印内容为： 逃课中..

class Student:
    def __init__(self, name, number, age, sex):
        self.name = name
        self.number = number
        self.age = age
        self.sex = sex

    def study(self, content):
        print(f'{self.name}学习的内容是:{content}')
# 小学生
class Pupil(Student):
    def __init__(self, name, number, age, sex):
        super().__init__(name, number,age,sex)
    def fight(self):
        print('我是小学生，我喜欢打架')
# 中学生
class Middle(Student):
    def __init__(self, name, number, age, sex):
        super().__init__(name, number, age, sex)
    def love(self):
        print('我是中学生，我开始谈恋爱了')

# 大学生
class College(Student):
    def __init__(self, name, number, age, sex):
        super().__init__(name, number, age, sex)
    def game(self):
        print('我是大学生，我现在喜欢玩游戏')


pupil = Pupil('tyt_pupil', 10001, 9, 'girl')
middle = Middle('tyt_middle', 10002, 16, 'boy')
college = College('tyt_college', 10003, 21, 'girl')

pupil.study('语文 数学 英语')
middle.study('语数外 生物化 史地政')
college.study('逃课中..')