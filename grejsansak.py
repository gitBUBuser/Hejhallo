import json
import sys
import numpy as np
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt

def main():
    dataSet = {}
    tempName = {}

    for argument in sys.argv[1:]:
        jsonData = LoadFile(argument)
        argumentLines = argument.split('/')

        tempName[argumentLines[-1]] = []

        answers = {}
        answers["subject"] = jsonData.get("subject answer")
        answers["system"] = jsonData.get("expected answer")

        argumentLines = argument.split('/')

        dataSet[argumentLines[-1]] = answers

    for key, value in dataSet.items():
        subjectAns = value.get("subject")
        systemAns = value.get("system")

        for i in range(len(subjectAns)):
            tempName[key].append(IsCorrect(subjectAns[i], systemAns[i]))
    DrawDiagram(tempName)

            
def DrawDiagram(thing):
    plt.figure()
    plt.figure(figsize=(20,40))
    for key, value in thing.items():
        names = []
        names.append(key + "_R")
        names.append(key + "_W")
        corrFalse= []

        correctAmount = 0
        falseAmount = 0

        for conclusion in value:
            if conclusion:
                correctAmount += 1
            else :
                falseAmount += 1

        corrFalse.append(correctAmount)
        corrFalse.append(falseAmount)
        plt.barh(names[0], corrFalse[0], color='Green')
        plt.barh(names[1], corrFalse[1], color='Red')
    plt.savefig("sn��llafunka.png")



def LoadFile(path):
    file = open(path)
    data = json.load(file)
    file.close()
    return data

def IsCorrect(response, answer):
    if response == answer:
        return True
    return False


if __name__ == "__main__":
    main()
