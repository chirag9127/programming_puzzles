"""
Say you have an array for which the ith element is the price of a
given stock on day i. If you were only permitted to complete at most one
transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import pytest


def stock_purchase(input_array):
    """
    Args:
        input_array: an array of stock prices of day i
    Returns:
        max_profit: maximum profit possible based on the prices
    """
    candidate_max = 0
    total_max = 0
    for i in range(1, len(input_array)):
        candidate_max = max(input_array[i] - input_array[i - 1] + candidate_max,
                            0)
        total_max = max(total_max, candidate_max)
    print total_max


@pytest.mark.parametrize("input_array,expected_output", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
])
def test_stock_purchase(input_array, expected_output):
    assert stock_purchase(input_array) == expected_output
