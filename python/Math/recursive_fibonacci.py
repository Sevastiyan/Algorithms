def recursive_f(n): 
    if n < 2: 
        return n

    return recursive_f(n - 1) + recursive_f(n - 2)


def main(): 
    # Given a number 'n' find the first 'n' elements in the Fibonacci sequence.
    print(recursive_f(3)) # 2
    print(recursive_f(5)) # 5
    print(recursive_f(8)) # 21

# Big-O = O(n)

if __name__ == "__main__": 
    main()