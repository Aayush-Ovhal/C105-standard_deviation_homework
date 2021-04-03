import csv
import math

with open("std_deviation.csv", newline='') as f:
      reader = csv.reader(f)
      fileData = list(reader)

newData = fileData[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total/n
    return mean

squareNo = []

for n in newData:
    a = int(n) - mean(newData)
    a = a**2
    squareNo.append(a)

sum = 0
for j in squareNo:
    sum = sum + j

result = sum/(len(newData)-1)

std_dev = math.sqrt(result)
print("standard deviation is: " + str(std_dev))
