S = [-1, 0, 1, 2, -1, -4]
output = []


def is_odd(num):
    if num % 2 == 0:
        return False
    return True


def find_3sums(arr):
    count = 0
    sorted_array = sorted(arr)
    i = 0
    j = len(sorted_array) - 1
    k = i + 1
    while(True):
        found = False
        if i == j - 1:
            break
        for k in range(i + 1,  j):
            if arr[i] + arr[j] + arr[k] == 0:
                output.append([arr[i], arr[j], arr[k]])
                break
        if found is True:
            continue
        elif is_odd(count):
            i += 1
        else:
            j -= 1
        count += 1


def find_3sums_dict(arr):
    values = set()
    for item in arr:
        values.add(item)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if -(arr[i] + arr[j]) in values:
                output.append([arr[i], arr[j], -(arr[i] + arr[j])])


def find_3sums_alternate(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 2):
        if arr[i] == arr[i - 1]:
            continue
        start, end = i + 1, len(arr) - 1
        while start < end:
            if arr[i] + arr[start] + arr[end] == 0:
                output.append([arr[i], arr[start], arr[end]])
                start += 1
                end -= 1
                while start < end and arr[start] == arr[start - 1]:
                    start += 1
                while end > start and arr[end] == arr[end + 1]:
                    end -= 1
            elif arr[start] + arr[end] > -(arr[i]):
                end -= 1
            else:
                start += 1


find_3sums_alternate(S)
print output
