def divide_numbers(a, b):
    """基础除法函数，演示异常处理"""
    try:
        result = a / b
        print(f"{a} ÷ {b} = {result}")
    except ZeroDivisionError as e:
        print(f"错误：除数不能为零！ ({e})")
    except TypeError as e:
        print(f"错误：输入必须是数字！ ({e})")
    else:
        print("计算成功完成！")
    finally:
        print("本次计算结束\n")

# 测试
divide_numbers(10, 2)      # 正常
divide_numbers(10, 0)      # 除零错误
divide_numbers(10, "2")    # 类型错误