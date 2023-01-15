mess =[]
enmess =[]
inp = input("Enter A Message: ")
for x in inp:
    mess.append(x)

for x in mess:
    if(x == 'x'):
        enmess.append('a')
    elif(x == 'y'):
        enmess.append('b')
    elif (x == 'z'):
        enmess.append('c')
    elif (x == ' '):
        enmess.append(' ')
    else:
        e = chr(ord(x)+3)
        enmess.append(e)
em =""
for x in enmess:
    em += x
print(em)

