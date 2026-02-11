# 合法的标识符示例
valid_identifiers = [
    "my_variable",  # 字母+下划线
    "_private_var",  # 单下划线开头
    "var123",  # 字母+数字
    "Class_Name",  # 字母+下划线
    "data_2023"  # 字母+数字+下划线
]

# 非法的标识符示例
invalid_examples = [
    "123variable",  # 以数字开头 - 错误
    "my-variable",  # 包含连字符 - 错误
    "class",  # 关键字 - 不推荐
]


# 演示不同下划线前缀的意义
class ExampleClass:
    def __init__(self):
        self.public_drink = "可乐"
        self._protected_attr = "受保护属性"
        self.__private_drug = "毒品"

    def get_private(self):
        return self.__private_attr

    def _internal_method(self):
        return "内部方法，不应直接调用"


# 实例化并测试访问
obj = ExampleClass()

print(obj.public_attr)  # 可以直接访问
print(obj._protected_attr)  # 可以访问，但按约定不应该直接访问
# print(obj.__private_attr)     # 这会引发 AttributeError
print(obj.get_private())  # 通过方法访问私有属性
# print(obj.__private_attr)

# 查看对象的所有属性
print([attr for attr in dir(obj) if not attr.startswith('__')])
