# This class can generate various functions.

import math

#-----------------------------------------------------

class function_generic(object):

    def __init__(self):
        self.active           = False
        self.parameter_float  = []
        self.parameter_number = 2
        self.function_name    = 'generic'

    def init(self,parameters):
        self.parameters = parameters.split(':')

        if len(self.parameters) != self.parameter_number:
            print('ERR:',self.function_name,'function parameters number:',parameters)
            return 0

        print('#',self.parameters)

        #self.parameter_float = []
        try:
            for p in self.parameters:
                self.parameter_float.append(float(p))
        except:
            print('ERR:',self.function_name,'function parameters format:',parameters)
            return 0

        self.active = True
        return 1

    def function(self,x,y):
        return 0

    def get_value(self,x,y):
        if not self.active:
            return float('nan')

        return self.function(x,y)

class function_polynomial(object):
    def __init__(self):
        self.active = False

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

        self.active = True
        return 1

    def get_value(self,x,y):
        if not self.active:
            return float('nan')

        s = 0
        for n in range(self.order+1):
            s = s*x + self.par_float[n]
        return s
        
class function_sine(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 3
        self.function_name    = 'Sine'

    def function(self,x,y):
        return self.parameter_float[0]*math.sin(2*math.pi*self.parameter_float[1]*(x-self.parameter_float[2]))

class function_exp(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 2
        self.function_name    = 'Exponential'

    def function(self,x,y):
        return self.parameter_float[0]*math.exp(-self.parameter_float[1]*x)

class function_gauss(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 3
        self.function_name    = 'Gauss'

    def function(self,x,y):
        return self.parameter_float[0]*math.exp(-(x-self.parameter_float[2])*(x-self.parameter_float[2])/(self.parameter_float[1]*self.parameter_float[1]))

#-----------------------------------------------------

class function_generator:
    skip = True

    def __init__(self, function, parameters):
        self.init(function,parameters)

    def init(self,function,parameters):
        if function == 'polynomial':
            self.function = function_polynomial()
        elif function == 'sine':
            self.function = function_sine()
        elif function == 'exponential':
            self.function = function_exp()
        elif function == 'gauss':
            self.function = function_gauss()
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
    xbasis = 0

    functions = ['polynomial','polynomial','sine','exponential','gauss']
    parameters= ['1:0.1:5','2:0.002:-0.3:1','5:0.1:0.5','10:0.2','10:10:50']

    for n in range(len(functions)):
        print('#Processing:',functions[n],parameters[n])
        F = function_generator(functions[n],parameters[n])

        for n in range(100):
            y = F.get_function_value(n,1)
            if not math.isnan(y):
                print(n+xbasis*100,y)

        xbasis += 1

