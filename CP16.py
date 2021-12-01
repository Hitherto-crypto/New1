#LOOPS
#Break and Contionue in Loops

i = 0
while i < 7:
 print(i)
 if i == 4:
    print("Breaking from loop")
    break
 i += 1

#Continue statement
for i in (0, 1, 2, 3, 4, 5):
 if i == 2 or i == 4:
 continue
 print(i)

#Nested Loops
while True:
 for i in range(1,5):
 if i == 2:
 break # Will only break out of the inner loop!

def break_loop():
 for i in range(1, 5):
 if (i == 2):
 return(i)
 print(i)
 return(5)


def break_all():
 for j in range(1, 5):
 for i in range(1,4):
 if i*j == 6:
 return(i)
 print(i*j)

#For Loops
for i in [0, 1, 2, 3, 4]:
 print(i)

#iterating over list
for x in ['one', 'two', 'three', 'four']:
 print(x)

for x in range(1, 6):
 print(x)

for index, item in enumerate(['one', 'two', 'three', 'four']):
 print(index, '::', item)

x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(x)

#Loops with 'else' clause
for i in range(3):
 print(i)
else:
 print('done')
i = 0
while i < 3:
 print(i)
 i += 1
else:
 print('done')


for i in range(2):
 print(i)
 if i == 1:
 break
else:
 print('done')

while loop_condition():
 ...
 if break_condition():
 break
 ...


while loop_condition():
 ...
 if break_condition():
 break
 ...
else:
 print('done')


 ...
 if break_condition():
 goto <<end>>
 ...
 goto <<start>>
else:
 print('done')


#Pass Statement
for x in range(10):
    pass

while x == y:
 pass

#Iterating over dictionaries
 d = {"a": 1, "b": 2, "c": 3}

for key in d:
 print(key)

for key, value in d.items():
 print(key, "::", value)

#Half loop "do while"
a = 10
while True:
 a = a-1
 print(a)
 if a<7:
 break
print('Done.')

#Looping and unpacking
collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]

for item in collection:
 i1 = item[0]
 i2 = item[1]
 i3 = item[2]
 # logic

for i1, i2, i3 in collection:
 # logic

#While Loop
#loop will cause loop statement to be executed until loop is falsey
 i = 0
 while i < 4:
     # loop statements
     i = i + 1

myObject = anObject()
while myObject.isNotReady():
 myObject.tryToGetReady()

import cmath
complex_num = cmath.sqrt(-1)
while complex_num: # You can also replace complex_num with any number, True or a value of any
type
 print(complex_num) # Prints 1j forever

while True:
 print "Infinite loop"