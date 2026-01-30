
# 类：
#    属性：类属性，对象属性，私有属性
#    方法：对象方法，私有方法， 类方法，静态方法

class Person:
    age = 30  # 类属性

    def __init__(self, name):
        self.name = name  # 对象属性

    # 对象方法，成员方法
    def run(self):
        print('run')
        print(self.name)
        print(Person.age)
        self.__sleep()

    # 私有方法
    def __sleep(self):
        print('sleep')

    # 类方法: (掌握)
    # @classmethod
    #    1.类方法可以用类名来调用（推荐），也可以用对象来调用
    #    2.类方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用类方法，可以节省内存
    #    3.类方法中有cls,没有self,表示可以去调用类名能调用的，不能调用对象属性，对象方法，私有属性，私有方法
    #      cls可以调用类属性，其他类方法，静态方法
    @classmethod
    def eat(cls):  # cls: class
        print('eat')
        print(cls == Person)
        print(cls.age)

    # 静态方法:（了解）
    # @staticmethod
    #    1.静态方法可以用类名来调用（推荐），也可以用对象来调用
    #    2.静态方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用静态方法，可以节省内存（类名来调用）
    #    3. 既没有cls，也没有self，静态方法内部不需要调用类中的任何属性和方法
    @staticmethod
    def game():
        print('game：静态方法')


# 对象
# p = Person('邓超')
# p.run()
Person.eat()
Person.game()

# 类方法: (掌握)
# @classmethod
#    1.类方法可以用类名来调用（推荐），也可以用对象来调用
#    2.类方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用类方法，可以节省内存
#    3.类方法中有cls,没有self,表示可以去调用类名能调用的，不能调用对象属性，对象方法，私有属性，私有方法。
#      cls可以调用类属性，其他类方法，静态方法

# 静态方法:（了解）
# @staticmethod
#    1.静态方法可以用类名来调用（推荐），也可以用对象来调用
#    2.静态方法作用是：不需要创建对象(不需要消耗对象内存)，就可以直接使用静态方法，可以节省内存（类名来调用）
#    3. 既没有cls，也没有self，静态方法内部不需要调用类中的任何属性和方法。类属性和类方法只能通过传入类/用类型访问，实例属性和实例方法智能通过传入实例访问


# import datetime
# dt = datetime.datetime(year=2030, month=1, day=2)
# print(dt.hour)
# datetime.datetime.fromtimestamp()




class Student:
    name = '我是类属性'
    # 构造方法：初始化【实例属性】（每个学生的专属属性）
    def __init__(self, name, score):
        self.name = name  # 实例属性：学生姓名（每个实例值不同） 既有类属性又有实力属性的时候，实例优先
        self.score = score  # 实例属性：学生成绩（每个实例值不同）

    @classmethod
    def get_name_cls(cls):
        return cls.name

    # 实例方法1：访问实例属性（获取学生姓名）
    def get_name(self):
        return self.name  # 通过self访问当前实例的name属性

    # 实例方法2：修改实例属性（更新学生成绩）
    def update_score(self, new_score):
        if 0 <= new_score <= 100:  # 简单的成绩合法性校验
            self.score = new_score  # 通过self修改当前实例的score属性
            print(f"{self.name}的成绩已更新为：{self.score}")
        else:
            print("成绩不合法，必须在0-100之间！")

    # 实例方法3：基于实例属性做专属逻辑（判断该学生是否及格）
    def is_pass(self):
        # 结合当前实例的score属性，执行实例专属的判断逻辑
        if self.score >= 60:
            return f"{self.name}成绩{self.score}，及格✅"
        else:
            return f"{self.name}成绩{self.score}，不及格❌"


# ------------- 测试：创建不同实例，调用实例方法操作专属属性 -------------
# 实例1：学生"张三"，成绩58（每个实例的属性值独立）
stu1 = Student("张三", 58)
print(stu1.get_name())  # 访问实例属性 → 输出：张三
print(Student.get_name_cls())
print(stu1.is_pass())   # 基于实例属性做逻辑 → 输出：张三成绩58，不及格❌
stu1.update_score(85)  # 修改实例属性 → 输出：张三的成绩已更新为：85
print(stu1.is_pass())   # 重新判断 → 输出：张三成绩85，及格✅

print("-" * 30)

# 实例2：学生"李四"，成绩92（与stu1的属性完全独立，互不影响）
stu2 = Student("李四", 92)
print(stu2.get_name())  # 访问实例属性 → 输出：李四
print(stu2.is_pass())   # 基于实例属性做逻辑 → 输出：李四成绩92，及格✅
stu2.update_score(105) # 尝试修改为非法成绩 → 输出：成绩不合法，必须在0-100之间！



class Student:
    # 类属性：所有学生共享的班级名称
    class_name = "Python进阶班"


    @classmethod
    def get_class_name(cls):
        # 访问类属性
        return cls.class_name

    @classmethod
    def set_class_name(cls, new_name):
        # 修改类属性
        cls.class_name = new_name

# 类名直接调用类方法，操作类属性
print(Student.get_class_name())  # 输出：Python进阶班
Student.set_class_name("Python实战班")
print(Student.get_class_name())  # 输出：Python实战班

# 实例也能调用（自动关联所属类），但推荐类名调用
stu = Student()
print(stu.get_class_name())  # 输出：Python实战班


# 类属性和实例属性
# 优先级：实例属性 > 类属性 。普通方法中/init中通过 self 里面访问的是对象（实例）属性；classmethod类方法里通过cls访问的是类属性
# 普通方法只能修改list,dict，set可变值的类属性，可以修改对象（实例）属性；classmethod中是操作类属性的，可以修改任意类属性

