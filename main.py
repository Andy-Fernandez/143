import math
import sys

'''for a in sys.stdin:
	a=str(a.strip())
	if a=="":
		continue
	l=list(map(int,input().split()))
	b = l[0]*l[1]*l[2]*l[3]*l[4]*l[5]
	a = str(pow(int(a),b))
	print(a[len(a)-1])
	print()'''

'''import sys
x = iter(sys.stdin.readlines()) # iterador
n = int(next(x))
for _ in range(n):
	a, b = map(int, next(x).split())
	if (a+2)/2>=b:
		print(int((b+2)/2))
	else:
		print(int((a-b+1)/2)+1)'''

'''import sys
x = iter(sys.stdin.readlines()) # iterador
n = int(next(x))
for _ in range(n):
	a = int(next(x))
	if a==1:
		print(192)
	else:
		print(192+250*(a-1))'''

import sys
x = iter(sys.stdin.readlines()) # iterador
a,b = map(int, next(x).split())
c = next(x)
if(b>0):
	print(c[abs(b)+1:] + ' '+c[:abs(b)])
else:
	print(c[:abs(b)]+c[abs(b):])



'''for a in sys.stdin:
	a=str(a.strip())
	print("a:" +  a)
	if a=="":
		continue
	l=list(map(int,input().split()))
	print(l)
	for i in l:
		a=str(int(a[len(a)-1])**i)
	print(a[len(a)-1])
	print()'''

'''
for j in sys.stdin.readlines():
    x = int(sys.stdin.readline())
    lista = sys.stdin.readline().split()
    exponente = 1
    for i in lista:
        exponente *= int(i)

    print(pow(x,exponente)%10)
'''