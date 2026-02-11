def getDogAge(age):
    if type(age) != int:
        return "请重新输入"
    if age <= 0:
        return "输入有误请重新输入："
    elif age == 1:
        return f'你家狗子约等于人的14岁'
    elif age == 2:
        return f'你家狗子约等于人的22岁'
    elif age > 2:
        human = 22 + (age - 2) * 5
        if human > 100:
            return "狗龄过大，请重新输入："
        return f'你家狗子约等于人的{human}岁'


while True:  # 添加循环
    a = input("请输入你家狗子年龄（输入'quit'退出）：")

    # 检查是否要退出
    if a.lower() == 'quit':
        break

    # 尝试转换为整数
    try:
        age = int(a)
        result = getDogAge(age)

        # 检查是否需要重新输入
        if "重新输入" in result:
            print(result)
            continue  # 继续循环，重新输入
        else:
            print(result)
            break  # 正确结果，退出循环

    except ValueError:
        print("输入类型错误，请输入数字")
        continue  # 继续循环，重新输入
