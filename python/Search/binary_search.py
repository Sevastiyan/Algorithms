def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last: 
        middle = int((first + last) / 2)
        if arr[middle] == target:
            return middle
        
        if target < arr[middle]:
            last = middle - 1
        else: 
            first = middle + 1 
    
    return -1


def main(): 
    arr = [-5, 2, 4, 6, 10]
    print(binary_search(arr, 10))
    print(binary_search(arr, 6))
    print(binary_search(arr, 20))

# Big-O = O(logn)

if __name__ == '__main__':
    main()