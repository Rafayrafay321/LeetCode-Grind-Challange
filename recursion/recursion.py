"""# printing the name using the recursion

def printName(n):
    if n == 0:
        return
    print("Abdul rafay")
    printName(n - 1)

n = 5
printName(n)"""

# printing the 1 till n number using the recursion

"""def printNum(i,n):
    if i > n:
        return
    print(i)
    printNum(i + 1,n)

i = 1
n =5
printNum(i,n)"""

# print in the reverse like n to 1

"""def reversenum(i,n):
    if i > n:
        return
    reversenum(i + 1,n)
    print(i)

i = 1
n =5
reversenum(i,n)
"""
# print the 1 to n using the back tracking

"""def numUsingbackT(i):
    if i < 1:
        return 
    numUsingbackT(i - 1)
    print(i)

n = 5
i = 5
numUsingbackT(i)"""

# print n to 1 using the backtracking
"""""def reverseBacktrack(i,n):
    if i > n:
        return
    reverseBacktrack(i + 1,n)
    print(i)

i = 1
n = 5
reverseBacktrack(i,n)"""""

# sum of the N numbers using the recursion
# Functional way

"""def SumUseRec(n):
    if n == 0:
        return 0
    return n + SumUseRec(n - 1)

n = 5
print(SumUseRec(n))"""

# reverse the list using the 
