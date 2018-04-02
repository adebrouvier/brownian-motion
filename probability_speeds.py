import sys
import subprocess
import csv
import math

def probability_calculator(ranges, data):
    values = [0 for x in range(0, len(ranges))]
    for x in data:
        for i in range(0,len(ranges)):
            if x > ranges[i]:
                continue
            values[i] += 1
    values = [x/float(len(data)) for x in values]
    return values

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

    times = [float(lines[x]) for x in range(0, len(lines)) if x % (numberOfParticles + 2) == 1]
    time = times[len(times)/3]

    speeds = [math.sqrt(float(lines[x].split()[3]) ** 2 + float(lines[x].split()[4]) ** 2)
     for x in range(0, len(lines)) if x % (numberOfParticles + 2) != 0 and x % (numberOfParticles + 2) != 1
     and x % (numberOfParticles + 2) != numberOfParticles and x % (numberOfParticles + 2) != numberOfParticles + 1]
    speeds_initial = speeds[0:numberOfParticles-2]
    speeds = [speeds[x] for x in range(0, len(speeds)) if x/(numberOfParticles-2) > time]
    speeds_initial.sort()
    speeds.sort()

    retval = p.wait()
    print('SPEEDS AVERAGE:' + str(sum(speeds)/len(speeds)))
    print('SPEEDS INITIAL AVERAGE:' + str(sum(speeds_initial)/len(speeds_initial)))

    range_speeds = range(0,10000,1)
    range_speeds = [speeds[-1] * x/10000.0 for x in range_speeds]
    values = probability_calculator(range_speeds, speeds)
    range_speeds_initial = range(0,10000,1)
    range_speeds_initial = [speeds_initial[-1] * x/10000.0 for x in range_speeds_initial]
    values_initial = probability_calculator(range_speeds_initial, speeds_initial)

    csv_writer.writerow(['x_initial', 'probability', 'x_speed', 'probability'])
    for i in range(0, len(range_speeds)):
        csv_writer.writerow([range_speeds_initial[i], values_initial[i], range_speeds[i], values_initial[i]])
