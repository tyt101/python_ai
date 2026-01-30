import math


# 利用面向对象的思想写下面的程序：直接赋值
#%%
# 1.小明穿着白色的特步运动鞋在奥林匹克公园跑步
#   Person类
#      属性：name
#      方法：run(self, place, shoes)
class Person:
    name = ''

    def __init__(self, name):
        self.name = name

    def run(self, place, shoes):
        print(f'{self.name}穿着白色的{shoes}在{place}跑步')

p = Person('小明')
p.run('奥林匹克公园', '特步运动鞋')

#%%
# 2.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
#   Person2类
#      属性：name, pig
#      方法：find_pig(self)

class Person2:
    name = ''
    pig = ''

    def __init__(self, name, pig):
        self.name = name
        self.pig = pig

    def find_pig(self):
        print(f'{self.name}家的荷兰宠物猪【{self.pig}】跑丢了，她哭着贴寻猪启示。')

p = Person2('王梅', '笨笨')
p.find_pig()

#%%
# 3. 定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
# 圆类Circle:
#     属性: 半径r,圆心(Point对象)
#     方法: 周长,面积
#
# 点类Point:
#   属性: x,y
#   方法: 与圆的关系(在圆内/在圆外/在圆上)

import math

class Circle:
    def __init__(self, r, point):
        self.r = r
        self.center = point


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def relation_with_round(self, circle):
        distance = math.sqrt((self.x - circle.center.x) ** 2 + (self.y - circle.center.y) ** 2)
        if distance < circle.r:
            position = '在圆内'
        elif distance > circle.r:
            position = '在圆外'
        else:
            position = '在圆上'
        return position

center = Point(0, 0)
circle = Circle(5, center)

point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = Point(4, 5)
print('point1:', point1.relation_with_round(circle))
print('point2:', point2.relation_with_round(circle))
print('point3:', point3.relation_with_round(circle))


#%%
# 4. 使用面向对象的思想，创建下面的类，对象
#
#  有一个银行账户类 Account,
#     属性包括: 名字name , 余额balance属性
#    方法有：存钱 save_money(self,money)、
#           取钱 get_money(self,money)、
#           查询余额 show_balance(self)。
#    要求：取钱时，要判断余额是否充足，余额不够的时候要提示余额不足




