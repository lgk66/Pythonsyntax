list=['red','blue','green','white','black','yellow']

print(list[-1])
print(list[-2])
print(list[0:4])
print(list[2:])
list.append('orange')  #默认添加到末尾
del list[0]
list.insert(0,'orange') #添加到指定位置
print( list)

list.pop(2)
list.remove('white')
list.reverse()

list.count('orange')
a,b,c='hello','python','world'
print('a+b输出结果：',a+b)

