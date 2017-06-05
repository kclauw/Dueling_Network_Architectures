import glob, os,csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def read_files(folder):
    runs = []
    os.chdir(folder)
    for file in glob.glob("*.csv"):
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            steps = []
            values = []
            row1 = next(readCSV)  # First line is header
            for i,row in enumerate(readCSV):
                step = row[1]
                value = row[2]
                #steps.append(step)
                if i < 100:
                    steps.append(step)
                    values.append(float(value))
            runs.append(values)
    return [runs,steps]

def set_plot(values,label,xlabel,ylabel):
    plt.plot(values,label=label)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    leg = plt.legend(loc=4,prop={'size':10},fontsize=30,shadow=True,markerscale=100)
    # set the linewidth of each legend object
    for legobj in leg.legendHandles:
        legobj.set_linewidth(10.0)


def main():

   y_label = sys.argv[2]

   #averages = [float(sum(col))/len(col) for col in zip(*read_files(sys.argv[1]))]
   runs = read_files(sys.argv[1])
   average_runs = [float(sum(col))/len(col) for col in zip(*runs[0])]
   print(average_runs)
   plt.figure()
   plt.plot(average_runs)
   plt.xlabel("Steps", fontsize=18)
   plt.ylabel(y_label, fontsize=18)
   plt.show()
   plt.savefig('plot1.png')




   
  

if __name__ == "__main__":
   main()






