#ARRAYS
#accessing elements through indexes
my_array = array('i', [1,2,3,4,5])
print(my_array[1])
# 2
print(my_array[2])
# 3
print(my_array[0])
# 1

from array import *
my_array = array('i', [1,2,3,4,5])
for i in my_array:
 print(i)

#Using append
my_array = array('i', [1,2,3,4,5])
my_array.append(6)
# array('i', [1, 2, 3, 4, 5, 6])

#insert using array
my_array = array('i', [1,2,3,4,5])
my_array.insert(0,0)
#array('i', [0, 1, 2, 3, 4, 5])

#Extend python array
my_array = array('i', [1,2,3,4,5])
my_extnd_array = array('i', [7,8,9,10])
my_array.extend(my_extnd_array)
# array('i', [1, 2, 3, 4, 5, 7, 8, 9, 10])

#fromlist method
my_array = array('i', [1,2,3,4,5]) c=[11,12,13]
my_array.fromlist(c)
# array('i', [1, 2, 3, 4, 5, 11, 12, 13])

#Fetching element
my_array = array('i', [1,2,3,4,5])
print(my_array.index(5))
# 5
my_array = array('i', [1,2,3,3,5])
print(my_array.index(3))
# 3

#Reverse python array
my_array = array('i', [1,2,3,4,5])
my_array.reverse()
# array('i', [5, 4, 3, 2, 1])

#Array buffer
my_array = array('i', [1,2,3,4,5])
my_array.buffer_info() (33881712, 5)

#Number occurrence using count methods
my_array = array('i', [1,2,3,3,5])
my_array.count(3)
# 2

#Array using tostring
#tostring() converts the array to a string.

my_char_array = array('c', ['g','e','e','k'])
# array('c', 'geek')
print(my_char_array.tostring())
# geek

#Append a string to char array using fromstring() method
my_char_array = array('c', ['g','e','e','k'])
my_char_array.fromstring("stuff")
print(my_char_array)
#array('c', 'geekstuff')

