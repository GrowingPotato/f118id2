class Device:
    objlist = []
    def __init__(self, name, isOn):
        Device.objlist.append(self)
        self.name = name
        self.isOn = isOn

    def turnOn(self):
        self.isOn = True

    def turnOff(self):  
        self.isOn = False
    def getStatus(self):
        return self.isOn

tom = Device('TOM', False)
ben = Device('BEN', True)

for i in Device.objlist:
    print(i.name)





class MyClass:
    _instances = [] # Список для хранения всех экземпляров

    def __init__(self, name):
        self.name = name
        MyClass._instances.append(self) # Добавляем себя в список

    @classmethod
    def get_all_instances(cls):
        return cls._instances

obj1 = MyClass("Экземпляр 1")
obj2 = MyClass("Экземпляр 2")

print(f"Всего объектов: {len(MyClass.get_all_instances())}") # 2
for obj in MyClass.get_all_instances():
    print(obj.name)
