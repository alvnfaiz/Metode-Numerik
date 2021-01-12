#Nama       : Alvin Faiz Zulfitri
#Kelas      : TRPL 2 B
#No BP      : 1811081025
#Program    : Program pencarian polinomial
import sympy as sym
import colorama
from colorama import Fore, Style
import sys
import time
x = sym.Symbol('x')

def main():
	print(Fore.GREEN)
	mengetik("|===============================|\n|1. Bisection\n|2. Regula Falsi\n|3. Newthon Rapshon\n|4. Secant\n|================================|")
	print(Fore.BLUE)
	p = int(input("Metode yang digunakan  = "))
	if(p==1 or p==2 or p==4):
		a = float(input("Titik x1 = "))
		b = float(input("Titik x2 = "))
	else:
		a = float(input("Titik x1 = "))

	f = input("Fungsi = ")
	print(Fore.GREEN)
	if(p==1):
		mengetik("Metode Bisection Method")
		bisection(a,b,f)
	elif(p==2):
		mengetik("Metode Regula Falsi")
		regulaFalsi(a,b,f)
	elif(p==3):
		mengetik("Metode Newthon Raphson")
		newtonRaphson(a,f)
	elif(p==4):
		mengetik("Metode Secant")
		secant(a,b,f)
	else:
		print("404 | Input metode tidak ditemukan")

def bisection(a,b,fn):
	f = eval("lambda x : " + fn)
	if(f(a)*f(b)>0):
		print("Fungsi tidak memiliki akar, Ulang kembali")
		main()
	else:
		c = float((a+b)/2)
		fc = f(c)
		print("x(t) = %.6f"%c, "\t f(x(t)) = %.6f"%fc)
		if(f(c)*f(a)<0):
			b = c
		else:
			a = c
		if(abs(f(c))<=0.00001):
			print("Akar Persamaan  = %.5f"%c, "\t f(x(t)) = %.6f"%fc )
			return
		else:
			bisection(a,b,fn)

def regulaFalsi(a,b,fn):
	f = eval("lambda x : " + fn)
	if(f(a)*f(b)>0):
		print("Fungsi tidak memiliki akar, Ulang kembali")
		main()
	else:
		c = a-f(a)*((b-a)/(f(b)-f(a)))
		fc = f(c)
		print("x(t) = %.6f"%c, "\t f(x(t)) = %.6f"%fc)
		if(f(c)*f(a)<0):
			b = c
		else:
			a = c
		if(abs(f(c))<=0.00001):
			print("Akar Persamaan  = %.5f"%c, "\t f(x(t)) = %.6f"%fc )
			return
		else:
			regulaFalsi(a,b,fn)

def newtonRaphson(a,fn):
	f2 = str(sym.diff(fn))
	f = eval("lambda x : " + fn)
	fa = eval("lambda x : " + f2)
	b = a - f(a)/fa(a)
	fb = f(b)
	if(abs(fb)<=0.0001):
		print("Akar Persamaan  = %.5f"%b, "\t f(x(t)) = %.10f"%fb )
	else:
		a=b
		newtonRaphson(a,fn)

def secant(a,b,fn):
	f = eval("lambda x : " + fn)
	c = b - f(b)*(b-a)/(f(b)-f(a))
	fc =  f(c)
	if(abs(f(c))>0.00001):
		a=b
		b=c
		secant(a,b,fn)
	else:
		print("Akar Persamaan  = %.5f"%c, "\t f(x(t)) = %.6f"%fc )
		return

import time
def mengetik(s):
    print()
    for c in s:
        sys.stdout.write(Fore.GREEN + c )
        sys.stdout.flush()
        time.sleep(0.05)
    print()

main()
