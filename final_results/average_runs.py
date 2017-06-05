import glob, os,csv
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from pylab import *


def runningMean(x, N):
    y = np.zeros((len(x),))
    for ctr in range(len(x)):
         y[ctr] = np.sum(x[ctr:(ctr+N)])
    return y/N



def read_files(folder):
    runs = []
    print("DIRECTORY")
    print(folder)
    os.chdir(folder)
    for file in glob.glob("*.csv"):
        print(file)
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            steps = []
            values = []
            row1 = next(readCSV)  # First line is header
            for i,row in enumerate(readCSV):
                #steps.append(step)
                if i < 270:
                    step = row[1]
                    value = row[2]
                    print(value)
                    steps.append(int(step))
                    values.append(float(value))
            runs.append(values)
    return [runs,steps]

def main():

  

   label_text = sys.argv[1]
   reward_type = sys.argv[2]
   game = sys.argv[3]
   title = sys.argv[4]

 
   current_folder = os.path.dirname(os.path.realpath(__file__))
   fig = plt.figure()
   plot = fig.add_subplot(111)
   plt.title(title,fontsize = 35)
   # We change the fontsize of minor ticks label 
  # We change the fontsize of minor ticks label 
   plot.tick_params(axis='both', which='major', labelsize=10)
   plot.tick_params(axis='both', which='minor', labelsize=10)

   plt.xlabel("Steps", fontsize=20)
   plt.ylabel(sys.argv[1], fontsize=20)
   plt.tick_params(labelsize=20)
   steps = []
   for arg in sys.argv[5:]:
     runs = read_files(current_folder + '/' + reward_type + '/' + game + '/' + arg)
    # plt.legend(handles=[arg])
     average_runs = [float(sum(col))/len(col) for col in zip(*runs[0])]
     rolling_average = np.convolve(average_runs, np.ones((10,))/10, mode='valid')
     print(average_runs)
     steps = runs[1]
     plt.plot(steps[9:],rolling_average ,label=arg,linewidth=5)
     plt.ticklabel_format(style='plain', axis='x', scilimits=(0,0))



   plt.rcParams.update({'font.size': 30})



   leg = plt.legend(loc='upper left',prop={'size':15},fontsize=15,shadow=True,markerscale=100)
    # set the linewidth of each legend object
   for legobj in leg.legendHandles:
        legobj.set_linewidth(10.0)

   fontsize = 30
   ax = gca()
   plt.grid(True)


 
   plt.tick_params(labelsize=20)
   plt.savefig(current_folder + '\ ' + game + ' ' + reward_type + '.pdf',dpi=1800)
   plt.show()
 
   
  



if __name__ == "__main__":
   main()






