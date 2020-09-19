"""
Create a module lengthconversion.py that stores function for
verios length conversion. e.g
1. miletokm()
2. kmtomile()
3. feettoinches()
4. inchestofeet()
@Author : XII Science Students
@Date : 24/07/2000
"""


def miletokm(mile):
    """
    function to covert mile to km
    :param mile: distance in mile
    :return: distance in kilo meter
    """
    km = mile / ONE_MILE
    return km


def kmtomile(km):
    """
    function to covert km to mile
    :param km: distance in km
    :return: distance in mile
    """
    mile = km * ONE_MILE
    return mile


def feetoinches(feet):
    """
    Function to convert feet to inches
    :param feet: distance in feet
    :return: distance in inches
    """
    inches = feet * ONE_FEET
    return inches


def inchestofeet(inch):
    """
    Function to convert inch to feet
    :param inch: distance in inches
    :return: distance in feet
    """
    feet = inch / ONE_FEET
    return feet


# CONSTANTS
ONE_MILE = 1.609344
ONE_FEET = 12
