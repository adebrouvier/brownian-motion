import sys
import subprocess
import csv
import math
name, particles, time, q, filename = sys.argv
q = int(q)
with open(filename, 'w') as f:
    csv_writer = csv.writer(f, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, q):
        values = ['collisions {}'.format(i + 1)]
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
        length = int(math.ceil(sum(collisions)))
        data = [0 for x in range(0,length)]
        t = 0
        for x in collisions:
            t += x
            data[int(math.floor(t))] += 1
        values = values + data
        csv_writer.writerow(values)
