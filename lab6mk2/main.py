class Device:
    name: str
    isOn: bool
    def __init__(self, name: str, isOn: bool):
        self.name = name
        self.isOn = isOn

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def getStatus(self):
        print(f'Устройство "{self.name}" | Состояние = {self.isOn}')
    

class Light(Device):
    def __init__(self, name: str, isOn: bool, brightness: int):
        self.brightness = brightness
        if brightness >100:
            self.brightness = 100
            print('Brightness cannot be more than 100')
        elif self.brightness <0:
            self.brightness = 0
            print('Brightness cannot be less than 0')
        super().__init__(name, isOn)

    def performAction(self):
        print(f"Lamp {self.name} is shining with brightness {self.brightness}")

class Thermostat(Device):
    number: int
    def __init__(self, name: str, isOn: bool, temperature: int):
        self.temperature = temperature
        super().__init__(name, isOn)

    def increaseTemp(self, number: int):
        self.temperature = self.temperature + number
    
    def decreaseTemp(self, number: int):
        self.temperature = self.temperature - number

    def performAction(self):
        print(f'Термостат "{self.name}" температура = {self.temperature}°C')

class SecurityCamera(Device):
    recording: bool
    def __init__(self, name: str, isOn: bool, recording: bool):
        self.recording = recording
        super().__init__(name, isOn)
        
    def startRecording(self):
        if self.isOn == False:
            print('Камера не включена')

    def stopRecording(self):
        self.recording = False

    def performAction(self):
        if self.recording == True:
            print(f"Камера {self.name} записывает")
        else:
            print(f"Камера {self.name} не записывает")



class SmartHome:
    device_list: list[Device] = []
    def addDevice(device: Device):
        SmartHome.device_list.append(device)

    def showAllDevices():
        for device in SmartHome.device_list:
            device.getStatus()
    
    def activateAll():
        for device in SmartHome.device_list:
            device.turnOn()
            device.performAction()

    def turnOffAll():
        for device in SmartHome.device_list:
            device.turnOff()


class Main:
    def __init__(self):
        light = Light('lamp', isOn = False, brightness = 100)
        thermo = Thermostat('temp', isOn = False, temperature = 36)
        camera = SecurityCamera('cam', isOn = False, recording = False)
        SmartHome.addDevice(light)
        SmartHome.addDevice(thermo)
        SmartHome.addDevice(camera)
        
        SmartHome.activateAll()
        thermo.increaseTemp(15)
        thermo.decreaseTemp(22)
        camera.startRecording()

        SmartHome.activateAll()
        SmartHome.showAllDevices()
        SmartHome.turnOffAll()
        SmartHome.showAllDevices()



Main()