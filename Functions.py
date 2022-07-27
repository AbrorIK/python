# ggT
def ggT(x, y):
    if y == 0:
        return x
    else:
        return ggT(y, x % y)


# Multiplikation
def multiplication(Erste_Faktor, Zweite_Faktor):
    Produkt = Erste_Faktor
    i = 1
    while i < Zweite_Faktor:
        Produkt += Erste_Faktor
        i += 1
    return Produkt


# Potenz
def pow(x, n):
    if n == 0:
        return 1
    elif n > 0:
        if n == 1:
            return x
        else:
            return x * pow(x, n - 1)
    else:
        if n == -1:
            return 1 / x
        else:
            return 1 / x * pow(x, n + 1)


# Fakultät
def fakultaet(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fakultaet(n - 1)


# Wurzel
def square_root(a):
    x = 1
    while abs(x ** 2 - a) > 0.00000000001:
        x = (x + a / x) / 2
    return x


# Exponentiale Funktion:
def exponent(Exponent):
    # 1 + x + x ** 2 / 2 + x ** 3 / 6 + ...
    sum = 0
    for n in range(0, 100):
        a = Exponent ** n / fakultaet(n)
        sum += a
    return sum


# e
def e():
    sum = 0
    for n in range(0, 30):
        a = n / fakultaet(n)
        sum += a
    return sum


# Potenz
def potenz(Basis, Exponent):
    i = 1
    c = Basis
    if Basis % 1 != 0 or Exponent % 1 != 0:
        import math
        return exponent(Exponent * math.log(Basis, e))
        # n = multiplication(y, math.log(x, e))
    else:
        if Exponent == 0:
            c = abs(Basis)
        while i < abs(Exponent):
            c *= Basis
            i += 1
        if Exponent < 0:
            c = 1 / c
        elif Exponent == 0:
            c = abs(Basis)
        return c


# kgV
def kgV(Zahl_1, Zahl_2):
    a = multiplication(Zahl_1, Zahl_2) / ggT(Zahl_1, Zahl_2)
    return a


# Fibonacci Zahlen
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Zahl Pi
def pi():
    import math
    n = 6
    S1 = 1
    a = math.sqrt(1 - (S1 / 2) ** 2)
    b = 1 - a
    S2 = math.sqrt(b ** 2 + (S1 / 2) ** 2)
    P = S1 * n
    Pi = P / 2
    i = 0
    while n < 100000000000:
        n *= 2
        S1 = S2
        a = math.sqrt(1 - (S1 / 2) ** 2)
        b = 1 - a
        S2 = math.sqrt(b ** 2 + (S1 / 2) ** 2)
        P = S1 * n
        Pi = P / 2
        i += 1
    return Pi


# Binomial Koeffizient
def binom(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binom(n - 1, k - 1) + binom(n - 1, k)


def efkt(x, i):
    def a(x, i):
        if i > 0:
            return a(x, i - 1) * x / i
        else:
            return 1

    if i > 0:
        return efkt(x, i - 1) + a(x, i)
    else:
        return 1





# cosine
def cosine(x, n):
    if n == 0:
        return 1
    else:
        return cosine(x, n - 1) + (x ** (2*n) * (-1) ** n / fakultaet(2 * n))



# sinus
def sinus(winkel):
    sin = 0
    for n in range(0, 50):
        sin += ((-1) ** n) * (winkel ** (2 * n + 1)) / (fakultaet(2 * n + 1))
    return sin


# Turm von Hanoi
def h(n, start, end):
    def pm(start, end):
        print(start, '-->', end)
    if n == 1:
        pm(start, end)
    else:
        other = 6 - (start + end)
        h(n - 1, start, other)
        pm(start, end)
        h(n - 1, other, end)


