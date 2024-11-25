This is a project based on the ElGamal elliptic curve encryption scheme.
The first part creates an elliptic curve y^2 = x^3 + ax + b.
The second part uses the x value from the curve and actually implements an ElGamal elliptic curve encryption scheme.
Based on Neal Koblitz's paper in a 1987 issue of Mathematics of Computation:
https://www.ams.org/journals/mcom/1987-48-177/S0025-5718-1987-0866109-5/S0025-5718-1987-0866109-5.pdf
The x value and number encrypted are chosen by the user, while the other values are constants.
