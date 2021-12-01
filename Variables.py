#Variable Scope and Binding
def counter():
 num = 0
 def incrementer():
  nonlocal num
 num += 1
 return num
 return incrementer

c = counter()
c()
c()
c()

#Global Variable
x = 'Hi'
def read_x():
 print(x) # x is just referenced, therefore assumed global
read_x() # prints Hi
def read_y():
 print(y) # here y is just referenced, therefore assumed global
read_y() # NameError: global name 'y' is not defined
def read_y():
 y = 'Hey' # y appears in an assignment, therefore it's local
 print(y) # will find the local y
read_y() # prints Hey
def read_x_local_fail():
 if False:
 x = 'Hey' # x appears in an assignment, therefore it's local
 print(x) # will look for the _local_ z, which is not assigned, and will not be found
read_x_local_fail() # UnboundLocalError: local variable 'x' referenced before assignment

x = 'Hi'
def change_local_x():
 x = 'Bye'
 print(x)
change_local_x() # prints Bye
print(x) # prints Hi

x = 'Hi'
def change_global_x():
 global x
 x = 'Bye'
 print(x)
change_global_x() # prints Bye
print(x) # prints Bye

#Local Variables
def foo():
 a = 5
 print(a) # ok
print(a) # NameError: name 'a' is not defined

def foo():
 if True:
 a = 5
 print(a) # ok
b = 3
def bar():
 if False:
 b = 5
 print(b) # UnboundLocalError: local variable 'b' referenced before assignment

#The del command
del v
x = 5
print(x) # out: 5
del x
print(x) # NameError: name 'f' is not defined

del v.name
class A:
 pass
a = A()
a.x = 7
print(a.x) # out: 7
del a.x
print(a.x) # error: AttributeError: 'A' object has no attribute 'x'
del v[item]

x = {'a': 1, 'b': 2}
del x['a']
print(x) # out: {'b': 2}
print(x['a']) # error: KeyError: 'a'
del v[a:b]

x = [0, 1, 2, 3, 4]
del x[1:3]
print(x) # out: [0, 3, 4]


#function skip class scope
a = 'global'


class Fred:
    a = 'class'  # class scope
    b = (a for i in range(10))  # function scope
    c = [a for i in range(10)]  # function scope
    d = a  # class scope
    e = lambda: a  # function scope
    f = lambda a=a: a  # default argument uses class scope

    @staticmethod  # or @classmethod, or regular instance method
    def g():  # function scope
        return a


print(Fred.a)  # class
print(next(Fred.b))  # global
print(Fred.c[0])  # class in Python 2, global in Python 3
print(Fred.d)  # class
print(Fred.e())  # global
print(Fred.f())  # class
print(Fred.g())  # global

#Local vs Global Scope

foo = 1 # global
def func():
 bar = 2 # local
 print(foo) # prints variable foo from global scope
 print(bar) # prints variable bar from local scope

foo = 1
def func():
 bar = 2
 print(globals().keys()) # prints all variable names in global scope
 print(locals().keys()) # prints all variable names in local scope

foo = 1
def func():
 foo = 2 # creates a new variable foo in local scope, global foo is not affected
 print(foo) # prints 2
 # global variable foo still exists, unchanged:
 print(globals()['foo']) # prints 1
 print(locals()['foo']) # prints 2
#To modify a global variable, use keyword global:
foo = 1
def func():
 global foo
 foo = 2 # this modifies the global foo, rather than creating a local variable

#Fuctions within Functions
foo = 1
def f1():
 bar = 1
 def f2():
 baz = 2
 # here, foo is a global variable, baz is a local variable
 # bar is not in either scope
 print(locals().keys()) # ['baz']
 print('bar' in locals()) # False
 print('bar' in globals()) # False
 def f3():
 baz = 3
 print(bar) # bar from f1 is referenced so it enters local scope of f3 (closure)
 print(locals().keys()) # ['bar', 'baz']
 print('bar' in locals()) # True
 print('bar' in globals()) # False
 def f4():
 bar = 4 # a new local bar which hides bar from local scope of f1
 baz = 4
 print(bar)
 print(locals().keys()) # ['bar', 'baz']
 print('bar' in locals()) # True
 print('bar' in globals())  # False

#Binding Occurrence
x = 5
x += 7
for x in iterable: pass
