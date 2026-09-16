from array import * 

# for i, u refer README 1.1
val = array('i', [1,2,3,4,5,6,7]) 

val1 = array('u', ['s', 'a', 'y', 'a', 'l', 'i'])

for i in val:
    print(i, end=",")

print(val.typecode)

print('\n')

for x in val1:
    print(x, end="")
print(f" -", val1.typecode)


# Reversing the Array

val.reverse()

for i in val:
    print(i, end=",")