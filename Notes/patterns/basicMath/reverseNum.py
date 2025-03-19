def reverseNum(n):
    firstD = 0
    while n > 0:
        lastD = n % 10
        firstD = firstD * 10 + lastD
        n //= 10
    return firstD

if __name__ == "__main__":
    n = 567846546
    print("Before: ", n)
    print(reverseNum(n))

    
