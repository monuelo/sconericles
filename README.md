# SCONERICLES


### Prepare the environment

```
sudo docker build -t sconericles:latest .
```

##### Run the image
```
sudo docker run -it --rm --device /dev/isgx --privileged --network=host sconericles:latest /bin/bash
```


### Try to get a memory dump
First select a process to do the memory dump. Let's use `fib.c` as an example.
```
 gcc fib.c -o fib
```

##### Run on sim mode

```
SCONE_ALPINE=1 SCONE_VERSION=1 SCONE_MODE=sim ./fib.c [a large number] > /dev/null & 
```

##### Run on hw mode
```
SCONE_ALPINE=1 SCONE_VERSION=1 SCONE_MODE=hw ./fib.c [a large number] > /dev/null & 
```

Using the `memdump.py` script and the `PID` of the process, run:
```
python3 memdump.py [PID] > fib.dump
```


### Using cast-sh to stream the environment
In the cast-sh directory, run:
```
python3 -m cast
```
> See more about cast-sh [here](https://github.com/hericlesme/cast-sh)
