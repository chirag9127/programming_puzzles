arr = ['1', '2', '3', '4']

answers = set(['1234', '1243', '1342', '1324', '1423', '1432',
               '2134', '2143', '2341', '2314', '2431', '2413',
               '3142', '3124', '3214', '3241', '3412', '3421',
               '4123', '4132', '4213', '4231', '4312', '4321'])

output = []


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def generate_permutations(arr, pos=0):
    if pos == len(arr):
        output.append(''.join(arr))
        return
    for i in range(len(arr)):
        swap(arr, pos, i)
        generate_permutations(arr, pos + 1)
        swap(arr, pos, i)


generate_permutations(arr)
assert set(output) == answers
