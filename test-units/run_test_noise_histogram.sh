#!/bin/bash

BASEDIR=$(dirname $0)

echo "Calling gnuplot..."
gnuplot -e "fname='< python3 $BASEDIR/../test-units/noise_histogram.py';oname='out/test_noise_histo.png'" $BASEDIR/../plot-libs/plot_histogram.gp

echo "  done."
