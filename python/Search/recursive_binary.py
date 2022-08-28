def binary_search(arr, target):
    first = 0 
    last = len(arr) - 1

    return search(arr, target, first, last)


def search(arr, target, first, last):
    if first > last:
        return -1

    middle = int((first + last) / 2)

    if target == middle:
        return middle

    if target < arr[middle]:
        return search(arr, target, first, middle - 1)
    else:
        return search(arr, target, middle + 1, last)



def main(): 
    arr = [-5, 2, 4, 6, 10]
    print(binary_search(arr, 10))
    print(binary_search(arr, 6))
    print(binary_search(arr, 2))

# Big-O = O(logn)

if __name__ == '__main__':
    main()