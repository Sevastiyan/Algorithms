def fibonacci(n): 
    fib = [0, 1]
    for i in range(1, n):
        print(i)
        fib.append(fib[i] + fib[i-1])
    
    return fib


def main(): 
    # Given a number 'n' find the first 'n' elements in the Fibonacci sequence.
    print(fibonacci(3))
    print(fibonacci(5))
    print(fibonacci(8))

# Big-O = O(n)

if __name__ == "__main__": 
    main()