"""
Equations are given in the format A / B = k, where A and B are variables
represented as strings, and k is a real number (floating point number).
Given some queries, return the answers.
If the answer does not exist, return -1.0.
"""
from collections import defaultdict


def test_calc_equations():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"]]

    calc_equations(equations, values, queries)
    assert calc_equations(equations, values, queries) == \
        [6.00000, 3.00000, -1.00000, 1.00000, -1.00000]


def calc_equations(equations, values, queries):
    variables = defaultdict(dict)

    for equation, value in zip(equations, values):
        variables[equation[0]][equation[0]] = 1.0
        variables[equation[1]][equation[1]] = 1.0

        variables[equation[0]][equation[1]] = value
        variables[equation[1]][equation[0]] = 1 / value

    add_neighbors(variables)

    results = []
    for query in queries:
        if query[0] in variables and query[1] in variables[query[0]]:
            results.append(variables[query[0]][query[1]])
        else:
            results.append(-1.0)

    return results


def add_neighbors(variables):
    for var in variables:
        for var1 in variables[var]:
            for var2 in variables[var]:
                variables[var1][var2] = \
                    variables[var1][var] * variables[var][var2]
