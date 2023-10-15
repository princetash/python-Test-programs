# def sequence(n):
#     while n != 1:
#         print(n)
#         if n % 2 == 0:  # n is even
#             n = n / 2
#         else:  # n is odd
#             n = n*3 + 1


# sequence(3)


def print_n(s, n):
    while n > 0:
        print(s)
        n -= 1


print_n("James", 5)
