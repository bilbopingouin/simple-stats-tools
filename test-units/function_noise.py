# basic libs
import os
import sys

# local directory to path
path=os.path.dirname(__file__)
if not path:
    path='.'
sys.path.append(path+'/../python-libs/')

# local libs
from function_generator import function_generator
from noise import noise

if __name__ == '__main__':
    N = noise('gauss',4.0,'absolute')
    F = function_generator('sine','10:0.0001:2')

    for n in range(1000):
        print(n,N.noisy(F.get_function_value(n,1)))


