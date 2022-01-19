num = print(input("enter a number"))
try:
  val = int(num)
  print("conversion successful")
except:
   val = -1



if val > 0:
    print("number is",val)
else:
    print("not a number")
