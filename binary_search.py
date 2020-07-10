def binary_search(list, item):
    '''O(logn)'''
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            high = mid - 1
        elif list[mid] < item:
            low = mid + 1
    return False