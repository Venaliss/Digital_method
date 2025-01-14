import math


def Cheb(n):
    a, b, pi = 0, 2, math.pi
    x_ch = []
    if n % 2 == 1:
        for i in range(n+1):
            x_i = (b + a) / 2 + (b - a) * math.cos((2 * i + 1) * pi / (2 * n + 2)) / 2
            x_ch += [x_i]
    else:
        for i in range(1, n+1):
            x_i = (b + a) / 2 + (b - a) * math.cos((2 * i - 1) * pi / (2 * n)) / 2
            x_ch += [x_i]
    return x_ch


def Erf_T(x):
    a_n = x
    summ = x
    n = 0
    while abs(a_n) >= 10 ** (-6):
        q = ((-1) * (x ** 2) * (2 * n + 1)) / ((n + 1) * (2 * n + 3))
        a_n = q * a_n
        summ += a_n
        n += 1
    return summ * const


def Lagrange(x, y, value):
    result = 0
    for i in range(len(x)):
        term = y[i]
        for j in range(len(x)):
            if i != j:
                term *= (value - x[j])/(x[i] - x[j])
        result += term
    return result


const = (2/math.sqrt(math.pi))
a, b, n, m = 0, 2, 5, 10
h = (b - a) / n
x, f = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0], []
x_i, f_i = [0.0, 0.4, 0.8, 1.2, 1.6, 2.0], []
x_ch, f_ch = Cheb(n), []

#заполняем массив значений функций по равномерным, чебышева и для всех наших точек
for i in range(len(x_i)):
    f_i += [Erf_T(x_i[i])]
for i in range(len(x_ch)):
    f_ch += [Erf_T(x_ch[i])]
for i in range(len(x)):
    f += [Erf_T((x[i]))]

#массив по лагранжу по равномерным и чебышевским
l_i, l_ch = [], []
for i in range(len(x)):
    l_i += [Lagrange(x_i, f_i, x[i])]
    l_ch += [Lagrange(x_ch, f_ch, x[i])]

#массив значений погрешности по равномерным и по чебышевским
err_i, err_ch = [], []
for i in range(len(x)):
    err_i += [abs(f[i] - l_i[i])]
    err_ch += [abs(f[i] - l_ch[i])]

#выводим таблицу по равномерным и чебышевским
print("-"*10, "РавномерноРаспределенные", "-"*10)
print("x[i]", "  ", "f[i]", "      ", "l_i[i]","    ", "err_i[i]")
print(x[0], "  ", f[0], "       ", l_i[0],"       ", err_i[0])
for i in range(len(x)-1):
    print(round(x[i+1], 6), "  ", round(f[i+1], 6), "  ", round(l_i[i+1], 6),"  ",round(err_i[i+1], 6))
print("")
print("-"*10, "Чебышевские", "-"*10)
print("x[i]", "  ", "f[i]", "      ", "l_ch[i]","  ", "err_ch[i]")
print(x[0], "  ", f[0], "       ", round(l_ch[0], 6),"   ", round(err_ch[0], 6))
for i in range(len(x)-1):
    print(round(x[i+1], 6), "  ", round(f[i+1], 6), "  ", round(l_ch[i+1], 6),"  ",round(err_ch[i+1], 6))
