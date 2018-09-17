# very basic libs
import os
import sys

# Add local directory to path
path=os.path.dirname(__file__)
if not path:
    path='.'
sys.path.append(path+'/../python-libs/')

# standards libs
import random

# local libs
from histogram import histogram

H = histogram(0,10,10)

for n in range(100):
    H.add_value(random.uniform(0,10))

H.print()
