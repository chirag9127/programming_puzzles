"""
Say you have an array for which the ith element is the price of a
given stock on day i.

Design an algorithm to find the maximum profit.
You may complete at most two transactions.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
import pytest


def get_max_stock_in_local(prices):
    curr_max, total_max = 0, 0
    for i in range(1, len(prices)):
        curr_max = max(prices[i] - prices[i - 1] + curr_max, 0)
        total_max = max(curr_max, total_max)
    return total_max


def stock_purchase_3(stock_prices):
    """
    This does it in O(n^2).
    """
    total_max = 0
    for i in range(1, len(stock_prices)):
        left, right = stock_prices[:i + 1], stock_prices[i + 1:]
        left_max, right_max = (get_max_stock_in_local(left),
                               get_max_stock_in_local(right))
        total_max = max(left_max + right_max, total_max)
    return total_max


@pytest.mark.parametrize("stock_prices,expected_output", [
    ([7, 1, 5, 3, 6, 4], 7),
    ([7, 6, 4, 3, 1], 0),
    ([7, 1, 5, 4, 7, 2, 3, 1, 6, 4], 11),
    ([1, 5, 2, 6, 4, 3, 2, 1], 8),
    ([], 0),
    ([1, 5, 4, 7, 3, 8], 11),
])
def test_stock_purchase_3(stock_prices, expected_output):
    assert stock_purchase_3(stock_prices) == expected_output
