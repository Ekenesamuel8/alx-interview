#!/usr/bin/python3
"""solution to making change problem"""


def makeChange(coins, total):
    """ Edge case: if total is 0 or less, no coins are needed
    """
    if total <= 0:
        return 0

    """ Initialize dp array with "infinity", except dp[0] which is 0
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    """ Fill the dp table
    """
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    """ If dp[total] is still "infinity", the total can't be reached
    """
    return dp[total] if dp[total] != float('inf') else -1
