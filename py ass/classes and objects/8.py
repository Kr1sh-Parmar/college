

class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, String):
            self.value += other.value
        else:
            raise TypeError("Operand must be of type String")
        return self

    def toLower(self):
        return self.value.lower()

    def toUpper(self):
        return self.value.upper()
    
str1 = String("Hello")
str2 = String(" World")
str1 += str2  
print(str1.value)  
print(str1.toLower()) 
print(str1.toUpper())  


