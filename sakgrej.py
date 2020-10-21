import json
import sys
import numpy as np
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt

def main():
    data = {}
    data = LoadFile(sys.argv[1])
    
    responseTimes = data.get("response time")
    expectedAnswers = data.get("expected answer")
    subjectAnswers = data.get("subject answer")

    completeResponseTimes = ClassifyAll(responseTimes, subjectAnswers, expectedAnswers)
    DrawAllLines(completeResponseTimes)

    

def LoadFile(path):
    file = open(path)
    data = json.load(file)
    file.close()
    return data


def ClassifyAll(responseTime, subjectAnswer, expectedAnswer):

    classifiedResponseTimes = {}
    classifiedResponseTimes["tp"] = []
    classifiedResponseTimes["fp"] = []
    classifiedResponseTimes["tn"] = []
    classifiedResponseTimes["fn"] = []

    for i in range(len(subjectAnswer)):
        if(expectedAnswer[i] != "[N/A]" and subjectAnswer[i] != "[N/A]"):
            key = AnswerClassification(subjectAnswer[i], expectedAnswer[i])
            print(key + " | " + str(subjectAnswer[i]) + " | " + str(expectedAnswer[i]))
            classifiedResponseTimes[key].append(responseTime[i])

    return classifiedResponseTimes

def DrawAllLines(responseTimes):
    plt.figure()
    
    index = 0

    for key, values in responseTimes.items():
        x = []
        y = []

        for i in range(len(values)):
            if(values[i] == "N/A"):
                y.append(np.nan)
            else:
                y.append(int(values[i]))
            x.append(i)
        plt.plot(x, y, label = key)
        plt.legend(loc='best')
    plt.show()
    plt.savefig("obunga.png")


def AnswerClassification(opinion, answer):
    
    if opinion == "[b]" and answer == "[b]":
        return "tp"
    elif opinion == "[b]" and answer == "[n]":
        return "fp"
    elif opinion == "[n]" and answer == "[n]":
        return "tn"
    elif opinion == "[n]" and answer == "[b]":
        return "fn"


if __name__ == "__main__":
    main()