# Insight Data Engineering Coding Challenge

_Huijuan Zhang_

Aug 30th, 2018

This is a solution for Insight Data Engineering Coding Challenge. Instructions can be found [here](https://github.com/InsightDataScience/prediction-validation).

## Approach

The high-level idea of my solution is to read `actual.txt` and `predicted.txt` as two dictionaries in Python, considering `time` and `stock` ID as dictionary key and `price` as corresponding value. Then calculate error between values of the same key in two dictionaries. Finally calculate average error within a window size.

## Dependency

All the code was written in __Python 3.6__, which does not contain any 'exotic' packages.

## Run Instructions

The shell script `run.sh` compiles and runs the program. To execute the code, run `run.sh` within the top-level file `InsightCodingChallenge`.

    ./run.sh
    
