import sys
import math

import argparse

#--------------------------

sum_values  = 0
sum_squared = 0
nb_values   = 0

average     = 0.0
variance    = 0.0

output_string = ""

#--------------------------

def parse_commands():
    global output_precision
    global list_values

    parser = argparse.ArgumentParser(description='Calculating average and variance of inputs')
    parser.add_argument('-p','--output-precision',default='2',help='Sets the number of digits to be printed',required=False)
    parser.add_argument('values',metavar='N', type=float, nargs='*',help='Input values')

    try:
        options = parser.parse_args()
    except:
        sys.exit(0)

    try:
        output_precision = int(options.output_precision)
    except:
        print('Output format parameter not correct: ',options.output_precision)

    list_values = options.values

#--------------------------

def print_output():
    average     = float(sum_values)/float(nb_values)
    variance    = float(sum_squared)/float(nb_values) - average*average

    print(output_string % (average,variance,math.sqrt(variance)) )

#--------------------------

if __name__ == '__main__':
    global output_precision
    global list_values

    parse_commands()

    output_string = "<v> = %.{}E\ts^2(v) = %.{}E\ts(v) = %.{}E".format(output_precision,output_precision,output_precision)

    if len(list_values):
        for value in list_values:
            nb_values   += 1
            sum_values  += value
            sum_squared += value*value

        print('Using the following list of values:')
        print(list_values)
        print_output()

    else:
        while True:
            print('v =',end=' ')
            try:
                ans = input()
            except:
                print('Closing...')
                sys.exit(0)

            try:
                value = float(ans)
            except:
                print('Wrong input format:',ans)
                sys.exit(1)

            nb_values   += 1
            sum_values  += value
            sum_squared += value*value

            print_output()

