"""
Given a list of locations with their costs, find the minimum distance between a\
pair of points.
"""
import pytest
import heapq


def test_flight_optimization():
    flights = [('a', 'b', 5), ('b', 'a', 5),
               ('a', 'c', 2), ('b', 'c', 1), ('a', 'x', 1), ('x', 'b', 1)]
    print (flight_optimization('a', 'b', flights))
    print (flight_optimization('a', 'x', flights))
    print (flight_optimization('c', 'b', flights))
    print (flight_optimization('c', 'c', flights))


def flight_optimization(origin, destination, flights):
    """
    origin: str
    destination: str
    flights: list
    return: list, int
    """
    graph = {}
    for flight in flights:
        source, dest, cost = flight
        if source not in graph:
            graph[source] = {}
        graph[source][dest] = cost

    if origin not in graph:
        return [], -1
    queue = [(0, origin, [origin])]
    visited = set([origin])
    while len(queue) > 0:
        cost, curr, path = heapq.heappop(queue)
        if curr == destination:
            return path, cost
        for neighbor in graph[curr]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(queue, (cost + graph[curr][neighbor], neighbor,
                                       new_path))

    return [], -1
