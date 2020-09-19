"""
Test the mass Conversion function
"""
import MassConversion as ms

help(ms)
kg = float(input("Enter mass in KG - "))
tone = ms.kgtotone(kg)
print(kg, " KG is equal to ", tone, " TONE")