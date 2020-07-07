# This class can generate various functions.

import math

# -----------------------------------------------------


class function_generic(object):

    def __init__(self):
        self.active = False
        self.parameter_float = []
        self.parameter_number = 2
        self.function_name = 'generic'

    def init(self, parameters):
        self.parameters = parameters.split(':')

        if len(self.parameters) != self.parameter_number:
            print(
                'ERR:',
                self.function_name,
                'function parameters number:',
                len(self.parameters),
                'expected:',
                self.parameter_number,
                '(', parameters, ')')
            return 1

        print('#', self.parameters)

        try:
            for p in self.parameters:
                self.parameter_float.append(float(p))
        except ValueError:
            print('ERR:', self.function_name,
                  'function parameters format:', parameters)
            return 2

        self.active = True
        return 0

    def function(self, x, y):
        return 0

    def get_value(self, x, y):
        if not self.active:
            return float('nan')

        return self.function(x, y)


class function_polynomial(object):
    def __init__(self):
        self.active = False

    def init(self, parameters):
        self.parameters = parameters.split(':')

        if len(self.parameters) < 2:
            print('ERR: parameters of polynomial function not fitting')
            return 2

        try:
            self.order = int(self.parameters[0])
        except ValueError as verr:
            print('ERR: polynomial order not correct:', end=' ')
            print(verr)
            return 3

        if len(self.parameters) != self.order+2:
            print('ERR: polynomial number of parameters not correct')
            return 4

        self.par_float = []

        try:
            for n in range(len(self.parameters)-1):
                self.par_float.append(float(self.parameters[n+1]))
        except ValueError as verr:
            print(
                'ERR: polynomial function: error while converting the'
                'parameters: ',
                end=' '
            )
            print(verr)
            return 5

        self.active = True
        return 0

    def get_value(self, x, y):
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
        self.function_name = 'Sine'

    def function(self, x, y):
        return (
            self.parameter_float[0]*math.sin(2*math.pi*self.parameter_float[1]
                                             * (x-self.parameter_float[2]))
        )


class function_exp(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 2
        self.function_name = 'Exponential'

    def function(self, x, y):
        return self.parameter_float[0]*math.exp(-self.parameter_float[1]*x)


class function_gauss(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 3
        self.function_name = 'Gauss'

    def function(self, x, y):
        return (
            self.parameter_float[0]
            * math.exp(-(x-self.parameter_float[2])
                       * (x-self.parameter_float[2])
                       / (self.parameter_float[1] * self.parameter_float[1]))
        )


class function_poisson(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 2
        self.function_name = 'Poisson'

    def function(self, x, y):
        lambda_parameter = self.parameter_float[1]
        return (
            self.parameter_float[0]
            * math.exp(-lambda_parameter)
            * (lambda_parameter**(int(x)))/(math.factorial(x))
        )


class function_log(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 2
        self.function_name = 'Log'

    def function(self, x, y):
        return self.parameter_float[0]*math.log(self.parameter_float[1]+x)


class function_sqrt(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 2
        self.function_name = 'Sqrt'

    def function(self, x, y):
        return self.parameter_float[0]*math.sqrt(self.parameter_float[1]+x)


class function_inverse(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 2
        self.function_name = 'Inverse'

    def function(self, x, y):
        return self.parameter_float[0]*(1.0/(self.parameter_float[1]+x))


class function_identity(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 1
        self.function_name = 'Identity'

    def function(self, x, y):
        return x


class function_window_average(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 1
        self.function_name = 'Window moving average'
        self.window = []

    def add_to_window(self, y):
        if len(self.window) < self.parameter_float[0]:
            self.window.append(y)
        else:
            for n in range(int(self.parameter_float[0])-1):
                self.window[n] = self.window[n+1]
            self.window[int(self.parameter_float[0]-1)] = y

    def function(self, x, y):
        self.add_to_window(y)
        return sum(self.window)/len(self.window)


class function_factored_moving_average(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 1
        self.function_name = 'Factored moving average'
        self.sum_v = 0

    def function(self, x, y):
        self.sum_v = (
            self.parameter_float[0]*self.sum_v+y)/(self.parameter_float[0]+1)
        return self.sum_v


class function_cumulative_average(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 1
        self.function_name = 'Cumulative average'
        self.sum_v = 0
        self.sum_n = 0

    def function(self, x, y):
        self.sum_v = (self.sum_n*self.sum_v+y)/(self.sum_n+1)
        self.sum_n += 1
        return self.sum_v


class function_quadratic_moving_average(function_generic):
    def __init__(self):
        super().__init__()
        self.parameter_number = 1
        self.function_name = 'Quadratic moving average'
        self.sum_v = 0

    def function(self, x, y):
        self.sum_v = (
            self.parameter_float[0]*self.sum_v+y*y)/(self.parameter_float[0]+y)
        return self.sum_v

# -----------------------------------------------------


class function_generator(object):
    skip = True

    def __init__(self, function, parameters):
        self.init(function, parameters)

    def init(self, function, parameters):
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
        elif function == 'identity':
            self.function = function_identity()
        elif function == 'window':
            self.function = function_window_average()
        elif function == 'cumulative':
            self.function = function_cumulative_average()
        elif function == 'factored':
            self.function = function_factored_moving_average()
        elif function == 'quadratic':
            self.function = function_quadratic_moving_average()
        else:
            print('ERR: unknown function:', function)
            return 1
        if 0 != self.function.init(parameters):
            print('ERR: function initialisation')
            return 2
        self.skip = False
        return 0

    def get_function_value(self, x, y):
        if not self.skip:
            return self.function.get_value(x, y)

        return float('nan')
