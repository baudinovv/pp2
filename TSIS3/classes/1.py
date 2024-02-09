class myClass:

    def getString(self):
        self.content = str(input()).upper()
    
    def printString(self):
        print(self.content)

x = myClass()
x.getString()
x.printString()