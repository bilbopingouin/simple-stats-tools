
####################################
# Packages
####################################

# standard libs
import random
import os
import importlib.util
import math

# local directory to path
path = os.path.dirname(__file__)
if not path:
    path = '.'

# local libs
spec = importlib.util.spec_from_file_location(
        'noise',
        path+'/../python-libs/noise.py'
    )
noise = importlib.util.module_from_spec(spec)
spec.loader.exec_module(noise)

####################################
# Tests
####################################


def test_noise_gauss():
    n = noise.noise_gauss()

    assert n.active is True

    assert 5 == n.get_value(5, 0)

    random_value = n.get_value(5, 2)

    assert math.isnan(random_value) is False
    assert isinstance(random_value, float) is True
    assert 5 != random_value

    n.active = False
    assert math.isnan(n.get_value(5, 0)) is True


def test_noise_uniform():
    n = noise.noise_uniform()

    assert n.active is True

    assert 5 == n.get_value(5, 0)

    random_value = n.get_value(5, 2)

    assert math.isnan(random_value) is False
    assert isinstance(random_value, float) is True
    assert 5 != random_value

    n.active = False
    assert math.isnan(n.get_value(5, 0)) is True


def test_noise_noise_undefined_type():
    n = noise.noise('foo', 5, 'relative')

    assert n.skip is True

    assert math.isnan(n.noisy(42)) is True


def test_noise_noise_undefined_parameter():
    n = noise.noise('uniform', 5, 'foo')

    assert math.isnan(n.noisy(42)) is True


def test_noise_noise():
    for type_noise in 'uniform gauss'.split(' '):
        for parameter_type in 'relative absolute sqrt'.split(' '):
            if parameter_type == 'relative':
                N = noise.noise(type_noise, 0, parameter_type)
            elif parameter_type == 'absolute':
                N = noise.noise(type_noise, 0, parameter_type)
            elif parameter_type == 'sqrt':
                N = noise.noise(type_noise, 0, parameter_type)

            assert 42 == N.noisy(42)


def test_noise():
    base_value = random.uniform(1, 10)
    parameter_abs = random.uniform(0.5, 2)
    parameter_rel = random.uniform(0.0, 0.2)
    print('#', base_value, parameter_abs, parameter_rel)

    index = 0

    for type_noise in 'uniform gauss'.split(' '):
        for parameter_type in 'relative absolute sqrt'.split(' '):
            if parameter_type == 'relative':
                N = noise.noise(type_noise, parameter_rel, parameter_type)
            elif parameter_type == 'absolute':
                N = noise.noise(type_noise, parameter_abs, parameter_type)
            elif parameter_type == 'sqrt':
                N = noise.noise(type_noise, parameter_rel, parameter_type)
            else:
                print('ERR: parameter type unkown: ', parameter_type)

            for n in range(100):
                print(100*index+n, N.noisy(base_value))

            index += 1
