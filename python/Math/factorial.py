def factorial(n): 
    result = 1
    for i in range(1, n+1):
        result = result * i

    return result

def main(): 
    # Given a number 'n' find the first 'n' elements in the Fibonacci sequence.
    print(factorial(3))
    print(factorial(5))
    print(factorial(8))

# Big-O = O(n)

if __name__ == "__main__": 
    main()
