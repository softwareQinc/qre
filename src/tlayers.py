#!/usr/bin/env python3

import argparse
import json
import sys

# Initialize parser
parser = argparse.ArgumentParser(
    description='Takes as input a JSON file file produced by staq_lattice_surgery and outputs the list of T-counts '
                'for each layer of commuting pi/8 rotations')

# Adding optional arguments
parser.add_argument("-f", "--file", help="Reads from file (by default reads from stdin)")
parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")

# Read arguments from command line
args = parser.parse_args()

verbose = False
if args.verbose:
    verbose = True

if __name__ == '__main__':
    data = {}
    if args.file:
        with open(args.file) as f:
            data = json.loads(f.read())
    else:
        data = json.load(sys.stdin)

    n_qubits = int(data['3. Circuit after T depth reduction']['n'])
    t_layers = data['3. Circuit after T depth reduction']['T layers']
    t_counts = []
    if t_layers is not None:
        for layer in t_layers:
            t_counts.append(len(layer))

    if verbose:
        print("n_qubits:", n_qubits)
        print("T-depth:", len(t_counts))
        print("T-count:", sum(t_counts))
        print("T-count/layer:", t_counts)
    else:
        print(n_qubits)
        print(t_counts)
