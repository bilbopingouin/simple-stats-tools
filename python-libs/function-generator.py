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
            print('ERR:',self.function_name,'function parameters number:',len(self.parameters),'expected:',self.parameter_number,'(',parameters,')')
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

class function_poisson(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number  = 2
        self.function_name     = 'Poisson'

    def function(self,x,y):
        l = self.parameter_float[1]
        return self.parameter_float[0]*math.exp(-l)*(l**(int(x)))/(math.factorial(x)) 

class function_log(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number  = 2
        self.function_name     = 'Log'

    def function(self,x,y):
        return self.parameter_float[0]*math.log(self.parameter_float[1]+x) 

class function_sqrt(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number  = 2
        self.function_name     = 'Sqrt'

    def function(self,x,y):
        return self.parameter_float[0]*math.sqrt(self.parameter_float[1]+x) 

class function_inverse(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number  = 2
        self.function_name     = 'Inverse'

    def function(self,x,y):
        return self.parameter_float[0]*(1.0/(self.parameter_float[1]+x))

class function_window(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 1
        self.function_name    = 'Window average'
        self.window           = []

    def add_to_window(self,y):
        if len(self.window) < self.parameter_float[0]:
            self.window.append(y)
        else:
            for n in range(int(self.parameter_float[0])-1):
                self.window[n] = self.window[n+1]
            self.window[int(self.parameter_float[0]-1)] = y

    def function(self,x,y):
        self.add_to_window(y)
        return sum(self.window)/len(self.window)
        

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
        elif function == 'poisson':
            self.function = function_poisson()
        elif function == 'log':
            self.function = function_log()
        elif function == 'sqrt':
            self.function = function_sqrt()
        elif function == 'inverse':
            self.function = function_inverse()
        elif function == 'window':
            self.function = function_window()
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

    # Using: https://stackoverflow.com/questions/32111941/r-how-to-generate-a-noisy-sine-function#32112610
    yvalues =   [
                     0.82982774,  2.24736614,  2.65015416, 
                     3.46682674,  3.52729297,  3.49584034,  
                     3.21650125,  4.36715717,  3.33775743, 
                     4.25865056,  3.08154581,  1.29021692,
                     1.29727107,  0.18405785,  0.54038839, 
                    -1.56588876, -1.12647564, -2.22541481,
                    -1.73397892, -1.47479364, -2.78684092, 
                    -0.71941248, -1.18848838, -1.14310578,
                     0.99296343,  1.96275316,  2.21877083, 
                     1.82625195,  3.56494503,  4.58475139,
                     3.43430470,  4.96176449,  4.05305860, 
                     3.47720003,  3.12880561,  1.63220985,
                     2.47756490,  0.32653887,  0.04058271, 
                    -0.27735692, -1.00248342, -2.03402250,
                    -1.99755668, -1.76619781, -2.03965488, 
                    -2.48876795, -1.17858836, -0.83329113,
                     0.41488879,  0.50468218,  1.12150799, 
                     1.68485862,  2.28072161,  3.96888097,
                     2.91623328,  3.34443738,  3.09313796, 
                     3.28688135,  3.72462122,  2.96415418,
                     1.85136958,  2.62886448,  1.13530004, 
                     0.27470068, -0.12288578, -1.15473463,
                    -2.15411720, -1.00004169, -2.54632330, 
                    -1.92948988, -1.29557262, -1.53368721,
                    -1.04163048, -0.20596297,  1.77020757, 
                     2.41725266,  1.92812607,  2.81425263,
                     3.74461982,  3.47113171,  3.01444636, 
                     4.55037931,  2.80800815,  4.33598397,
                     3.66507070,  2.72017885,  2.17351610, 
                     0.75793812,  0.25465984, -1.62278327,
                    -1.04956540, -0.86896317, -1.34327100, 
                    -2.07355078, -1.00718962, -1.08180038,
                    -1.25338040, -1.03877604,  1.12414670, 
                     0.24223937
                ]

    functions = [
                    ['polynomial',  '1:0.1:5'], 
                    ['polynomial',  '2:0.002:-0.3:1'],
                    ['sine',        '5:0.1:0.5'],
                    ['exponential', '10:0.2'],
                    ['gauss',       '10:10:50'],
                    ['poisson',     '10:4'],
                    ['log',         '5:2'],
                    ['sqrt',        '0.5:5'],
                    ['inverse',     '10:5'],
                    ['window',      '5']
                ]

    for n in range(len(functions)):
        print('#Processing:',functions[n][0],functions[n][1])
        F = function_generator(functions[n][0],functions[n][1])

        for n in range(100):
            y = F.get_function_value(n,yvalues[n])
            if not math.isnan(y):
                print(n+xbasis*100,y)

        xbasis += 1

