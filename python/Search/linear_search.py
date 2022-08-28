def linear_search(arr, target): 
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1


def main(): 
    arr = [-5, 2, 10, 4, 6]
    print(linear_search(arr, 10))
    print(linear_search(arr, 6))
    print(linear_search(arr, 20))

# Big-O = O(n)

if __name__ == '__main__':
    main()