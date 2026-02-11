thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)
thisset.update([1,4],[5,6])
print(thisset)
#thisset.remove(8) # 删除元素 如果元素不存在则不会报错

thisset.discard(8) # 删除元素 不存在也不会报错
print(thisset)
# thisset.pop()
print(thisset)
print(len(thisset))
if "ok" in thisset:
    print("存在")
else:
    print("不存在")

thisset.clear()
print(thisset)