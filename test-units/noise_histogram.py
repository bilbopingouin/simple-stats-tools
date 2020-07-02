# basic libs
from noise import noise
from histogram import histogram
import os
import sys

# local directory to path
path = os.path.dirname(__file__)
if not path:
    path = '.'
sys.path.append(path+'/../python-libs/')

# local libs

if __name__ == '__main__':
    N = noise('gauss', 2.0, 'absolute')
    H = histogram(0.0, 10.0, 20)

    for n in range(1000):
        H.add_value(N.noisy(5.0))

    H.print()
