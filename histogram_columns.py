import sys
import csv
import math

with open(sys.argv[1], 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        row.pop(0)
        row = [float(x) for x in row]
        length = math.ceil(sum(row))
        data = [0 for x in range(0,length)]
        time = 0
        for x in data:
            time += x
            data[math.floor(time)] += 1
        print(data)
