import time


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        duration = stop_time - start_time
        print('用时:', duration * 3, 'ms')
    return deco


@timer
def test1(n):
    pass


def test2():
    a = range(10)
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(b[1:10])


if __name__ == '__main__':
    test2()
