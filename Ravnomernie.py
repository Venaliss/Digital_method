import math


const = (2/math.sqrt(math.pi))
a, b, n, m = 0, 2, 5, 10
h = (b - a) / n
x_i = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

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


# разбиваем отрезок [a, b] на n частей и считаем f_x
x, f_x = [], []
for i in range(n+1):
    x += [round(a + i*h, 2)]
    f_x += [Erf_T(x[i])]


L_x, err = [], []
for i in range(len(x_i)):
    L_x += [Lagrange(x, f_x, x_i[i])]
    err += [abs(Erf_T(x_i[i]) - L_x[i])]

for i in range(len(x_i)):
    print(x_i[i], Erf_T(x_i[i]), L_x[i], abs(Erf_T(x_i[i]) - L_x[i]))
