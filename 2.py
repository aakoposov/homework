from math import*
AB=input("первый катет:")
AC=input("второй катет:")
AB=float(AB)
AC=float(AC)
BC=sqrt(AB**2+AC**2)
P=(AB+AC+BC)
S=(AB+AC)/2
print("площадь:",S)
print("периметр:",P)