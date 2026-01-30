# 作业

# 已知列表 names = ['jeff','rain','jack','lucy','lance','feifei']
# a.往names列表里feifei前面插入一个alex
#%%
names = ['jeff','rain','jack','lucy','lance','feifei']
names.insert(0, 'alex')
print(names)
# b.把lucy的名字改成中文：路西
#%%
names = ['jeff','rain','jack','lucy','lance','feifei']
names[names.index('lucy')] =  '路西'
print(names)
# c.往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]
#%%
names = ['jeff','rain','jack','lucy','lance','feifei']
rain_index = names.index('rain')
names[rain_index + 1:rain_index + 1] = ['oldboy', 'oldgirl']
print(names)
# d.返回lance的索引值
#%%
names = ['jeff','rain','jack','lucy','lance','feifei']
print(names.index('lance'))
# e.创建新列表["佩奇", "喜羊羊"],合并入names列表
#%%
lists = ["佩奇", "喜羊羊"]
names.extend(lists)
print(names)
# f.取出names列表中索引4-7的4个元素
#%%
names = ['jeff','rain','jack','lucy','lance','feifei',"佩奇", "喜羊羊"]
names_4_7 = []
for name_index in range(len(names)):
    if 4 <= name_index <= 7:
        names_4_7.append(names[name_index])
print(names_4_7)
# g.取出names列表中索引2-10的5个元素，步长为2
#%%
names = ['jeff','rain','jack','lucy','lance','feifei',"佩奇", "喜羊羊", 'tyt1', 'gjf1', 'tyl1', 'fxq']
print(names[2:11:2])
# h.取出names列表中最后3个元素
#%%
names = ['jeff','rain','jack','lucy','lance','feifei',"佩奇", "喜羊羊", 'tyt1', 'gjf1', 'tyl1', 'fxq']
print(names[-3:])
# I.循环names列表，打印每个元素和索引值，如果索引值为偶数时，把对应的元素改成-1
#%%
names = ['jeff','rain','jack','lucy','lance','feifei',"佩奇", "喜羊羊", 'tyt1', 'gjf1', 'tyl1', 'fxq']
for index, name in enumerate(names):
    print(f'索引 {index},元素 {name}')
    if index % 2 == 0:
        names[index] = 1
print(names)