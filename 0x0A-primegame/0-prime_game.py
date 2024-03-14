#!/usr/bin/python3


def isWinner(x, nums):
    maria = 0
    ben = 0

    def SieveOfEratosthenes(n):
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False
        return prime

    max_n = max(nums)
    primes = SieveOfEratosthenes(max_n)

    for round in nums:
        round_primes = [i for i in range(round + 1) if primes[i]]
        if len(round_primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"

    return None
