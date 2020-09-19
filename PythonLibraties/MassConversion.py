"""
Module for MassConversion
@Author : XII Science Students
@Date : 25/07/2020
"""

def kgtotone(kg) :
    """
    Function to convert kg to tone
    :param kg: parameter in kg
    :return: returns weight in tone
    """
    tone = ONE_KILO_TONE*kg
    return tone

#CONSTANTS
ONE_KILO_TONE = 0.001
ONE_KILO_POUND = 2.20462