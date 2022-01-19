days =  int(input("enter the number of days"))
rate  =  float(input("enter the rate"))
result = days * rate
if  rate > 0:
   print("total", result)
elif rate < 0:
   print("enter positive numeric value")
else:
    print("rate can't be zero")
