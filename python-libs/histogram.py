#  This create an array to plot an histogram as
#   ^
#   |       +-+
#   |     +-+ | +-+
#   |     | | +-+ |
#   |   +-+ | | | +-+
#   |   | | | | | | +-+
#   +---+-+-+-+-+-+-+-+------->
#      Vm            Vmax


class histogram:
    def __init__(self,vmin,vmax,nbins):
        self.init_values(vmin,vmax,nbins)

    def init_values(self,vmin,vmax,nbins):
        self.array = [0] * nbins
        self.min = vmin
        self.max = vmax
        self.step = float(vmax-vmin)/float(nbins)

    def add_value(self,v):
        bin_idx = int(((v-self.min)-(v-self.min)%self.step)/(self.step))
        self.array[bin_idx] += 1

    def print_array(self):
        print(self.array)

    def print(self):
        for i in range(len(self.array)):
           print(i*self.step+0.5*self.step+self.min,self.array[i]) 

# Test unit
if __name__ == '__main__':
    import random

    # Basic histogram
    vmin = random.uniform(0,5)
    vmax = random.uniform(5,20)
    nbins= random.randint(7,20)

    print('#',vmin,vmax,nbins)

    H = histogram(vmin,vmax,nbins)

    for n in range(200):
        H.add_value(random.uniform(vmin,vmax))

    H.print()
