
# Creating a protected variable
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

# Creating a private variable
class Protected2:
    def __init__(self):
        self.__privateVar = 12
    
    def getPrivate(self):
        print(self.__privateVar)
    
    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected2()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()