import math

x = int(input('Put a number: '))
xcb =  math.pow(x , 3) #x cubed
a = 5
b = 4

ysqr = int(xcb + (a * x) + b)
y = math.sqrt(ysqr) #square root of ec to get y
yInt = math.isqrt(ysqr) #y as a whole number
print('y^2 = x^3 + ax + b')
print('%d = %d + (%d * %d) + %d' % (ysqr, xcb, a, x, b))
print('The coordinates are %d and %d' % (x, y)) #prints out coordinates

priv = 3 #private key
public = (x * priv) #public key
print('The public key is %d'% public) #published value
print('The private key is %d' % priv) #published value, though not in practice

k = 5 #int used to transmit message back to original user
m = int(input('Choose a number for a message: '))

xEc = x * k #first encrypted value
yEc = m + k * public #second encrypted value

encryptMessage = (xEc, yEc) #establishes encrypted message
print(encryptMessage) #prints out encrypted message

decryptFirst = xEc * priv #multiples encrypted x with private key
decryptNext = yEc - decryptFirst #subtracts decryptFirst from encrypted y
print('The message is %d' % decryptNext) #prints out message
