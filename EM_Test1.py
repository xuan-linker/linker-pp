import math


# Expectation for P(A)
def probability_a(p_a, p_b, coin_h, coin_t):
    print("%.4f %.4f %.4f %.4f" % (p_a, p_b, coin_h, coin_t))
    mid_p_a = math.pow(p_a, coin_h) * math.pow(1 - p_a, coin_t)
    mid_p_b = math.pow(p_b, coin_h) * math.pow(1 - p_b, coin_t)
    result = mid_p_a / (mid_p_a + mid_p_b)
    return result


def probability_b(p_a, p_b, coin_h, coin_t):
    mid_p_a = probability_a(p_a, p_b, coin_h, coin_t)
    result = 1 - mid_p_a
    return result


def print_num(num, p_a, p_b, coin_h, coin_t):
    print("-------------", num)

    print_num_pa = probability_a(p_a, p_b, coin_h, coin_t)
    print("pa  %.8f" % print_num_pa)

    print_num_pb = 1 - probability_a(p_a, p_b, coin_h, coin_t)
    print("pb  %.8f" % print_num_pb)
    print("-------------", num)

    return [print_num_pa, print_num_pb]


# a = math.pow(0.6, 9) * math.pow(0.4, 1)
#
# b = math.pow(0.5, 10)
#
# p2 = a / (a + b)
# print("p2 : %.8f" % p2)
#
# ep2a = 9 * p2
# print("ep2a : %.8f" % ep2a)
#
# ep2b = 9 * (1 - p2)
# print("ep2b : %.8f" % ep2b)
#
# pa3 = probability_a(0.6, 0.5, 8, 2)
# print("pa3 %.8f" % pa3)
#
# pb3 = 1 - pa3
# print("pb3 %.8f" % pb3)
nums = []

for i in range(1, 5):
    if i == 1:
        nums.append(print_num(1, 0.6, 0.5, 5, 5))
    elif i == 2:
        nums.append(print_num(2, 0.6, 0.5, 9, 1))
    elif i == 3:
        nums.append(print_num(3, 0.6, 0.5, 8, 2))
    elif i == 4:
        nums.append(print_num(4, 0.6, 0.5, 4, 6))
    elif i == 5:
        nums.append(print_num(5, 0.6, 0.5, 7, 3))
print(nums)

sigma = 1 / (math.sqrt(2 * math.pi))
print("first sigma={0}".format(sigma))
# def functionname( parameters ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]

# def printme(str):
#     "打印任何传入的字符串"
#     print
#     str
#     return
