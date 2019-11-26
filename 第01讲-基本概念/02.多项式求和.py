"""
f(n, x) = 1 + x + 2 * x**2 + 3 * x**3 + n * x**n
比较两种不同的计算方法用时情况
"""
import time


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        duration = stop_time - start_time
        print('用时:', duration * 1000, 'ms')
    return deco


# 暴力解法：T(N)=O(N**2)
@timer
def polynomial_1(n: int, x):
    a = range(n + 1)
    total = 0
    i = 0
    while i < n + 1:
        total = a[i] * (x ** i) + total
        i += 1
    print(total)


# 先合并，后计算：T(N)= O(N)
@timer
def polynomial_2(n: int, x):
    a = range(n + 1)
    total = a[n]
    i = n
    while i > 0:
        total = a[i-1] + (x * total)
        i -= 1
    print(total)


if __name__ == '__main__':
    polynomial_1(1000, 1.1)
    polynomial_2(1000, 1.1)
