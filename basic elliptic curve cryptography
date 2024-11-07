'''This is a project that creates an elliptic curve and uses a value from it for an ElGamal elliptic curve encryption scheme.
The x value and number encrypted are chosen by the user, while the other values are preset. I may change that in the future.
I have not been able to decrypt the modulo. When I have, I will add it to this project.
Work in progress. '''

import math

x = int(input('Put a number: '))
xcb =  math.pow(x , 3) #x cubed
a = 5
b = 4
p = 11 #prime modulo

ysqr = int(xcb + (a * x) + b)
y = math.sqrt(ysqr) #square root of ec to get y
yInt = math.isqrt(ysqr) #y as a whole number
print('y^2 = x^3 + ax + b')
print('%d = %d + (%d * %d) + %d' % (ysqr, xcb, a, x, b))
print('The coordinates are %d and %d' % (x, y)) #prints out coordinates

priv = 3 #private key
public = (x * priv) #public key
print('The public key is %d'% public) #published value

k = 2 #int used to transmit message back to original user
m = int(input('Choose a number for a message: '))

xEc = x * k #first encrypted value
yEc = m + k * public #second encrypted value

encryptMessage = (xEc % p, yEc % p) #adds mod to values
print(encryptMessage) #prints out encrypted message

decryptFirst = xEc * priv #multiples encrypted x with private key
decryptNext = yEc - decryptFirst #subtracts decryptFirst from encrypted y
print('The message is %d' % decryptNext) #prints out message
