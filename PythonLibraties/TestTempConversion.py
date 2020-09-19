import tempConversion as tc

temp = float(input("Enter temperature -"))
unit = input("Enter unit of temperature in [c/f] - ")
if unit == 'c':
    ftemp = tc.to_fahrenheit(temp)
    print(temp, "C is equal to ", ftemp, "F")
elif unit == 'f':
    ctemp = tc.to_centigrade(temp)
    print(temp, "F is equal to ", ctemp, "C")

print('Freezing temperature in C  is - ', tc.FREEZING_C)
print('Freezing temperature in f  is - ', tc.FREEZING_F)
