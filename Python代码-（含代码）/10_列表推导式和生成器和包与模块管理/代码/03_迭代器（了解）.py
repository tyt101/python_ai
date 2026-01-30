
# 迭代器Iterator,
# 可迭代对象Iterable
from collections.abc import Iterator, Iterable, Generator

# type(): 查看数据类型
# isinstance() : 判断某个变量是否为某个数据类型

print(10, type(10))  # 10
# print(type(10) == int)  # True
print(isinstance(10, int))  # 判断10是不是int类型
print(isinstance(10, (int, float, list)))  # 判断10是不是int或float或list类型
print()

# 迭代器Iterator (了解)
#    1. 可以使用for循环遍历
#    2. 可以使用next调用
print(isinstance(3, Iterator))  # False
print(isinstance(3.14, Iterator))  # False
print(isinstance("hello", Iterator))  # False
print(isinstance(None, Iterator))  # False
print(isinstance(True, Iterator))  # False
print(isinstance([1,2], Iterator))  # False
print(isinstance((1,2), Iterator))  # False
print(isinstance({1:2}, Iterator))  # False
print(isinstance({1,2}, Iterator))  # False
print(isinstance((i for i in range(3)), Iterator))  # True
print()

# 可迭代对象 Iterable
#   1. 可以使用for循环遍历
print(isinstance(3, Iterable))  # False
print(isinstance(3.14, Iterable))  # False
print(isinstance("hello", Iterable))  # True
print(isinstance(None, Iterable))  # False
print(isinstance(True, Iterable))  # False
print(isinstance([1,2], Iterable))  # True
print(isinstance((1,2), Iterable))  # True
print(isinstance({1:2}, Iterable))  # True
print(isinstance({1,2}, Iterable))  # True
print(isinstance((i for i in range(3)), Iterable))  # True
print()

# 生成器 Generator
#
print(isinstance(3, Generator))  # False
print(isinstance(3.14, Generator))  # False
print(isinstance("hello", Generator))  # False
print(isinstance(None, Generator))  # False
print(isinstance(True, Generator))  # False
print(isinstance([1,2], Generator))  # False
print(isinstance((1,2), Generator))  # False
print(isinstance({1:2}, Generator))  # False
print(isinstance({1,2}, Generator))  # False
print(isinstance((i for i in range(3)), Generator))  # True


# 生成器(Generator)是迭代器(Interator)的子类,迭代器是可


# iter() : 可迭代对象 => 迭代器 (了解)
n = [1, 2, 3]
n2 = iter(n)
print(n2)  # list_iterator object
# print(next(n2))
# print(next(n2))

# list(): 变成列表
n3 = list(n2)
print(n3)