xh = input("Enter Days:")
xr = input("Enter Rate:")
try:
    fh = float(xh)
    fr = float(xr)
    print(fh*fr)
except:
    print("Error, please enter numeric input")
