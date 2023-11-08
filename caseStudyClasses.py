class vehicle:
    def __init__(self, vehtype):
        self.vehtype = "car"
    
class automobile(vehicle):
    def __init__(self, vehtype, year, make,  model, doors, roof):
        super().__init__(vehtype)
        argList = [automobile.year, automobile.make, automobile.model, automobile.doors, automobile.roof]
        promptList = ["What is the year of the vehicle? ", "What is the make of the vehicle? ", "What is the mnodel of the vehicle? ", "How many doors does this vehicle have? ", "Does it have a solid roof or sun roof? "]
        for x, y in zip(argList,promptList):
            y = input(x)