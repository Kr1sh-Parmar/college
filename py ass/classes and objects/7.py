

class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters
    

weather = Weather(["temperature", "humidity", "wind speed"])

print("temperature" in weather)  
print("pressure" in weather)    
print("humidity" in weather)     
print("wind speed" in weather)   
print("rain" in weather)




