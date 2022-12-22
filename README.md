# qre - quantum resource estimator

Usage:

``` bash
cd src
cat file.qasm | staq_lattice_surgery | ./qre.py -c config_compact.json
```

Or, for a given JSON file already produced by `staq_lattice_surgery`:

``` bash
cd src
cat file.json | ./qre.py -c config_fast.json
```

To read the JSON directly (without stdin redirection):
``` bash
cd src
./qre.py -c config_fast.json -f file.json
```

For help
``` bash
cd src
./qre.py -h
```
