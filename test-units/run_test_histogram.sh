#!/bin/bash

BASEDIR=$(dirname $0)

echo "Calling gnuplot..."
gnuplot -e "fname='< python3 $BASEDIR/../python-libs/histogram.py'" $BASEDIR/../plot-libs/plot_histogram.gp

echo "  done."
