# This class adds noise to some values
# That noise can be of different types

import random
import math

class noise:
    def __init__(self,ntype,par,rel_abs):
        self.init_parameters(ntype,par,rel_abs)

    def init_parameters(self,ntype,par,rel_abs):
        self.noise_type        = ntype
        self.noise_parameter   = par
        self.relative_absolute = rel_abs

    def uniform(self,y):
        return (y+random.uniform(-self.max,self.max))

    def gauss(self,y):
        return (y+random.gauss(0.0,self.max))

    def noisy(self,y):
        if self.relative_absolute == 'relative':
            self.max = self.noise_parameter*y
        elif self.relative_absolute == 'absolute':
            self.max = self.noise_parameter
        elif self.relative_absolute == 'sqrt':
            self.max = self.noise_parameter*math.sqrt(y)
        else:
            print('ERR: paramter type not known')
            return 0.0

        if self.noise_type == 'uniform':
            return self.uniform(y)
        if self.noise_type == 'gauss':
            return self.gauss(y)
        else:
            return y



# Test unit
if __name__ == '__main__':
    base_value = random.uniform(1,10)
    parameter_abs = random.uniform(0.5,2)
    parameter_rel = random.uniform(0.0,0.2)
    print('#',base_value,parameter_abs,parameter_rel)

    index = 0

    for type_noise in 'uniform gauss'.split(' '):
        for parameter_type in 'relative absolute sqrt'.split(' '):
            if parameter_type == 'relative':
                N = noise(type_noise,parameter_rel,parameter_type)
            elif parameter_type == 'absolute':
                N = noise(type_noise,parameter_abs,parameter_type)
            elif parameter_type == 'sqrt':
                N = noise(type_noise,parameter_rel,parameter_type)
            else:
                print('ERR: parameter type unkown: ',parameter_type)

            for n in range(100):
                print(100*index+n,N.noisy(base_value))

            index += 1

