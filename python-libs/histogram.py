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
        self.array[int((v-v%self.step)/(self.step))] += 1

    def print_array(self):
        print(self.array)

    def print(self):
        for i in range(len(self.array)):
           print(i*self.step+0.5*self.step+self.min,self.array[i]) 
