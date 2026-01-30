
# Python
#   不可变类型: int,float,str,tuple,bool,NoneType
#    可变类型: list, set, dict

# 赋值
# 不可变类型 (没有关联)
a = 10
b = a
b = 20
print(a, b)  # a=10, b=20


# 可变类型 (有关联)
a = [1, 2, 3]
b = a
b[0] = 666
print(a)  # [666, 2, 3]
print(b)  # [666, 2, 3]



# 深浅拷贝的可视化视图
#  http://pythontutor.com/live.html#mode=edit

# copy: 浅拷贝/浅复制
a = [1, 2, 3]
b = a.copy()
b[0] = 666
print(a)  # [1, 2, 3]
print(b)  # [666, 2, 3]


################拷贝只对可变对象有意义################
# 可变对象：dict list set
#%% 浅拷贝
# 只复制 “外层容器”，容器里的元素还是指向原来的内存地址（相当于 “复制文件夹快捷方式”）。
a = [1, 2, [3, 4]]
b = a.copy()  # 浅拷贝
b[-1][-1] = 888
b[0] = 2
print(a)  # [1, 2, [3, 888]]
print(b)  # [1, 2, [3, 888]]


#%% 深拷贝
# 复制 “外层容器 + 所有嵌套的子元素”，完全生成新的独立对象（相当于 “复制文件夹所有内容”）。
import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)  # 深拷贝
b[-1][-1] = 888
print(a)  # [1, 2, [3, 4]]
print(b)  # [1, 2, [3, 888]]



#%% 直接赋值-相当于改文件夹的名字
a = [1, 2, [3, 4]]
b = a
b[-1][-1] = 888
b[0] = 2
print(a)
print(b)


