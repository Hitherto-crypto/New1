#Conditionals

n = 5
"Greater than 2" if n > 2 else "Smaller than or equal to 2"
# Out: 'Greater than 2
n = 5
"Hello" if n > 10 else "Goodbye" if n > 5 else "Good day"

#if, elif and else
number = 5
if number > 2:
 print("Number is bigger than 2.")
elif number < 2: # Optional clause (you can have multiple elifs)
 print("Number is smaller than 2.")
else: # Optional clause (you can only have one else)
 print("Number is 2.")

#Cmp Functions
['equal', 'greater than', 'less than', ][cmp(x,y)]
# x,y = 1,1 output: 'equal'
# x,y = 1,2 output: 'less than'
# x,y = 2,1 output: 'greater than'

#Else statement
if condition:
 body
else:
 body

if True:
 print "It is true!"
else:
 print "This won't get printed.."
# Output: It is true!
if False:
 print "This won't get printed.."
else:
 print "It is false!"
# Output: It is false!

#if statement
if True:
 print "It is true!"

if 2 + 2 == 4:
 print "I know math!"



