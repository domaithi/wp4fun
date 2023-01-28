# Contraint-based Probabilistic Model Checking 4 Fun
This a bash based command-line tool for contraint-based probabilistic model checking, as part of a masters thesis.
The tool uses two different sat-solver: Z3 and CVC5.

This tool supports macOS.

# MacOS
## Prerequisites
- Python3 installed (preferely version 3.10)

### Z3
The Z3 is already added to the repository, but the binding does not support macs with the M1 or M2 chip.

Mac with the M1 or M2 chip:
- Delete the z3 folder in the repository
- Install z3 following: https://github.com/Z3Prover/z3?fbclid=IwAR2wsOm3KF_lsLpeTj2F1FibnF2GJir0A2A6Bm_LChStWTcKRcpja7oV0T0
### CVC5
Install the python binding by running the following:
```bash
pip3 install cvc5
```

## How to use the tool
Run the executable script _run_ with a .pgcl file as argument and choose one or both SMT-solver.

```bash
./run <program> -z3 -cvc5
```

Example:
```bash
./run Input/Mixed/test.pgcl -z3 -cvc5
```
The file _test.pgcl_ is solved using both the Z3 and cvc5 solver.

### Switched off the non-negativity and probability check
Use the flags --p and --n to turn off the probability check and non-negativity check, respetively.

Example:
```bash
./run Input/Mixed/test.pgcl -z3 --p
```
The file _test.pgcl_ is not checked for invalid probability. It is solved using the Z3 solver.

### Use variables of reals
Use the flag --r to use variables of reals intead of intergers.

Example:
```bash
./run Input/Mixed/test.pgcl -z3 --r
```
The variables in file _test.pgcl_ are of reals. It is solved using the Z3 solver.

# Documentation
Pre-expectation: Lower or upper bound (e.g. _>= 0_)

Post-expectation: The expectation for which you want to find the expected value of

Init: Only used for generating prism, can be disregarded completely

## Grammar of a pGCL program
See the report

## pGCL files
The format of a .pgcl file:
```bash
pre: <insert constraint>,
post: <insert postexpectation>,
init: <insert initial values>, (optional)

<pgcl program>
```

Example:
```bash
pre: <= 5,
post: x,

y:=1;
if (y > 0) {
    x:=0
} else {
    x:=10
}
```


For other examples of pgcl programs go to the _Input/Mixed_ folder.