# This class can generate various functions.

class function_polynomial:
    active = False

    def __init__(self):
        self.active = True

    def init(self,parameters):
        self.parameters = parameters.split(':')

        if len(self.parameters) < 1:
            print('ERR: parameters of polynomial function not fitting')
            return 0

        try:
            self.order = int(self.parameters[0])
        except:
            print('ERR: polynomial order not correct')
            return 0
        
        if len(self.parameters) != self.order+2:
            print('ERR: polynomial number of parameters not correct')
            return 0

        self.par_float = []

        try:
            for n in range(len(self.parameters)-1):
                self.par_float.append(float(self.parameters[n+1]))
        except:
            print('ERR: polynomial function: error while converting the parameters')
            return 0

        return 1

    def get_value(self,x,y):
        s = 0
        for n in range(self.order+1):
            s = s*x + self.par_float[n]
        return s
        

class function_generator:
    skip = True

    def __init__(self, function, parameters):
        self.init(function,parameters)

    def init(self,function,parameters):
        if function == 'polynomial':
            self.function = function_polynomial()
        else:
            print('ERR: unknown function:',self.function)
            return 0
        if not self.function.init(parameters):
            print('ERR: function initialisation')
            return 0
        self.skip = False
        return 1
        

    def get_function_value(self,x,y):
        if not self.skip:
            return self.function.get_value(x,y)
        else:
            return float('nan')

# Test unit
if __name__ == '__main__':
    import math

    F = function_generator('polynomial','1:0.1:5')

    for n in range(100):
        y = F.get_function_value(n,1)
        if not math.isnan(y):
            print(n,y)

