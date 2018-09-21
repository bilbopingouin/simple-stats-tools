#!/bin/bash

BASEDIR=$(dirname $0)

echo "Calling gnuplot..."
gnuplot -e "fname='< python3 $BASEDIR/../test-units/function_noise.py';oname='out/test_function_noise.png'" $BASEDIR/../plot-libs/plot_trace.gp

echo "  done."
