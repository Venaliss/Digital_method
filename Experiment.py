import math
import matplotlib.pyplot as plt

def erf_ch(n):
    def Cheb(n):
        a, b, pi = 0, 2, math.pi
        x_ch = []
        if n % 2 == 1:
            for i in range(n + 1):
                x_i = (b + a) / 2 + (b - a) * math.cos((2 * i + 1) * pi / (2 * n + 2)) / 2
                x_ch += [x_i]
        else:
            for i in range(1, n + 1):
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
                    term *= (value - x[j]) / (x[i] - x[j])
            result += term
        return result

    const = (2 / math.sqrt(math.pi))
    a, b, m = 0, 2, 10
    h = (b - a) / n
    x_i = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    x_ch, f_ch = Cheb(n), []

    for i in range(len(x_ch)):
        f_ch += [Erf_T(x_ch[i])]

    L_ch, err_ch = [], []
    for i in range(len(x_i)):
        L_ch += [Lagrange(x_ch, f_ch, x_i[i])]
        err_ch += [abs(Erf_T(x_i[i]) - L_ch[i])]

    return max(err_ch)
def erf_n(n):
    const = (2 / math.sqrt(math.pi))
    a, b, m = 0, 2, 10
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
                    term *= (value - x[j]) / (x[i] - x[j])
            result += term
        return result

    x, f_x = [], []
    for i in range(n + 1):
        x += [round(a + i * h, 2)]
        f_x += [Erf_T(x[i])]

    L_x, err = [], []
    for i in range(len(x_i)):
        L_x += [Lagrange(x, f_x, x_i[i])]
        err += [abs(Erf_T(x_i[i]) - L_x[i])]
    return max(err)

n, err = [], []
for i in range(5, 45):
    if i % 10 == 0:
        continue
    else:
        n += [i]
        err += [erf_ch(i)]
        print(i, erf_ch(i))
plt.plot(n, err)
plt.show()