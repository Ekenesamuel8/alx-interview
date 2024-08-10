#!/usr/bin/python env
"""calculates the fewest number of operations needed"""


def minOperations(n):
    """n: number of times given
    prime_nub: prime factor of the n number
    return the sum of the prime factor
    """
    if n <= 1:
        return 0

    prime_nub = 0
    div_num = 2

    while n > 1:
        while n % div_num == 0:
            prime_nub += div_num
            n //= div_num
        div_num += 1
