"""
Conversion functions between fahrenheit and centigrade.

@Author - Rajesh Kumar Jha
PGT Computer Science
Name-tempConversion
Date - 16/07/2020
"""


# Functions
def to_centigrade(x):
    """
    :param x: fahrenheit as input
    :return: centigrade as output
    """
    return 5 * (x - 32) / 9.0


def to_fahrenheit(x):
    """
    :param x: centigrade as input
    :return: fahrenheit as output
    """
    return 9 * x / 5.0 + 32


# constants
FREEZING_C = 0.0  # water freezing temp.(in celcius)
FREEZING_F = 32.0  # water freezing temp.(in fahrenheit)
