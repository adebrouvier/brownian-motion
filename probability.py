import sys
import subprocess
import csv
import math

name, particles, time, filename = sys.argv
with open(filename, 'w') as f:
    csv_writer = csv.writer(f, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
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
    data = range(0,100000,1)
    data = [x/100000.0 for x in data]
    values = [0 for x in range(0, len(data))]
    for x in collisions:
        for i in range(0,len(data)):
            if x > data[i]:
                continue
            values[i] += 1
    values = [x/float(len(collisions)) for x in values]
    print(values)
    
    csv_writer.writerow(['time', 'probability'])
    for i in range(0, len(data)):
        csv_writer.writerow([data[i], values[i]])
