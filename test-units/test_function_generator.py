####################################
# Packages
####################################

# standard libs
import math
import os
import importlib.util

# local directory to path
path = os.path.dirname(__file__)
if not path:
    path = '.'

# local libs
spec = importlib.util.spec_from_file_location(
    'function_generator',
    path+'/../python-libs/function_generator.py'
)
function_generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(function_generator)

####################################
# Tests
####################################


def test_function_generator_polynomial():
    # Order 1: 5+0.1*x
    order = 1
    a0 = 5
    a1 = 0.1

    F = function_generator.function_generator(
        'polynomial', str(order)+':'+str(a1)+':'+str(a0))

    expected_result = a0+a1*3
    function_result = F.get_function_value(3, float('nan'))

    assert expected_result == function_result

    # Order 2: 1-2x+x^2
    order = 2
    a0 = 1
    a1 = -2
    a2 = 1

    F = function_generator.function_generator(
        'polynomial', str(order)+':'+str(a2)+':'+str(a1)+':'+str(a0))

    expected_result = 0
    function_result = F.get_function_value(1, float('nan'))

    assert expected_result == function_result

    function_result = F.get_function_value(2, float('nan'))

    assert expected_result != function_result


def test_function_generator_sine():
    amplitude = 5
    frequence = 0.1
    offset = 0.5

    F = function_generator.function_generator(
        'sine', str(amplitude)+':'+str(frequence)+':'+str(offset))

    expected_result = (amplitude*math.sin(2*math.pi*frequence*(4-offset)))
    function_result = F.get_function_value(4, float('nan'))

    assert expected_result == function_result


def test_function_generator_exponential():
    amplitude = 10
    factor = 0.2

    F = function_generator.function_generator(
        'exponential', str(amplitude)+':'+str(factor))

    expected_result = amplitude*math.exp(-factor*5)
    function_result = F.get_function_value(5, float('nan'))

    assert expected_result == function_result


def test_function_generator_gauss():
    amplitude = 10
    sigma = 10
    offset = 50

    F = function_generator.function_generator(
        'gauss', str(amplitude)+':'+str(sigma)+':'+str(offset))

    expected_result = amplitude*math.exp(-(5-offset)*(5-offset)/(sigma*sigma))
    function_result = F.get_function_value(5, float('nan'))

    assert expected_result == function_result


def test_function_generator_poisson():
    amplitude = 10
    lambda_parameter = 4

    F = function_generator.function_generator(
        'poisson', str(amplitude)+':'+str(lambda_parameter))

    expected_result = amplitude * \
        math.exp(-lambda_parameter)*(lambda_parameter**(5))/(math.factorial(5))
    function_result = F.get_function_value(5, float('nan'))

    assert expected_result == function_result


def test_function_generator_log():
    amplitude = 10
    offset = 4

    F = function_generator.function_generator(
        'log', str(amplitude)+':'+str(offset))

    expected_result = amplitude*math.log(offset+5)
    function_result = F.get_function_value(5, float('nan'))

    assert expected_result == function_result


def test_function_generator_sqrt():
    amplitude = 10
    offset = 4

    F = function_generator.function_generator(
        'sqrt', str(amplitude)+':'+str(offset))

    expected_result = amplitude*math.sqrt(offset+5)
    function_result = F.get_function_value(5, float('nan'))

    assert expected_result == function_result


def test_function_generator_inverse():
    amplitude = 10
    offset = 4

    F = function_generator.function_generator(
        'inverse', str(amplitude)+':'+str(offset))

    expected_result = amplitude/(offset+5)
    function_result = F.get_function_value(5, float('nan'))

    assert expected_result == function_result


def test_function_generator_identity():
    F = function_generator.function_generator('identity', 'nan')

    expected_result = 5
    function_result = F.get_function_value(5, float('nan'))

    assert expected_result == function_result


def test_function_generator_window():
    window_size = 6

    F = function_generator.function_generator('window', str(window_size))

    expected_result = 0
    for n in range(window_size):
        expected_result += n*n
        function_result = F.get_function_value(float('nan'), n*n)

    expected_result /= window_size

    assert expected_result == function_result


def test_function_generator_cumulative():
    F = function_generator.function_generator('cumulative', 'nan')

    expected_result = 0
    for n in range(5):
        function_result = F.get_function_value(float('nan'), n*n)
        expected_result = (n*expected_result+n*n)/(n+1)

    assert expected_result == function_result


def test_function_generator_factored():
    factor = 6

    F = function_generator.function_generator('factored', str(factor))

    expected_result = 0
    for n in range(5):
        function_result = F.get_function_value(float('nan'), n*n)
        expected_result = (factor*expected_result+n*n)/(factor+1)

    assert expected_result == function_result


def test_function_generator_quadratic():
    factor = 6

    F = function_generator.function_generator('quadratic', str(factor))

    expected_result = 0
    for n in range(5):
        function_result = F.get_function_value(float('nan'), n)
        expected_result = (factor*expected_result+n*n)/(factor+n)

    assert expected_result == function_result


def test_function_generator_wrong_function():
    F = function_generator.function_generator('foo', '0')

    assert F.skip is True
    assert math.isnan(F.get_function_value(0,0)) is True


def test_function_generator_parameter_size():
    F = function_generator.function_generator('gauss', '0')

    assert F.skip is True
    assert math.isnan(F.get_function_value(0,0)) is True


def test_function_generator_parameter_type():
    F = function_generator.function_generator('log', '0:a')

    assert math.isnan(F.get_function_value(0,0)) is True

    F = function_generator.function_generator('polynomial', '0:a')

    assert math.isnan(F.get_function_value(0,0)) is True

def test_function_generator_function_generic():
    F = function_generator.function_generic()
    F.init('0:1')

    assert 0 == F.function(float('nan'), float('nan'))
    assert 0 == F.get_value(float('nan'), float('nan'))

    F.active = False
    assert math.isnan(F.get_value(float('nan'), float('nan'))) is True


def test_function_generator_function_polynomial_errors():
    F = function_generator.function_polynomial()

    assert 2 == F.init('')
    assert 3 == F.init('a:5')
    assert 4 == F.init('0:1:2')
    assert 5 == F.init('0:a')
    assert math.isnan(F.get_value(0,0)) is True



def test_functions_generations():

    # Using:
    # https://stackoverflow.com/questions/32111941/
    #   r-how-to-generate-a-noisy-sine-function#32112610
    yvalues = [
        0.82982774,  2.24736614,  2.65015416,
        3.46682674,  3.52729297,  3.49584034,
        3.21650125,  4.36715717,  3.33775743,
        4.25865056,  3.08154581,  1.29021692,
        1.29727107,  0.18405785,  0.54038839,
        -1.56588876, -1.12647564, -2.22541481,
        -1.73397892, -1.47479364, -2.78684092,
        -0.71941248, -1.18848838, -1.14310578,
        0.99296343,  1.96275316,  2.21877083,
        1.82625195,  3.56494503,  4.58475139,
        3.43430470,  4.96176449,  4.05305860,
        3.47720003,  3.12880561,  1.63220985,
        2.47756490,  0.32653887,  0.04058271,
        -0.27735692, -1.00248342, -2.03402250,
        -1.99755668, -1.76619781, -2.03965488,
        -2.48876795, -1.17858836, -0.83329113,
        0.41488879,  0.50468218,  1.12150799,
        1.68485862,  2.28072161,  3.96888097,
        2.91623328,  3.34443738,  3.09313796,
        3.28688135,  3.72462122,  2.96415418,
        1.85136958,  2.62886448,  1.13530004,
        0.27470068, -0.12288578, -1.15473463,
        -2.15411720, -1.00004169, -2.54632330,
        -1.92948988, -1.29557262, -1.53368721,
        -1.04163048, -0.20596297,  1.77020757,
        2.41725266,  1.92812607,  2.81425263,
        3.74461982,  3.47113171,  3.01444636,
        4.55037931,  2.80800815,  4.33598397,
        3.66507070,  2.72017885,  2.17351610,
        0.75793812,  0.25465984, -1.62278327,
        -1.04956540, -0.86896317, -1.34327100,
        -2.07355078, -1.00718962, -1.08180038,
        -1.25338040, -1.03877604,  1.12414670,
        0.24223937
    ]

    functions = [
        ['polynomial',  '1:0.1:5'],
        ['polynomial',  '2:0.002:-0.3:1'],
        ['sine',        '5:0.1:0.5'],
        ['exponential', '10:0.2'],
        ['gauss',       '10:10:50'],
        ['poisson',     '10:4'],
        ['log',         '5:2'],
        ['sqrt',        '0.5:5'],
        ['inverse',     '10:5'],
        ['identity',    '0'],
        ['window',      '5'],
        ['cumulative',  '0'],
        ['factored',    '5'],
        ['quadratic',   '0.1']
    ]

    for n, func in enumerate(functions):
        print('#Processing:', func[0], func[1])
        F = function_generator.function_generator(func[0], func[1])

        for m in range(100):
            y = F.get_function_value(m, yvalues[m])
            if not math.isnan(y):
                print(m+n*100, y)
