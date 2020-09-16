'''
Created on Jul 8, 2020
Progtam to calculate simple interest using a function interest 
that can receive pricipal amount, time, rate and return calculated
simple interest. Do specify default values for rate and time as
if 10% and 2 years respecively.
@author: admin
'''

def simpleInterest(prin, time = 2, rate =10):
    si = (prin*time*rate)/100
    return si

prin = float(input("Enter prncipal amount - "))
si = simpleInterest(prin)
print('Simple interest is  - ',si)
si = simpleInterest(prin, 5, 15)
print('Simple interest is  - ',si)