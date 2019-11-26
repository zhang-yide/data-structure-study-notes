"""
最大子列和问题：
    给定一个数列，选取其中连续的子序列，求子序列和的最大值。
"""
import time


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        duration = stop_time - start_time
        print('用时:', duration * 3, 'ms')
    return deco

# 暴力解法:T(N)=O(N**3)
@timer
def max_subseq_sum_1(a: list):
    length = len(a)
    max_sum = 0
    for i in range(length):
        for j in range(i+1, length):
            this_sum = 0
            for k in a[i:j+1]:
                this_sum += k
                if this_sum > max_sum:
                    max_sum = this_sum
    print(max_sum)

# 暴力解法2:T(N)=O(N**2)
@timer
def max_subseq_sum_2(a: list):
    length = len(a)
    max_sum = 0
    for i in range(length):
        this_sum = a[i]
        for j in range(i+1, length):
            this_sum += a[j]
            if this_sum > max_sum:
                max_sum = this_sum
    print(max_sum)

# 分而治之:T(N)=O(N*log(N))
@timer
def max_subseq_sum_3(a: list):
    pass

# 在线处理:T(N)=O(N)
@timer
def max_subseq_sum_4(a: list):
    length = len(a)
    max_sum = 0
    this_sum = 0
    for i in range(length):
        this_sum += a[i]  # 向右累加
        if this_sum >= max_sum:
            max_sum = this_sum  # 发现更大值则更新
        elif this_sum < 0:  # 如果当前子列和为负
            this_sum = 0  # 则不可能使后面的部分和增大，抛弃
    print(max_sum)


if __name__ == '__main__':
    a = [1] * 1000
    # a = [2, -1, 6, 8, -5, 7, -11]
    max_subseq_sum_1(a)  # 用时: 38.21978974342346 ms
    max_subseq_sum_2(a)  # 用时: 0.15259122848510742 ms
    max_subseq_sum_4(a)  # 用时: 0.002993345260620117 ms
