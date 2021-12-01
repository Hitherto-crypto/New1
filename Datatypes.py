#string data type

a_str = 'Hello World'
print(a_str)            #output will be the whole string
print(a_str[0])         #output will be first character
print(a_str[0:5])       #output will be first few characters

#set data types
#set - mutable and new elements can be added once sets are defined

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   #duplicates will be removed

a = set('abracadabra')
print(a)

a.add('z')
print(a)

b = frozenset('asdfagsa')
print(b)
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
print(cities)

#Number data types
int_num = 10 #int value
float_num = 10.2 #float value
complex_num = 3.14j #complex value
long_num = 1234567 #long value

#List Data Types

list = [123,'abcd',10.2,'d'] #can be an array of any data type or single data type.
list1 = ['hello','world']
print(list) #will output whole list. [123,'abcd',10.2,'d']
print(list[0:2]) #will output first two element of list. [123,'abcd']
print(list1 * 2) #will gave list1 two times. ['hello','world','hello','world']
print(list + list1) #will gave concatenation of both the lists.
[123,'abcd',10.2,'d','hello','world']

#Dictionary data type
dic={'name':'red','age':10}
print(dic) #will output all the key-value pairs. {'name':'red','age':10}
print(dic['name']) #will output only value with 'name' key. 'red'
print(dic.values()) #will output list of values in dic. ['red',10]
print(dic.keys()) #will output list of keys. ['name','age']

# Tuple data type
tuple = (123,'hello')
tuple1 = ('world')
print(tuple) #will output whole tuple. (123,'hello')
print(tuple[0]) #will output first value. (123)
print(tuple + tuple1) #will output (123,'hello','world')
tuple[1]='update' #this will give you error.