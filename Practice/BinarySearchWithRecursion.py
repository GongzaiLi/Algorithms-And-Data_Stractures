def binary_search(items, target):
    """
    items: a sorted num array
    target: a num
    """
    low = 0
    high = len(items) - 1

    while low <= high:

        mid = round((low + high) // 2)


        if target == items[mid]:
            return mid

        if items[mid] > target:
            high = mid
        else:
            low = mid

    return None


def binary_search_recursion(items, target, low=0, high=None):
    """
    items: a sorted num array
    target: a num
    """
    if high is None:
        high = len(items) - 1

    mid = round((low + high) // 2)

    if target == items[mid]:
        return mid

    if items[mid] > target:
        high = mid
    else:
        low = mid
    return binary_search_recursion(items, target, low, high)


if __name__ == '__main__':
    #   issues: Cannot return None
    my_items = [1, 3, 5, 7, 9]
    print(binary_search(my_items, -1))
    # print(binary_search_recursion(my_items, -1))
