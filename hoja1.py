# Tasukete Kudasai
import random
import matplotlib.pyplot as plt
import numpy as np
import time

def f1(p):
  return (p[0]/2, p[1]/2)

def f2(p):
  return(p[0]/2 + 0.5, p[1]/2)

def f3(p):
  return(p[0]/2 + 0.25, p[1]/2 + 0.5)


def shierpinski(p = (40, 40), iterations = 100000):
  print("Shierpinski")
  i = 0
  ps = []
  temp = p
  while i < iterations:
    ps.append(p)
    x = random.random()
    if x < .25:
      p = f1(p)
    elif x<.50:
      p = f2(p)
    elif x<1:
      p = f3(p)
    i += 1

  x = []
  y = []
  for point in ps:
    x.append(point[0])
    y.append(point[1])
  plt.plot(x, y, '.')

  plt.show()

# La mejor parte para darle mayor probabilidad es la 3. 

#Ejercicio 3
def p1(mem):
  return ((5**5) * mem ) % ((2**35)-1)

def p2(mem):
  return ((7**5) * mem ) % ((2**31)-1)

def puntos(p1, limite):
  num = 0
  for p in p1:
    if limite - 0.1 <= p < limite:
      num += 1
  num = num / len(p1) * 100
  a = "*"*int(num)
  mensaje = a+ " %d" %int(num) + "%"
  return mensaje

def graficar(p1, p2, p3):
  for i in range(len(p1)):
    p1[i] = p1[i] / ((2**35)-1)
    p2[i] = p2[i] / ((2**31)-1)
  x = .1
  print("Generador 1")
  while x < 1:
    print( "%.1f" %(x-0.1), "-", "%.1f" %x, " ", puntos(p1, x))
    x += 0.1
  print("Generador 2")
  x = 0.1
  while x < 1:
    print( "%.1f" %(x-0.1), "-", "%.1f" %x, " ", puntos(p2, x))
    x += 0.1
  x = 0.1
  print("Generador local")
  while x < 1:
    print( "%.1f" %(x-0.1), "-", "%.1f" %x, " ", puntos(p3, x))
    x += 0.1
  

def generadores(iter = 100, seed = time.time()):
  print("Comparando Generadores")
  r1 = [seed]
  r2 = [seed]
  r3 = []
  i = 0
  while i < iter:
    r1.append(p1(r1[i]))
    r2.append(p2(r2[i]))
    r3.append(random.random())
    i+=1
  graficar(r1, r2, r3)



if __name__ == "__main__":
  print("Ejercicios 1 y 5")
  while(1):
    op = input("1. Ejercicio 1 \n2. Ejercicio 5 \n3. Salir\n")
    if op == "1":
      shierpinski()
    elif op == "2":
      iter = input("Iteraciones: ")
      generadores(int(iter))
    elif op == "3":
      break