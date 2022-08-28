def power_of_two(n): 
    if n < 1: 
        return False

    while n > 1: 
        if not n % 2 == 0: 
            return False
        n = n / 2
    
    return True


def power_of_two_bitwise(n):
    if n < 1: 
        return False

    return n & n-1 == 0


def main(): 
    # Given a number 'n' find the first 'n' elements in the Fibonacci sequence.
    print(power_of_two(3))
    print(power_of_two(5))
    print(power_of_two(8))

    print(power_of_two_bitwise(3))
    print(power_of_two_bitwise(5))
    print(power_of_two_bitwise(8))

# Big-O = O(logn) for power_of_two()
# Big-O = O(1) for power_of_two_bitwise()

if __name__ == "__main__": 
    main()
