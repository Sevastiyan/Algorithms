def recursive_f(n): 
    if n == 0: #  n < 2 also works
        return 1

    return recursive_f(n-1) * n

def main(): 
    # Given a number 'n' find the first 'n' elements in the Fibonacci sequence.
    print(recursive_f(3))
    print(recursive_f(5))
    print(recursive_f(8))

# Big-O = O(n)

if __name__ == "__main__": 
    main()
