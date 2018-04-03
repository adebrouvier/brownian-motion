import sys
import subprocess
import csv
import math
name, particles, time, q, filename = sys.argv
q = int(q)

with open(filename, 'w') as f:
    csv_writer = csv.writer(f, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    values = [None for x in range(0, q)]
    for i in range(0, len(values)):
        command = 'java -jar ./target/brownian-motion-1.0-SNAPSHOT-jar-with-dependencies.jar \
        -t {time} -p {particles}'.format(
                time=time,
                particles=particles,
                )
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        lines =  p.stdout.readlines()
        numberOfParticles = int(lines[0])

        collisions = [float(lines[x].split()[-1]) for x in range(0, len(lines)) if x % (numberOfParticles + 2) == 2]
        retval = p.wait()
        collisions.sort()
        values[i] = collisions

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
    data = ['interval'] + data
    csv_writer.writerow(data)
    for a in values:
        v = [0 for x in range(0,100)]
        print(sum(a)/len(a))
        for x in a:
            for i in range(0, len(v)):
                if x > data[i] and x < data[i + 1]:
                    v[i] += 1
        v = ['times'] + v
        csv_writer.writerow(v)
