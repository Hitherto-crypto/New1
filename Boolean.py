#Boolean Operators
def or_(a, b):
 if a:
 return a
 else:
 return b

#For and, it will return its first value if it's false, else it returns the last value:
def and_(a, b):
 if not a:
 return a
 else:
 return b

#Example
if 3.14 < x < 3.142:
 print("x is near pi")

 #And
 x = True
 y = True
 z = x and y  # z = True x = True y = False z = x and y # z = False x = False y = True z = x and y # z = False x = False y = False z = x and y # z = False x = 1 y = 1 z = x and y # z = y, so z = 1, see `and` and `or` are not guaranteed to be a boolean x = 0 y = 1 z = x and y # z = x, so z = 0 (see above) x = 1 y = 0
 z = x and y  # z = y, so z = 0 (see above)
 x = 0
 y = 0
 z = x and y  # z = x, so z = 0 (see above)

 

