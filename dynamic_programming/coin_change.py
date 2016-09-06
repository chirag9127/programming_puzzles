"""
You are given coins of different denominations and a
total amount of money amount.
Write a function to compute the fewest number of coins that
you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.
"""
import pytest


LARGE = 999999


def coin_change(coins, amount):
    # Time complexity is O(len(coins)*amount)
    output_arr = [LARGE] * (amount + 1)
    output_arr[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                output_arr[i] = min(output_arr[i], output_arr[i - coin] + 1)
    return output_arr[amount] if output_arr[amount] != LARGE else -1


@pytest.mark.parametrize("coins,amount,expected_output", [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
])
def test_coin_change(coins, amount, expected_output):
    assert coin_change(coins, amount) == expected_output
