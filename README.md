# brownian-motion
Implementation of the Brownian Motion system.

## Compilation
```
mvn package
```

## Execution

```
target/brownian-motion-1.0-SNAPSHOT-jar-with-dependencies.jar -p 100 -t 100 
```
Parameters:

* **-h, --help**: Shows the help.
* **-p, --particles &lt;arg>**: Number of particles.
* **-T, --temperature &lt;arg>**: Initial temperature of the system.
* **-t, --time &lt;arg>**: Total time of the simulation.

## Python scripts

This python script returns a csv file contained in the same folder. The name of the file is {filename}.


### Generate data to create an histogram for time

```
python histogram_data.py {particles} {time} {number of simulations} {filename}
```

### Probability of collisions

```
python probability.py {particles} {time} {filename}
```

### Generate data to create an histogram for speeds

```
python probability_speeds_hist.py {particles} {time} {number of simulations} {filename}
```

### Probability of speeds

```
python probability_speeds.py {particles} {time} {number of simulations} {filename}
```
