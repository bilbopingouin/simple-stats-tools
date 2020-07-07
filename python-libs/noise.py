# This class adds noise to some values
# That noise can be of different types

import random
import math


class noise_gauss:
    active = False

    def __init__(self):
        self.active = True

    def get_value(self, v, sigma):
        if self.active:
            return (v+random.gauss(0.0, sigma))

        return float('nan')


class noise_uniform:
    active = False

    def __init__(self):
        self.active = True

    def get_value(self, v, vmax):
        if self.active:
            return (v+random.uniform(-vmax, vmax))

        return float('nan')


class noise:
    skip = True

    def __init__(self, ntype, par, rel_abs):
        self.init(ntype, par, rel_abs)

    def init(self, ntype, par, rel_abs):
        self.noise_parameter = par
        self.relative_absolute = rel_abs

        if ntype == 'uniform':
            self.noise_generator = noise_uniform()
        elif ntype == 'gauss':
            self.noise_generator = noise_gauss()
        else:
            print('ERR: noise generator unknown:', ntype)
            return 0

        self.skip = False

    def noisy(self, y):
        if self.skip:
            return float('nan')

        if self.relative_absolute == 'relative':
            self.max = self.noise_parameter*y
        elif self.relative_absolute == 'absolute':
            self.max = self.noise_parameter
        elif self.relative_absolute == 'sqrt':
            self.max = self.noise_parameter*math.sqrt(y)
        else:
            print('ERR: parameter type not known')
            return float('nan')

        return self.noise_generator.get_value(y, self.max)
