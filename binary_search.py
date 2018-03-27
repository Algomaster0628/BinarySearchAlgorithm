primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def binary_search(mylist: list, item: int) -> bool:
    """
    checks if an item is inside a sorted list

    :param mylist: a sorted list of integers
    :param item: an integer
    """
    found = False
    first = 0
    last = len(mylist) - 1

    while first <= last and not found:
        midpoint = (first + last)//2
        if item == mylist[midpoint]:
            found = True
        else:
            if item < mylist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

print(binary_search(primes, 67))
