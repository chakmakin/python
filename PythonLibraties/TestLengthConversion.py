import lengthconversion as lc
distkm = float(input("Enter distance in KM - "))
distmile = lc.kmtomile(distkm)
print(distkm, " KM is equal to ", distmile, " MILE")
#print("%f KM is equal to %f"%(distkm, distmile))


distmile = float(input("Enter distance in MILE - "))
distkm = lc.miletokm(distmile)
print(distmile, " MILE is equal to ", distkm, " KM")