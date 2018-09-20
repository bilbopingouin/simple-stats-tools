# This class adds noise to some values
# That noise can be of different types

import random
import math

class noise_gauss:
    active = False

    def __init__(self):
        self.active = True

    def get_value(self,v,sigma):
        if self.active:
            return (v+random.gauss(0.0,sigma))
        else:
            return float('nan')
 
class noise_uniform:
    active = False

    def __init__(self):
        self.active = True

    def get_value(self,v,vmax):
        if self.active:
            return (v+random.uniform(-vmax,vmax))
        else:
            return float('nan')
        

class noise:
    skip = True

    def __init__(self,ntype,par,rel_abs):
        self.init(ntype,par,rel_abs)

    def init(self,ntype,par,rel_abs):
        self.noise_parameter    = par
        self.relative_absolute  = rel_abs

        if ntype == 'uniform':
            self.noise_generator = noise_uniform()
        elif ntype == 'gauss':
            self.noise_generator = noise_gauss()
        else:
            print('ERR: noise generator unknown:',ntype)
            return 0

        self.skip = False

    def noisy(self,y):
        if self.skip:
            return float('nan')

        if self.relative_absolute == 'relative':
            self.max = self.noise_parameter*y
        elif self.relative_absolute == 'absolute':
            self.max = self.noise_parameter
        elif self.relative_absolute == 'sqrt':
            self.max = self.noise_parameter*math.sqrt(y)
        else:
            print('ERR: paramter type not known')
            return float('nan')

        return self.noise_generator.get_value(y,self.max)




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

