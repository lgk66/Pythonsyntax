# # 使用大括号 {} 来创建空字典
# emptyDict = {}
#
# # 打印字典
# print(emptyDict)
#
# # 查看字典的数量
# print("Length:", len(emptyDict))
#
# # 查看类型
# print(type(emptyDict))
#
# # !/usr/bin/python3
#
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#
# print("tinydict['Name']: ", tinydict['Name'])
# print("tinydict['Age']: ", tinydict['Age'])
#
# # !/usr/bin/python3
#
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#
# tinydict['Age'] = 8  # 更新 Age
# tinydict['School'] = "菜鸟教程"  # 添加信息`
#
# print("tinydict['Age']: ", tinydict['Age'])
# print("tinydict['School']: ", tinydict['School'])
# !/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键 'Name'
print("tinydict: ", tinydict)
print(tinydict.get('Class', "No Key"))
print(tinydict.items()) #以列表的方式返回字典的键和值·
print(tinydict.keys())
print(tinydict.values())
print(tinydict)

print('元素个数：',len(tinydict))

print('打印字典里的字符串：',str(tinydict))

print('打印字典的变量类型：',type(tinydict))
if  'Name' in tinydict.keys():
    print("Name is present")
else:
    print("Name is not present")

if 7 in tinydict.values():
    print("Age is present")
else:
    print("Age is not present")

print(tinydict.pop('Age'))
tinydict.clear()  # 清空字典
print(tinydict)

del tinydict  # 删除字典


