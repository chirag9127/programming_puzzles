import pytest


def swap(arr, i, j):
    """
    function for swapping the ith and jth elements of the array
    """
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def permutations(arr):
    output = []

    def generate_permutations(arr, pos=0):
        """
        the recursive function to generate the permutations
        """
        if pos == len(arr):
            output.append(''.join(arr))
            return
        for i in range(len(arr)):
            swap(arr, pos, i)
            generate_permutations(arr, pos + 1)
            swap(arr, pos, i)
    generate_permutations(arr)
    return set(output)


@pytest.mark.parametrize("input_array,expected_permutations", [
    (['1', '2', '3', '4'],
     set(['1234', '1243', '1342', '1324', '1423', '1432',
          '2134', '2143', '2341', '2314', '2431', '2413',
          '3142', '3124', '3214', '3241', '3412', '3421',
          '4123', '4132', '4213', '4231', '4312', '4321'])),
    (['1', '2', '3'],
     set(['123', '132', '213', '231', '312', '321'])),
])
def test_permutations(input_array, expected_permutations):
    assert permutations(input_array) == expected_permutations
