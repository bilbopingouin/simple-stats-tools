#!/bin/bash

BASEDIR=$(dirname $0)

echo "Calling gnuplot..."
gnuplot -e "fname='< python3 $BASEDIR/../python-libs/noise.py'" $BASEDIR/../plot-libs/plot_trace.gp

echo "  done."
