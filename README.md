[![Build Status](https://travis-ci.org/aziflaj/numberoid.svg?branch=master)](https://travis-ci.org/aziflaj/numberoid)

#README
**Numberoid** is a collection of some Python functions that may be used to solve simple Numerical Analysis problems.

###Why called "Numberoid"?
I couldn't think of any other name. Before switching to Numberoid, the project's name was `NoName`.

##Capabilities

Matrix calculations:
  - Finding the determinant of a square matrix
  - Finding a minor of a square matrix
  - Transposing a matrix
  - Inverting a square matrix
  - Scalar multiplication
  - Matrix multiplication
  - Solving a system of linear equations by multiplying two matrices that characterize the system.
  
Numerical integration:
  - Riemann integral calculator


##ToDo
  - Add more numerical integration formulas, such as the Simpson rule
  - Add methods for solving equations
  - Add methods of interpolation


##Testing
All the tests go into the folder named `test`. To run the tests, execute:

```bash
python -m unittest discover -s test
```
