#!/usr/bin/python3
"""Determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers"""


def isWinner(rounds, nums):
    """Determines the winner of the game."""
    if rounds <= 0 or nums is None or rounds != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    primenum = [1] * (max(nums) + 1)
    primenum[0], primenum[1] = 0, 0

    for i in range(2, len(primenum)):
        remove_multiples(primenum, i)

    for num in nums:
        if sum(primenum[:num + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


def remove_multiples(lst, x):
    """Removes multiples of primes."""
    for i in range(2, len(lst)):
        try:
            lst[i * x] = 0
        except IndexError:
            break