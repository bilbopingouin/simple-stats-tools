import sys
import math

import argparse

# --------------------------


def parse_commands():
    # Parser
    parser = argparse.ArgumentParser(
        description='Calculating average and variance of inputs')
    parser.add_argument(
        '-p',
        '--output-precision',
        default='2',
        help='Sets the number of digits to be printed',
        required=False
    )
    parser.add_argument(
        'values',
        metavar='N',
        type=float,
        nargs='*',
        help='Input values')

    # Parse input
    options = parser.parse_args()

    # Parameters
    parameters = {}
    try:
        parameters['output_precision'] = int(options.output_precision)
    except ValueError:
        print(
            'Output format parameter not correct: ',
            options.output_precision
        )
        sys.exit(1)

    parameters['list_values'] = options.values

    return parameters


# --------------------------

def print_output(output_string, calculated_values):
    if 0 == calculated_values['nb_values']:
        average = 0
        variance = 0
    else:
        average = float(calculated_values['sum_values'])\
            / float(calculated_values['nb_values'])
        variance = float(calculated_values['sum_squared'])\
            / float(calculated_values['nb_values'])\
            - average*average

    print(output_string % (
        average,
        variance,
        math.sqrt(variance),
        calculated_values['nb_values'],
        calculated_values['sum_values']))


# --------------------------

def get_output_string(precision):
    return '<v> = %.{}E\ts^2(v) = %.{}E\ts(v) = %.{}E\tN = %d\t'\
           'Sum = %.{}E'.format(
               precision, precision,
               precision, precision)


# --------------------------

def interactive(parameters):

    calculated_values = {
        'list_values': [],
        'nb_values': 0,
        'sum_values': 0,
        'sum_squared': 0
    }

    if parameters['list_values']:     # exists and is not empty
        for value in parameters['list_values']:
            calculated_values['list_values'] += [value]
            calculated_values['nb_values'] += 1
            calculated_values['sum_values'] += value
            calculated_values['sum_squared'] += value*value

    else:
        while True:
            try:
                ans = input('v = ')
            except KeyboardInterrupt:
                print('\nFinished.')
                break

            try:
                value = float(ans)
            except ValueError:
                print('Wrong input format:', ans)
                break

            calculated_values['list_values'] += [value]

            calculated_values['nb_values'] += 1
            calculated_values['sum_values'] += value
            calculated_values['sum_squared'] += value*value

            print_output(parameters['output_string'], calculated_values)

    # Return all the values calculated
    return calculated_values


# --------------------------

def main():
    # Get input parameters
    parameters = parse_commands()

    # Define the output string
    parameters['output_string']\
        = get_output_string(parameters['output_precision'])

    # Calculate the values
    calculated_values = interactive(parameters)

    # Print the final ouput
    print('Using the following list of values:')
    print(calculated_values['list_values'])
    print_output(parameters['output_string'], calculated_values)


if __name__ == '__main__':
    main()
