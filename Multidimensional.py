#Multidimensional arrays
#List in list
lst=[[1,2,3],[4,5,6],[7,8,9]]

print (lst[0])
#output: [1, 2, 3]
print (lst[1])
#output: [4, 5, 6]
print (lst[2])
#output: [7, 8, 9]

print (lst[0][0])
#output: 1
print (lst[0][1])
#output: 2


#Lists in lists in lists in..
[[[111,112,113],[121,122,123],[131,132,133]],[[211,212,213],[221,222,223],[231,232,233]],[[311,312,
313],[321,322,323],[331,332,333]]]

[[[111,112,113],[121,122,123],[131,132,133]],\ [[211,212,213],[221,222,223],[231,232,233]],\ [[311,312,313],[321,322,323],[331,332,333]]]

accessing is similar 2D
print(myarray)
print(myarray[1])
print(myarray[2][1])
print(myarray[1][0][2])

#editing is similar
myarray[1]=new_n-1_d_list
myarray[2][1]=new_n-2_d_list
myarray[1][0][2]=new_n-3_d_list #or a single number if you're dealing with 3D arrays

