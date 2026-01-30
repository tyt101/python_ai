
# 练习
#%% # 1.求1-100之间可以被6整除的数的个数
c = 0
for i in range(1, 101):
    if i % 6 == 0:
        c += 1
print(c)


#%% # 2.计算1到100以内所有偶数的和。
t = 0
for i in range(1, 101):
    if i % 2 == 0:
        t += i
print(t)


#%% # 3.计算1到100以内所有能被3或者7整除的数的和。
t = 0
for i in range(1, 101):
    if i % 3 ==0 or i % 7 == 0:
        t += i
print(t)

#%%# 4.计算1到100以内能同时被7和3整除的数的个数。
c = 0
for i in range(1, 101):
    if i % 3 ==0 and i % 7 == 0:
        c += i
print(c)

#%%# 5. 求 1-2 + 3-4 + 5-6 ……… + 97-98 + 99-100的结果
t = 0
for i in range(1, 101):
    if i % 2 == 0:
        t -= i
    else:
        t += i
print(t)

#%%# 扩展题目：
# 6. 求 1/1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 ……… + 1/97 - 1/98 + 1/99 - 1/100的结果
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total -= 1 / i
    else:
        total += 1 / i
# 保留两位小数
print('total:%.2f' % total)
print(f'total:{total}')
print('total:{}'.format(total))
#%%# 7.丈母娘要彩礼:
#   小伙马上要准备结婚，丈母娘看小伙实诚，同意让小伙分30期给彩礼，分期规则如下
#   分期： 第1天给1分钱  2º
#         第2天给2分钱  2¹
#         第3天给4分钱  2²
#         第4天给8分钱  2³
#         第5天给16分钱
#         ...
#         第30天
# 如果是你，会同意吗,为什么？
total = 0
for i in range(30):
    total += 2**i
print(f'total:{total // 10 // 10}元')