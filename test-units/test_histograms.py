
####################################
# Packages
####################################

# standard libs
import random
import os
import importlib.util

# local directory to path
path = os.path.dirname(__file__)
if not path:
    path = '.'

# local libs
spec = importlib.util.spec_from_file_location(
    'histogram',
    path+'/../python-libs/histogram.py'
)
histogram = importlib.util.module_from_spec(spec)
spec.loader.exec_module(histogram)

####################################
# Tests
####################################


def test_histogram_basic(capsys):
    H = histogram.histogram(0.5, 10.5, 10)
    for n in range(11):
        H.add_value(n)

    H.print()
    H.print_array()

    out, err = capsys.readouterr()
    assert '1.0 1\n2.0 1\n3.0 1\n4.0 1\n5.0 1\n'\
           '6.0 1\n7.0 1\n8.0 1\n9.0 1\n10.0 1\n'\
           '[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]\n' == out


def test_histogram():
    # Basic histogram
    vmin = random.uniform(0, 5)
    vmax = random.uniform(5, 20)
    nbins = random.randint(7, 20)

    print('#', vmin, vmax, nbins)

    H = histogram.histogram(vmin, vmax, nbins)

    for n in range(200):
        H.add_value(random.uniform(vmin, vmax))

    H.print()
