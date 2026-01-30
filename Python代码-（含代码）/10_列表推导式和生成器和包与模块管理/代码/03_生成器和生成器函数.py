# 生成器 generator (掌握)
#  需要使用next或者for循环来调用

nums = [i for i in range(1, 6)]   # 列表推导式
print(nums)
s = {i for i in range(1, 6)}      # 集合推导式
print(s)
d = {f'name{i}': i for i in range(1, 6)}  # 字典推导式
print(d)
g = (i for i in range(1, 4))   # 生成器
print(g)  # generator 生成器对象
# print(list(g))  # [1, 2, 3]

# 1.next
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
# print(next(g))  # StopIteration 报错，已经没有数据了

# 2.for
g = (i for i in range(1, 4))
for i in g:
    print('i =', i)


print()

# 生成器函数:
#   1. 函数内部要有 yield
#   2. 需要用next来调用
#   3. 每个next都会在yield处暂停
#   4. yield 会暂停, 可以返回值

def fn():
    print('hello,我是fn，你看我会执行吗')
    yield  666    # 类似return的返回值，但是不会结束函数
    print('BBBB')
    yield 888

g = fn()
print(g)  # generator object
print( next(g) )  # 666
print( next(g) )  # 888




print()
# 示例:
def gen():
    g = (i for i in range(1, 10**100))

    for i in g:
        # 一个个返回值, 不会退出函数
        yield i

g = gen()
print(next(g))
print(next(g))
print(next(g))
print()

# 问题：
# ① 为什么 gen() 没有 return 却能赋值给 g；
    # 带yield会逐个产出值，是生成器函数，没有return是因为它不是接受函数的返回值，而是调用生成器函数，得到一个生成器对象并赋值给g
# ② 为什么调用 next(g) 能依次打印 1、2、3；
    # next(g)会触发生成器对象g的执行，进入gen的函数体。依次执行yield i并返回 i



# 练习
# 1.请写一个生成器函数, 得到前20个斐波那契数 (难度:*****)
# 斐波那契数列如下：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
#                a  b
#                   a  b
#                      a  b
#    提示:使用while True, 通过调用n次next来获取前20个数
import time
from collections.abc import Iterator, Iterable, Generator
def fun():
    a = 0  # 第一个数
    b = 1  # 第二个数
    m = 1  # 记数器
    while m <= 20:
        a, b = b, a+b
        m = m + 1
        yield a

print(isinstance(fun(), Iterator))
print(isinstance(fun(), Iterable))
print(isinstance(fun(), Generator))
g1 = fun()
for i in g1:
    print(i, end=' ')
    time.sleep(0.1)  # 每隔0.1秒获取下一个斐波那契数



