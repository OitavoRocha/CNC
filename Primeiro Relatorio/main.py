import math
from sympy import *

# ----- Perguntar -----
# 1) Tá dando problema quando eu tento fazer a expressão com ln x (newton)
# 2) Oq fazer no newton quando já nos é dado o x0, devo levar isso em consideração dentro da 
# função ou faço na mão mesmo   
# 3) Qual o resultado do que tá no slide do primeiro exemplo de secante?


def bisection(f, a, b, precision, n):   
    if (f(a) * f(b) > 0):
        return None
    
    if (abs(b - a) < precision):
        return (a + b) / 2
    
    k = 0
    m = f(a)
    
    for i in range(n):

        x = (a + b) / 2

        if ((m * f(x)) > 0):
            a = x
        elif ((m * f(x)) < 0):
            b = x

        if (abs(b - a) < precision):
            break

        if (abs(f(x)) < precision):
            break
        k += 1

    return x

def fake_position(f, a, b, precision, n):
    if (f(a) * f(b) > 0):
        return None
    
    if (abs(b - a) < precision):
        return (a + b) / 2
    
    k = 0
    m = f(a)
    
    for i in range(n):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if (abs(f(x)) < precision):
            break
        
        if ((m * f(x)) > 0):
            a = x
        elif ((m * f(x)) < 0):
            b = x
        
        if (abs(b - a) < precision):
            break

        k += 1    

    return x

def newton_raphson(f, a, b, precision, n):
    x = symbols('x')
    x0 = 0

    dx = diff(f(x), x)
    dxdx = diff(diff(f(x), x), x)
    da = dxdx.subs(x, a)
    db = dxdx.subs(x, b)
    
    print(dx, dxdx)

    if (f(a) * da > 0.0):
        x0 = a
    elif (f(b) * db > 0.0):
        x0 = b
    # Se nenhum dos dois for maior que zero então não tem raiz?

    print(x0)

    x0 = 0.75

    k = 1

    for _i in range(n):
        x1 = x0 - (f(x0) / dx.subs(x, x0))
        if ( abs(f(x1)) < precision ):
            return x1
        x0 = x1
        k += 1

    return x0

def secant(f, a, b, precision, n):
    # x0 é a; x1 é b
    if ( abs(f(a)) < precision ):
        return a
    
    if ( abs(f(b)) < precision or abs(b - a) < precision ):
        return b

    k = 1

    for _i in range(n):
        x = b - (f(b)/ ( f(b) - f(a) )) * (b - a)
        if ( abs(f(x)) < precision or abs(x - b) < precision ):
            return x
        a = b
        b = x
        k += 1

    return x

def main():
    #f = lambda x: 2 * x ** 3 + log(x) - 5
    #f = lambda x: x ** 3 - 5 * x**2 + x + 3
    #f = lambda x: x ** 3 - 9 * x + 3
    f = lambda x: x ** 3 - 5 * x ** 2 + 17 * x + 21
    a = -1
    b = 1
    precision = -100 #5 * 10**-4
    n = 8

    root = secant(f, a, b, precision, n)
    if (root == None):
        print("Não foi possível encontrar a raiz")
    else:
        print("Raiz encontrada: ", root)


if __name__ == "__main__":
    main()