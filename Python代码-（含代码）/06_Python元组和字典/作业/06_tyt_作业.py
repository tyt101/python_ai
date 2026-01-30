
#%%
# 1.已知字典 dic = {"k1": "v1", "k2": "v2", "k3": "v3"}，实现以下功能
dic = {"k1": "v1", "k2": "v2", "k3": "v3"}

# a.遍历字典 dic 中所有的key
print(dic.keys())
# b.遍历字典 dic 中所有的value
print(dic.values())
# c.循环遍历字典 dic 中所有的key和value
for key, value in dic.items():
    print(f'key:{key}, value:{value}')
# d.添加一个键值对"k4","v4",输出添加后的字典 dic
dic.update({'k4': 'v4'})
print(dic)
# e.删除字典 dic 中的键值对"k1","v1",并输出删除后的字典 dic
dic.pop('k1')
print(dic)

#%%
# 2. 去除列表中成绩小于70的字典
dict_list = [{"科目":"政治", "成绩":98},
             {"科目":"语文", "成绩":77},
             {"科目":"数学", "成绩":99},
             {"科目":"数学1", "成绩":45},
             {"科目":"数学2", "成绩":44},
             {"科目":"历史", "成绩":65}]

itemNew = []
for item in dict_list:
    if item["成绩"] >= 70:
        itemNew.append(item)
print(itemNew)


# 列表推到式
filterItem = [item for item in dict_list if item["成绩"] >= 70]
print(filterItem)


#%%
# 3.已知字典 d2 = {'k1':"v1", 'a':"b"}
#   编写程序，使得d2 = {'k1':"v1", 'k2':"v2", 'k3':"v3", 'a':"b"}

d2 = {'k1':"v1", 'a':"b"}
d2['k2'] = 'v2'
d2['k3'] = 'v3'
print(d2)

#%%
# 4.已知我的电话簿里头有以下联系人，现在输入人名，查询他的号码，
#   如果人名存在，则输出电话号码，如果该人不存在，返回"not found"
address_dict = {'mayun': '13309283335',
                'zhaolong': '18989227822',
                'zhangmin': '13382398921',
                'Gorge': '19833824743',
                'Jordan': '18807317878',
                'Curry': '15093488129',
                'Wade': '19282937665'}
name = input('请输入姓名:')
print(address_dict.get(name, 'not found'))

#%%
# 5.已知列表 numlist = [23,5,56,7,78,89,12,45,6,8,89,100,99],
# 生成一个字典，将大于66的数字保存在字典的第一个key中，
#            将小于等于66的数字保存在字典的第二个key中
# 结果为： { 'key1': [78, 89, 89, 100, 99],
#          'key2': [23, 5, 56, 7, 12, 45, 6, 8]}


num_list = [23,5,56,7,78,89,12,45,6,8,89,100,99]
dict_list = {
    'key1': [item for item in num_list if item > 66],
    'key2': [item for item in num_list if item <= 66]
}
print(dict_list)
