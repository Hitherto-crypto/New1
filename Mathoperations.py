#Simple mathematical operations
#Divisions
a, b, c, d, e = 3, 2, 2.0, -3, 10

print(a / b) # = 1
print(a / c) # = 1.5
print(d / b) # = -2
print(b / a) # = 0
print(d / e) # = -1

#Addition

a, b = 1, 2
# Using the "+" operator:
a + b # = 3

# Using the "in-place" "+=" operator to add and assign:
a += b # a = 3 (equivalent to a = a + b)
import operator # contains 2 argument arithmetic functions for the examples
operator.add(a, b) # = 5 since a is set to 3 right before this line
# The "+=" operator is equivalent to:
a = operator.iadd(a, b) # a = 5 since a is set to 3 right before this line

"first string " + "second string" # = 'first string second string'
[1, 2, 3] + [4, 5, 6] # = [1, 2, 3, 4, 5, 6]

#Exponentiation

a, b = 2, 3 (a ** b) # = 8
pow(a, b) # = 8
import math
math.pow(a, b) # = 8.0 (always float; does not allow complex results)
import operator
operator.pow(a, b) # = 8

a, b, c = 2, 3, 2
pow(2, 3, 2) # 0, calculates (2 ** 3) % 2, but as per Python docs,
 # does so more efficiently

import math
import cmath
c = 4
math.sqrt(c) # = 2.0 (always float; does not allow complex results)
cmath.sqrt(c) # = (2+0j) (always complex)

import math
 x = 8
math.pow(x, 1/3) # evaluates to 2.0
 x**(1/3) # evaluates to 2.0


math.exp(0) # 1.0
math.exp(1) # 2.718281828459045 (e)

math.expm1(0) # 0.0
math.exp(1e-6) - 1 # 1.0000004999621837e-06
math.expm1(1e-6) # 1.0000005000001665e-06
# exact result # 1.000000500000166666708333341666...

#Trigonometric Functions
a, b = 1, 2
import math
math.sin(a) # returns the sine of 'a' in radians
# Out: 0.8414709848078965
math.cosh(b) # returns the inverse hyperbolic cosine of 'b' in radians
# Out: 3.7621956910836314
math.atan(math.pi) # returns the arc tangent of 'pi' in radians
# Out: 1.2626272556789115
math.hypot(a, b) # returns the Euclidean norm, same as math.sqrt(a*a + b*b)
# Out: 2.23606797749979

#Inplace Operations
a = a + 1
a = a + 2

a += 1
# and
a *= 2

#Subtraction

a, b = 1, 2
# Using the "-" operator:
b - a # = 1

import operator # contains 2 argument arithmetic functions
operator.sub(b, a) # = 1

#Multiplication
a, b = 2, 3
a * b # = 6

import operator
operator.mul(a, b) # = 6

3 * 'ab' # = 'ababab'
3 * ('a', 'b') # = ('a', 'b', 'a', 'b', 'a', 'b')

#Logarithms
import math
import cmath
math.log(5) # = 1.6094379124341003
# optional base argument. Default is math.e
math.log(5, math.e) # = 1.6094379124341003
cmath.log(5) # = (1.6094379124341003+0j)
math.log(1000, 10) # 3.0 (always returns float)
cmath.log(1000, 10) # (3+0j)

# Logarithm base e - 1 (higher precision for low values)
math.log1p(5) # = 1.791759469228055
# Logarithm base 2
math.log2(8) # = 3.0
# Logarithm base 10
math.log10(100) # = 2.0
cmath.log10(100) # = (2+0j)

#Modulus
3 % 4 # 3
10 % 2 # 0
6 % 4 # 2

import operator
operator.mod(3 , 4) # 3
operator.mod(10 , 2) # 0
operator.mod(6 , 4) # 2