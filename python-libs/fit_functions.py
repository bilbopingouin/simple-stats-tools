# basic libs
import os
import sys

# local directory to path
path=os.path.dirname(__file__)
if not path:
    path='.'
sys.path.append(path+'/../python-libs/')

# local libs
from function_generator import function_generator,parameters_function_numbers

# Other libs
from scipy.optimize import curve_fit

class fit_function(object):
    def __init__(self):
        self.init('')
        self.active = False

    def init(self,function_name):
        self.parameters    = []
        self.function_name = function_name

    def init_parameters(self,*arg):
        #print('#',arg)
        self.parameters = []
        for a in arg:
            self.parameters.append(a)
        #print('#',self.parameters)
        
    
    def parameters_to_string(self):
        self.parameters_str = ''
        for a in self.parameters:
            self.parameters_str += str(a)+':'
        self.parameters_str = self.parameters_str[:-1]
            
    def load_dataset(self,xvector,yvector):
        self.xvector = xvector
        self.yvector = yvector

    def init_function(self):
        if self.function_name != 'polynomial':
            if len(self.parameters) != int(parameters_function_numbers[self.function_name]):
                self.parameters = []
                for n in range(int(parameters_function_numbers[self.function_name])):
                    self.parameters.append(1)
            
        self.parameters_to_string()
        
        self.active = True
    
        self.function = function_generator(self.function_name,self.parameters_str)
    
    def func(self, x, *arg):
        self.parameters = []
        for a in arg:
            self.parameters.append(a)
        #print('# x=',x,', arg=',arg,', =',self.parameters)
        #self.init_parameters(arg)
        self.parameters_to_string()
        self.function.function.init(self.parameters_str)
        return self.function.get_function_array(x,x)
        
    def fit(self):
        if self.active:
            popt, pcov = curve_fit(f=self.func, xdata=self.xvector, ydata=self.yvector, p0=self.parameters)
            print('Fit successfull with parameters: ',popt,' and covariance\n',pcov,'')
            return popt


# Test unit
if __name__ == '__main__':
    from noise import noise
    N = noise('gauss',4.0,'absolute')
    F = function_generator('sine','10:0.0001:2')

    xv = []
    yv = []

    for n in range(1000):
        xv.append(n)
        yv.append(N.noisy(F.get_function_value(n,1)))

    ffit = fit_function()
    ffit.init('sine')
    ffit.init_function()
    ffit.load_dataset(xv,yv)

    ffit.fit()


