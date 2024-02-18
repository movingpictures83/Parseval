import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fftpack

class ParsevalPlugin:
   def input(self, inputfile):
       tfile = open(inputfile, 'r')
       mylist = []
       for line in tfile:
          mylist.append(float(line.strip()))
       self.tdata = np.array(mylist)

   def run(self):
       pi = np.pi
       dt = self.tdata[1]-self.tdata[0]

       datay = np.sin(pi*self.tdata)+2*np.sin(pi*2*self.tdata)
       N = len(datay)

       fouriery = abs(fftpack.rfft(datay))/N

       freqs = fftpack.rfftfreq(len(datay), d=(self.tdata[1]-self.tdata[0]))

       df = freqs[1] - freqs[0]

       self.parceval = sum(datay**2)*dt - sum(fouriery**2)*df

   def output(self, outputfile):
       print(self.parceval)

