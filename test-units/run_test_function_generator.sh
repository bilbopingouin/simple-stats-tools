#!/bin/bash

BASEDIR=$(dirname $0)

echo "Calling gnuplot..."
gnuplot -e "fname='< python3 $BASEDIR/../python-libs/function-generator.py';oname='out/test_function.png'" $BASEDIR/../plot-libs/plot_trace.gp

echo "  done."
