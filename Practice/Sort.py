def quickSort(items):
    # base case [] or [1]
    if len(items) < 2:
        return items
    pivot = items[0]

    lower = []
    higher = []
    for i in items[1:]:  # remove pivot number
        if i <= pivot:
            lower.append(i)
        else:
            higher.append(i)

    return quickSort(lower) + [pivot] + quickSort(higher)


def swp(items, a, b):
    items[a], items[b] = items[b], items[a]


def bubbleSort(items):
    n = len(items)
    for i in range(n):
        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                swp(items, j, j + 1)
    return items


def selectionSort(items):
    for i in range(len(items)):
        lowest = i
        for j in range(i, len(items)):
            if items[j] < items[lowest]:
                lowest = j
        swp(items, i, lowest)
    return items


def insertionSort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j - 1] > items[j]:
            swp(items, j, j - 1)
            j -= 1

    return items


# Function to perform insertion sort on a list
def insertionSort2(A):
    # Start from the second element
    # (the element at index 0 is already sorted)
    for i in range(1, len(A)):

        value = A[i]
        j = i

        # find index `j` within the sorted subset `A[0…i-1]`
        # where element `A[i]` belongs
        while j > 0 and A[j - 1] > value:
            A[j] = A[j - 1]
            j = j - 1

        # Note that sublist `A[j…i-1]`is shifted to
        # the right by one position, i.e., `A[j+1…i]`

        A[j] = value


if __name__ == '__main__':
    items1 = [5, 4, 3, 2, 1]
    items2 = [1, 4, 3, 2, 1]
    items3 = [5, 3, 3, 2, 1]

    print(quickSort(items1))
    print(quickSort(items2))
    print(quickSort(items3))

    print("===========")

    print(bubbleSort(items1))
    print(bubbleSort(items2))
    print(bubbleSort(items3))

    print("===========")

    print(selectionSort(items1))
    print(selectionSort(items2))
    print(selectionSort(items3))

    print("===========")

    print(insertionSort(items1))
    print(insertionSort(items2))
    print(insertionSort(items3))

    print("===========")

    print(insertionSort2(items1))
    print(insertionSort2(items2))
    print(insertionSort2(items3))
