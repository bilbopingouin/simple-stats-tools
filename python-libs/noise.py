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

    def noisy(self,x,y):
        if self.relative_absolute == 'relative':
            self.max = self.noise_parameter*y
        elif self.relative_absolute == 'absolute':
            self.max = self.noise_parameter
        elif self.relative_absolute == 'sqrt':
            self.max = self.parameter*math.sqrt(y)
        else:
            print('ERR: paramter type not known')
            return 0.0

        if self.noise_type == 'uniform':
            return self.uniform(y)
        else:
            return y



# Test unit
if __name__ == '__main__':
    parameter = random.uniform(0.5,2)
    N = noise('uniform',parameter,'relative')

    print('#',parameter)
    for n in range(100):
        print(n,N.noisy(n,1.0))

