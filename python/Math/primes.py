from cmath import sqrt


def isPrime(n): 
    if n < 2: 
        return False 
    
    for i in range(2, n):
        if n%i == 0:
            return False
    
    return True


def optimisedIsPrime(n): 
    pass



def main(): 
    # Given a number, determine if it is a Prime number.
    print(isPrime(1))
    print(isPrime(5))
    print(isPrime(4))

    print(optimisedIsPrime(1))
    print(optimisedIsPrime(5))
    print(optimisedIsPrime(4))

# Big-O = O(n) for isPrime()
# Big-O = O(sqrt(n)) for optimisedIsPrime()


if __name__ == "__main__": 
    main()
