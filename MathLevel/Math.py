accuracy = 5

def factorial(n):
    if isinstance(n, int):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res


def sin(angel):
    if isinstance(angel, float) or isinstance(angel, int):
        res = 0
        for k in range(10):
            res += ((-1)**k)*(angel ** (2*k+1))/(factorial(2*k+1))
        return res


def cos(angel):
    if isinstance(angel, float) or isinstance(angel, int):
        res = 0
        for k in range(10):
            res += ((-1)**k)*(angel ** (2*k))/(factorial(2*k))
        return res


def arctg(x):
    res = 0
    for k in range(1, 10):
        res += (((-1)**(k-1))*x**(2*k-1))/(2*k-1)
    return res