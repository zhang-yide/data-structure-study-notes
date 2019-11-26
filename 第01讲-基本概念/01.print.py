import time


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        duration = stop_time - start_time
        print('用时:', duration)
    return deco


@timer
def test(n: int):
    for i in range(n):
        print(i)


if __name__ == '__main__':
    test(1000)
