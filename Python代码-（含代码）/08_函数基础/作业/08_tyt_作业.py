#%%
# 1.封装一个函数 验证一个数是否是回文：str(n)[::-1] == str(n)
#   回文： 颠倒过来 与 自身数据一样的称为回文  例如 111  121  1221 12321
def fn1(n) -> bool:
    if str(n)[::-1] == str(n):
        return True
    else:
        return False
print(fn1('123321'))

#%%
# 2.封装一个函数，获取多个数中的最小值，最大值，和，以及平均值
def fn2(*args) -> tuple:
    print(args)
    max_num = max(args)
    print(max_num)
    min_num = min(args)
    print(min_num)
    average = round(sum(args) / len(args), 2)
    return max_num, min_num, average

print(fn2(12,32,39))

#%%
# 3.封装一个函数 获取多个数中的平均值并统计其中高于平均数的值个数
def fn3(*args) -> tuple:
    average = round(sum(args) / len(args), 2)
    return tuple([item for item in args if item > average])
print(fn3(12,32,39))
#%%
# 4.封装一个函数，获取所有的水仙花数
#   水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
#   （例如：1^3 + 5^3+ 3^3 = 153）
def fn4() -> list:
    return [item for item in list(range(100,1000)) if int((str(item))[0]) ** 3 + int((str(item))[1]) ** 3 + int((str(item))[2]) ** 3 == int(item)]

print(fn4())

