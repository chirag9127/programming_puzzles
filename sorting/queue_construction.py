"""
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people
in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.
"""


def queue_reconstruction(array):

    array.sort(key=lambda x: (-x[0], x[1]))
    queue = []
    for item in array:
        queue.insert(item[1], item)

    return queue
