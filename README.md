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


##### Get the PID and dump

```
SPID=$(ps -a | grep -v grep | grep [process name] | awk  '{print $1}')
```


Using the `dumpstack.py` script and the `PID` of the process, run:
```
python dumpstack.py $SPID | strings -n [min-size] | grep [secret]
```

Using the `memdump.py` script and the `PID` of the process, run:
```
python3 memdump.py $SPID > fib.dump
```


#### Extra: Flask-API
```
python3 flask-api.py
```

```
curl -X POST -H "Content-Type: application/json" \
 -d '{"test":"ThisIsASecret"}' \
 http://localhost:5000
```

### Using cast-sh to stream the environment
In the cast-sh directory, run:
```
python3 -m cast
```
> See more about cast-sh [here](https://github.com/hericlesme/cast-sh)
