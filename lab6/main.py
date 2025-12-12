class Device:
    def __init__(self, id, name, isOn):
        self.id = id
        self.name = name
        self.isOn = isOn

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def getStatus(self):
        print(self.id, self.name,self.isOn)
    
class SmartHome:
    device_list = []
    id_count = 0
    def __init__(self):
        SmartHome.device_list.append(Device.self)

    def add_id(id_count):
        return id_count + 1
    
    def addDevice(name, isOn = False):
        SmartHome.id_count = SmartHome.add_id(SmartHome.id_count)
        id = SmartHome.id_count
        n = Device(id, name, isOn)
        SmartHome.device_list.append(n)

    def showAllDevices():
        for i in SmartHome.device_list:
            print(i.id, i.name)
        
    def activateAll():
        for i in SmartHome.device_list:
            Device.turnOn(i)

    def turnOffAll():
        for i in SmartHome.device_list:
            Device.turnOff(i)





class Main:
    def __init__(self):
        pass

class Light(Device):
    def __init__(self, light):
        self.light = light

    def performAction(self):
        print(f"Lamp {self.name} is shining with brightness {self.light}")

SmartHome.addDevice('gay')
SmartHome.addDevice('gay2')
lamp = Light(SmartHome.addDevice('lama'))
lamp.performAction()
# for i in SmartHome.device_list:
#     Device.getStatus(i)
# SmartHome.activateAll()
# for i in SmartHome.device_list:
#     Device.getStatus(i)
# SmartHome.turnOffAll()
# for i in SmartHome.device_list:
#     Device.getStatus(i)

#SmartHome.showAllDevices()
