"""
Given a list of transactions between a group of people,
return the minimum number of transactions required to settle the debt.
"""
import pytest


@pytest.mark.parametrize("transactions,output", [
    ([[0, 1, 10], [2, 0, 5]], 2),
    ([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]], 1),
    ([[1, 5, 8], [8, 9, 8], [2, 3, 9], [4, 3, 1]], 4),
    ([[1, 2, 3], [1, 3, 3], [6, 4, 1], [5, 4, 4]], 4),
])
def test_optimal_account_balancing(transactions, output):
    assert optimal_account_balancing(transactions) == output


def update_balances(user, amount, balances):
    if user not in balances:
        balances[user] = 0
    balances[user] += amount


def optimal_account_balancing(transactions):
    balances = {}
    for transaction in transactions:
        debtor, creditor, amount = transaction
        update_balances(debtor, -1 * amount, balances)
        update_balances(creditor, amount, balances)

    balances_values = balances.values()

    balance_set = set([balance for balance in balances_values])

    num_transactions = 0
    for balance in balances_values:
        if -1 * balance in balance_set:
            balances_values.remove(balance)
            balances_values.remove(-1 * balance)
            num_transactions += 1
        elif balance == 0:
            balances_values.remove(balance)

    balances_values = list(balances_values)

    num_transactions += dfs(0, 0, balances_values)

    print(num_transactions)

    return num_transactions


def dfs(position, count, balances_values):
    while position < len(balances_values) and balances_values[position] == 0:
        position += 1
    if position == len(balances_values):
        return count

    result = 999999
    for i in range(position + 1, len(balances_values)):
        if balances_values[i] * balances_values[position] < 0:
            balances_values[i] += balances_values[position]
            result = min(
                result, dfs(position + 1, count + 1, balances_values))
            balances_values[i] -= balances_values[position]

    if result < 999999:
        return result
    return count
