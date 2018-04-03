import sys
import subprocess
import csv
import math

def probability_calculator(ranges, data):
    values = [0 for x in range(0, len(ranges))]
    for x in data:
        for i in range(0,len(values)):
            if x > ranges[i] and x < ranges[i+1]:
                values[i] += 1
    return values

name, particles, time, q, filename = sys.argv
q = int(q)
with open(filename, 'w') as f:
    csv_writer = csv.writer(f, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    values = [None for x in range(0, q)]
    values_initial = [None for x in range(0, q)]
    for i in range(0, len(values)):
        command = 'java -jar ./target/brownian-motion-1.0-SNAPSHOT-jar-with-dependencies.jar \
        -t {time} -p {particles}'.format(
                time=time,
                particles=particles,
                )
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        lines =  p.stdout.readlines()
        numberOfParticles = int(lines[0])

        speeds = [math.sqrt(float(lines[x].split()[2]) ** 2 + float(lines[x].split()[3]) ** 2)
         for x in range(0, len(lines)) if x % (numberOfParticles + 2) != 0 and x % (numberOfParticles + 2) != 1
         and x % (numberOfParticles + 2) != numberOfParticles and x % (numberOfParticles + 2) != numberOfParticles + 1]
        speeds_initial = speeds[0:numberOfParticles-2]
        speeds = speeds[int((numberOfParticles-2)*2.0/3.0):len(speeds)]
        speeds_initial.sort()
        speeds.sort()

        retval = p.wait()
        values[i] = speeds
        values_initial[i] = speeds_initial

    maxim, minim = 0, 0
    for a in values:
        aux_max = max(a)
        aux_min = min(a)
        if aux_max > maxim:
            maxim = aux_max
        if aux_min < minim:
            minim = aux_mins

    step = maxim - minim
    step = step / 100
    data = [step * x for x in range(0,101)]
    csv_writer.writerow(['ranges'] + data)
    for a in values:
        v = probability_calculator(data, a)
        csv_writer.writerow(['data'] + v)
    csv_writer.writerow([])

    maxim, minim = 0, 0
    for a in values_initial:
        aux_max = max(a)
        aux_min = min(a)
        if aux_max > maxim:
            maxim = aux_max
        if aux_min < minim:
            minim = aux_mins

    step = maxim - minim
    step = step / 100
    data = [step * x for x in range(0,101)]
    csv_writer.writerow(['ranges'] + data)
    for a in values_initial:
        v = probability_calculator(data, a)
        csv_writer.writerow(['data'] + v)
