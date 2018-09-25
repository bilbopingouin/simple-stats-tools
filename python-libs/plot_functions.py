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

class plot_function(object):
    def __init__(self):
        self.init('')

    def init(self,function_name):
        self.parameters    = []
        self.function_name = function_name

    def init_parameters(self,*arg):
        for a in arg:
            self.parameters.append(a)
    
    def parameters_to_string(self):
        self.parameters_str = ''
        for a in self.parameters:
            self.parameters_str += str(a)+':'
        self.parameters_str = self.parameters[:-1]
            
    def load_dataset(self,xvector,yvector):
        self.xvector = xvector
        self.yvector = yvector

    def init_function(self):
        self.function = function_generator(self.function_name,self.parameters_str)
