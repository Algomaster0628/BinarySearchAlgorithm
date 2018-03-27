def binary_search(mylist, item):# Finds for a target in a given list if it is sorted.
    found = False
    first = 0
    last = len(primes) - 1
    while first <= last and not found:
        midpoint = (first + last)//2
        if item == mylist[midpoint]:
            print("Number is present in list.")
            found  = True
        else:
            if item < mylist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]
odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49]
binary_search(primes,41)
binary_search(even,52)
binary_search(odd,33)
