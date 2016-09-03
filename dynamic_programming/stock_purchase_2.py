"""
Say you have an array for which the ith element is the price of a
given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
import pytest


def stock_purchase_2(stock_prices):
    curr_max, total_profit = 0, 0
    for i in range(1, len(stock_prices)):
        curr_max = max(stock_prices[i] - stock_prices[i - 1], 0)
        total_profit += curr_max
    return total_profit


@pytest.mark.parametrize("input_array,expected_output", [
    ([7, 1, 5, 3, 6, 4], 7),
    ([7, 6, 4, 3, 1], 0),
])
def test_stock_purchase_2(input_array, expected_output):
    assert stock_purchase_2(input_array) == expected_output
