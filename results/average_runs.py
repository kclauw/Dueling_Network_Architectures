import glob, os,csv
import sys
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go


def read_files(folder):
    runs = []
    print("DIRECTORY")
    print(folder)
    os.chdir(folder)
    for file in glob.glob("*.csv"):
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            steps = []
            values = []
            row1 = next(readCSV)  # First line is header
            for i,row in enumerate(readCSV):
                #steps.append(step)
                if i < 250:
                    step = row[1]
                    value = row[2]
                    steps.append(step)
                    values.append(float(value))
            runs.append(values)
    return [runs,steps]

def main():


   current_folder = os.path.dirname(os.path.realpath(__file__))
   #plt.figure()
   #plt.xlabel("Steps", fontsize=18)
  # plt.ylabel(sys.argv[1], fontsize=18)
   data = []
   for arg in sys.argv[2:]:
     runs = read_files(current_folder + arg)
     average_runs = [float(sum(col))/len(col) for col in zip(*runs[0])]
     steps = runs[1]
     trace = go.Scatter(
      x = steps,
      y = average_runs,
      mode = 'lines',
      name = 'lines')
     data.append(trace)

 

     #plt.plot(steps,average_runs)
   
   #plt.show()
   #np.savetxt('test.csv', (average_runs), delimiter=',')
   # Create traces
    # Create traces

   




   
  

if __name__ == "__main__":
   main()






