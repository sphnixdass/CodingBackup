import numpy as np
import csv
import os
from string import digits 


def removedigit(tempstr):
    remove_digits = str.maketrans('', '', digits) 
    return tempstr.translate(remove_digits).lower().replace("  "," ").replace("."," ").replace("{"," ").replace("}"," ").replace(","," ").replace("("," ").replace(")"," ").replace("\n"," ").replace("\r"," ").replace("\n\r"," ").replace("\r\n."," ").replace("  "," ")

def levenshtein_ratio_and_distance(s, t, ratio_calc = False):

    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])

def mainprocesscal():
    temp1 = []
    BBCAvector = []
    NONBBCAvector = []
    Inputvector = []
    Resultvector = []
    vectorinner = []


    if not os.path.exists("uniqueid.csv"):
        f = open("uniqueid.csv", "w")
        f.write("")
        f.close()

    f = open("uniqueid.csv", "r")
    temp1 = f.read().split('\n')

    with open('BBCA.csv', newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    for x in your_list:
        x2 = str(removedigit(x[0])).split()
        vectorinner = []
        for x3 in x2:
            if x3.lower() not in temp1:
                print(x3)
                temp1.append(x3.lower())
                f = open("uniqueid.csv", "a")
                f.write(str(x3.lower()) + "\n")
                f.close()
                vectorinner.append(len(temp1))
            else:
                vectorinner.append(temp1.index(x3.lower()))
        BBCAvector.append(vectorinner)

    with open('NONBBCA.csv', newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    for x in your_list:
        x2 = str(removedigit(x[0])).split()
        vectorinner = []
        for x3 in x2:
            if x3.lower() not in temp1:
                print(x3)
                temp1.append(x3.lower())
                f = open("uniqueid.csv", "a")
                f.write(str(x3.lower()) + "\n")
                f.close()
                vectorinner.append(len(temp1))
            else:
                vectorinner.append(temp1.index(x3.lower()))
        NONBBCAvector.append(vectorinner)

    with open('input.csv', newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    for x in your_list:
        x2 = str(removedigit(x[0])).split()
        vectorinner = []
        for x3 in x2:
            if x3.lower() not in temp1:
                print(x3)
                temp1.append(x3.lower())
                f = open("uniqueid.csv", "a")
                f.write(str(x3.lower()) + "\n")
                f.close()
                vectorinner.append(len(temp1))
            else:
                vectorinner.append(temp1.index(x3.lower()))
        Inputvector.append(vectorinner)



    for ix in Inputvector:
        resultcountmax = 0
        tempresult1 = [0]
        tempresult1a = [0]
        j = 0
        for ib in BBCAvector:
            resultcounttemp = 0
            j = j + 1
            for ix2 in ix:
                if ix2 in ib:
                    resultcounttemp = resultcounttemp + 1
                if resultcounttemp > resultcountmax:
                    tempresult1[0] = j
                    tempresult1a[0] = resultcounttemp
                    resultcountmax = resultcounttemp

        resultcountmax2 = 0
        tempresult2 = [0]
        tempresult2a = [0]
        j = 0
        for ib in NONBBCAvector:
            resultcounttemp = 0
            j = j + 1
            for ix2 in ix:
                if ix2 in ib:
                    resultcounttemp = resultcounttemp + 1
                if resultcounttemp > resultcountmax2:
                    tempresult2[0] = j
                    tempresult2a[0] = resultcounttemp
                    resultcountmax2 = resultcounttemp

        tempres = "Unable to identify"
        if tempresult1a[0] > tempresult2a[0]:
            tempres = "BBCA"
        elif tempresult1a[0] < tempresult2a[0]:
            tempres = "NONBBCA"
        else:
            tempres = "Unable to identify"
        Resultvector.append([tempres, tempresult1,tempresult1a, tempresult2, tempresult2a])


    print(Inputvector)
    print(BBCAvector[1])
    print(Resultvector[0])

mainprocesscal()




