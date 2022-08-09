import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c
def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

def imprime_raízes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 *a)
            print("A única raíz é: , raíz1")
    else:
        if d < 0:
            print("Esta equação não possui raízes reais.")
        else:
            raíz1 = (-b + math.sqrt(d)) / (2 * a)
            raíz2 = (-b - math.sqrt(d)) / (2 *a)
            print("A primeira raíz é:", raíz1)
            print("A segunda raíz é:", raíz2)