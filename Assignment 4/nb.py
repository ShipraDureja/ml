"""
[Monday 13-15] ML Programming Assignment 4
Tarun Gupta, Shipra Dureja
Command to run this batch gradient descent model:
python3 nb.py --data <filepath> --output <output file>
Input: tsv File
Output: tsv File
"""

import argparse
import csv
import math

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--data', help='Data File')
parser.add_argument('-o', '--output', help='Output File')

args = parser.parse_args()
file, outputFile = args.data, args.output

with open(file) as tsvFile:
    reader = csv.reader(tsvFile, delimiter='\t')
    data = []
    data_temp = []
    X = []
    Y = []
    for row in reader:
        if(row.__contains__('')):
            row.remove('')
        col = len(row)
        data_temp = []
        for i in range(0, col):
            if(i==0):
                data_temp.append(row[i])
            else:
                data_temp.append(float(row[i]))
        data.append(data_temp)

    for i in range(len(data)):
        if (data[i][0] == 'A'):
            X.append(data[i])
        else:
            Y.append(data[i])


rows = len(data)
lenA = len(X)
lenB = len(Y)

probA = lenA / rows
probB = lenB / rows

x1, x2, x3, x4 = 0, 0, 0, 0
for i in range(0,lenA):
    x1 = x1 + float(X[i][1])
    x2 = x2 + float(X[i][2])
meanA_att1 = x1/lenA
meanA_att2 = x2/lenA

for i in range(0,lenB):
    x3 = x3 + float(Y[i][1])
    x4 = x4 + float(Y[i][2])
meanB_att1 = x3/lenB
meanB_att2 = x4/lenB

att1_A, att2_A, att1_B, att2_B = 0, 0, 0, 0
for i in range (0,lenA):
    att1_A = att1_A + pow((float(X[i][1]) - meanA_att1), 2)
    att2_A = att2_A + pow((float(X[i][2]) - meanA_att2), 2)
varianceA_att1 = att1_A/(lenA - 1)
varianceA_att2 = att2_A /(lenA - 1)

for i in range (0,lenB):
    att1_B = att1_B + pow((float(Y[i][1]) - meanB_att1), 2)
    att2_B = att2_B + pow((float(Y[i][2]) - meanB_att2), 2)
varianceB_att1 = att1_B/(lenB - 1)
varianceB_att2 = att2_B /(lenB - 1)

misc = 0
for i in range(rows):
    probx1_A = (math.exp(-(math.pow(data[i][1] - meanA_att1, 2) / (2 * varianceA_att1)))) / (math.sqrt(2 * math.pi * varianceA_att1))
    probx1_B = (math.exp(-(math.pow(data[i][1] - meanB_att1, 2) / (2 * varianceB_att1)))) / (math.sqrt(2 * math.pi * varianceB_att1))
    probx2_A = (math.exp(-(math.pow(data[i][2] - meanA_att2, 2) / (2 * varianceA_att2)))) / (math.sqrt(2 * math.pi * varianceA_att2))
    probx2_B = (math.exp(-(math.pow(data[i][2] - meanB_att2, 2) / (2 * varianceB_att2)))) / (math.sqrt(2 * math.pi * varianceB_att2))

    prob_A = probx1_A * probx2_A
    prob_B = probx1_B * probx2_B
    classification = ""
    if prob_A > prob_B:
        classification = "A"
    else:
        classification = "B"
    if data[i][0] != classification:
        misc = misc + 1

with open(outputFile, 'w', newline='') as tsvFile:
    writer = csv.writer(tsvFile, delimiter='\t')
    writer.writerow([meanA_att1, varianceA_att1, meanA_att2, varianceA_att2, probA])
    writer.writerow([meanB_att1, varianceB_att1, meanB_att2, varianceB_att2, probB])
    writer.writerow([misc])
