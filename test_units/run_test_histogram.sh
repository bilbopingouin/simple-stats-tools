#!/bin/bash

gnuplot -e "fname='< python3 ../test_units/test_histogram.py'" ../plot/plot_histogram.gp
