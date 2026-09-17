class glassware:
    def __init__(self, name):
        self.name = name

class beaker(glassware):
    def __init__(self, number):
        super().__init__("Beakers")
        self.number = number

class tray:
    def __init__(self):
        self.beaker = [beaker(i)for i in range(5)]

tray = tray()

print(len(tray.beaker))
