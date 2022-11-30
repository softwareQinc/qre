# qre - quantum resource estimator

Usage:

``` bash
cd src
cat file.qasm | staq_lattice_surgery | ./tlayers | ./qre.py -c config_compact.json
```

Or, for a given JSON file already produced by `staq_lattice_surgery`:

``` bash
cd src
cat file.json | ./tlayers | ./qre.py -c config_fast.json
```	
