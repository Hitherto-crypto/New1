# LOOPS
# FOR LOOPS - Used for iterating over a sequence

for letters in ("hello"):
    print (letters)

for j in range(50,100):
    print(j)

for n in range(0,10,2):
    print(n)

for m in range(100):
    if m%2==0:
        print(m,'is divisible by 2')
    else:
        print(m,'is not divisible by 2')

for i in range(10):
    for j in range(i+1):
        print ("*",end=" ")
    print()

for i in range(99,0,-1):
    print(i)

for k in  range(100):
    print(k)
