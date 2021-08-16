import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)

newdata = []

for i in range(len(filedata)):
    height = filedata[i][1]
    newdata.append(float(height))

n = len(newdata)
total = 0

for i in newdata:
    total += i

mean = total / n
print(mean)


    