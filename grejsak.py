#!/usr/bin/env python
import json
import sys
import numpy as np
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt

def main():
    data = {}
    data = load_file(sys.argv[1])
    diagram_of_response_times(data.get("response time"))
    

def load_file(path):
    file = open(path)
    data = json.load(file)
    file.close()
    return data

def diagram_of_response_times(response_times):
    y = []
    x = []
    for i in range(len(response_times)):
        if(response_times[i] == "N/A"):
            y.append(np.nan)
        else:
            y.append(response_times[i])
        x.append(i)
    save_figure(x, y, "test.png")
    

def save_figure(x, y, name):
    plt.figure()
    plt.plot(x, y)
    plt.savefig(name)

if __name__ == "__main__":
    main()
