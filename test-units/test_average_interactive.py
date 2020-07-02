
####################################
# Packages
####################################

# standard libs
import pytest
import sys
import os
import importlib.util

# local directory to path
path = os.path.dirname(__file__)
if not path:
    path = '.'

# local libs
spec = importlib.util.spec_from_file_location(
    'average_interactive',
    path+'/../python-libs/average_interactive.py'
)
average_interactive = importlib.util.module_from_spec(spec)
spec.loader.exec_module(average_interactive)

####################################
# Tests
####################################


def test_average_interactive_arguments_defaults(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['average_interactive'])
    parameters = average_interactive.parse_commands()
    assert 2 == parameters['output_precision']
    assert [] == parameters['list_values']


def test_average_interactive_argument(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        'average_interactive',
        '-p', '4',
        '1', '2', '3'
    ])
    parameters = average_interactive.parse_commands()
    assert 4 == parameters['output_precision']
    assert [1, 2, 3] == parameters['list_values']


def test_average_interactive_argument_wrong_precision(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        'average_interactive',
        '-p', 'a'
    ])
    with pytest.raises(SystemExit):
        average_interactive.parse_commands()


def test_average_interactive_print_output(capsys):
    calculated_values = {
        'sum_values': 4,
        'nb_values': 2,
        'sum_squared': 16
    }
    output_string = '%d, %d, %d, %d, %d'
    average_interactive.print_output(output_string, calculated_values)
    out, err = capsys.readouterr()
    assert '2, 4, 2, 2, 4\n' == out


def test_average_interactive_print_output_0values(capsys):
    calculated_values = {
        'sum_values': 4,
        'nb_values': 0,
        'sum_squared': 16
    }
    output_string = '%d, %d, %d, %d, %d'
    average_interactive.print_output(output_string, calculated_values)
    out, err = capsys.readouterr()
    assert '0, 0, 0, 0, 4\n' == out


def test_get_output_string():
    precision = 1
    string = average_interactive.get_output_string(precision)
    assert '<v> = %.1E\ts^2(v) = %.1E\ts(v) = %.1E\tN = %d\tSum = %.1E'\
        == string

    precision = 7
    string = average_interactive.get_output_string(precision)
    assert '<v> = %.7E\ts^2(v) = %.7E\ts(v) = %.7E\tN = %d\tSum = %.7E'\
        == string


def test_average_interactive_interactive(capsys):
    parameters = {
        'output_precision': 2,
        'list_values': [0, 10]
    }
    calculated_values = average_interactive.interactive(parameters)
    assert 2.0 == calculated_values['nb_values']
    assert 10.0 == calculated_values['sum_values']
    assert 100.0 == calculated_values['sum_squared']
    assert [0.0, 10.0] == calculated_values['list_values']


def test_main(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        'average_interactive',
        '-p', '1',
        '0', '10'
    ])
    average_interactive.main()
    out, err = capsys.readouterr()
    assert 'Using the following list of values:\n[0.0, 10.0]\n'\
        '<v> = 5.0E+00\ts^2(v) = 2.5E+01\ts(v) = 5.0E+00\tN = 2\t'\
        'Sum = 1.0E+01\n' == out


def test_main_interactive(capsys):
    input_values = [0, 10, '\n']
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    average_interactive.input = mock_input
    # average_interactive.print = lambda s: output.append(s)

    parameters = {
        'list_values': [],
        'output_string': '%d, %d, %d, %d, %d'
    }

    average_interactive.interactive(parameters)
    out, err = capsys.readouterr()
    assert '0, 0, 0, 1, 0\n5, 25, 5, 2, 10\nWrong input format: \n\n' == out
