#Comparison
# by 'is' vs '=='

a = 'Python is fun!'
b = 'Python is fun!'
a == b # returns True
a is b # returns False
a = [1, 2, 3, 4, 5]
b = a # b references a
a == b # True
a is b # True
b = a[:] # b now references a copy of a
a == b # True
a is b # False [!!]

a = 'short'
b = 'short'
c = 5
d = 5
a is b # True
c is d # True

if myvar is not None:
 # not None
 pass
if myvar is None:
 # None
 pass

sentinel = object()
def myfunc(var=sentinel):
    if var is sentinel:
        # value wasn’t provided
        pass
        else:
        # value was provided
        pass

#Equal To
12 == 12
# True
12 == 1
# False
'12' == '12'
# True
'spam' == 'spam'
# True
'spam' == 'spam '
# False
'12' == 12
# False

#Comparing objects
class Foo(object):
    def __init__(self, item):
        self.my_item = item

    def __eq__(self, other):
        return self.my_item == other.my_item


a = Foo(5)
b = Foo(5)
a == b  # True
a != b  # False
a is b  # False


class Bar(object):
    def __init__(self, item):
        self.other_item = item

    def __eq__(self, other):
        return self.other_item == other.other_item

    def __ne__(self, other):
        return self.other_item != other.other_item


c = Bar(5)
a == c  # throws AttributeError: 'Foo' object has no attribute 'other_item'

