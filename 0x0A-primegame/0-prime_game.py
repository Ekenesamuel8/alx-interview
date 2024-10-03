#!/usr/bin/python3
"""prime game"""


def sieve_of_eratosthenes(n):
    """Returns a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes


def isWinner(x, nums):
    """Determine the winner of the most rounds in the game."""
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to precompute primes only once
    max_n = max(nums)

    # Get the list of primes up to max_n
    primes = sieve_of_eratosthenes(max_n)

    # Keep track of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        turns = len(primes_in_game)

        # Maria starts, so if turns are odd, Maria wins, if even, Ben wins
        if turns % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
