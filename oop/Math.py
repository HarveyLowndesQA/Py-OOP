class Math:
        
    def div(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Divide by zero error")
    
    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def mul(self, a, b):
        return a*b
        
        
    def PrintAndDoMath(self, function):
        print(function)
