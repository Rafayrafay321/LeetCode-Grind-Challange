# Pattern 1
"""i = 0
while (i < 5):
    j = 0
    while(j < 5):
        print("*" ,end="")
        j += 1
    print()
    i += 1"""

# pattern 2
"""i = 1
while (i <= 5):
    j = 0
    while (j < i):
        print("*" , end = "")
        j += 1
    print()
    i += 1
"""

# Patern 3

"""i = 1
while i < 5:
    j = 1
    while j <= i:
        print(j , end= "")
        j += 1
    print()
    i += 1"""

# pattern 4

"""i = 1
while i <= 5:
    j = 0
    while j < i:
        print(i , end = " ")
        j += 1
    print()
    i += 1"""

# pattern 5

"""i = 1
while i <= 5:
    j = 5
    while j >= i:
        print("*" , end = " ")
        j -= 1
    print()
    i += 1"""

# Pattern 6

"""i = 5
while i > 0:
    j = 1
    while j <= i:
        print(j , end = " ")
        j += 1
    print()
    i -= 1
"""
# pattern 7
"""n = 5
i = 0
while i < n:
    j = 0
    while j < (n - i - 1):
        print(" " , end = "")
        j += 1

    j = 0
    while j < ( 2 * i + 1):
        print("*" , end = "")
        j += 1

    print()
    i += 1 """

# pattern 8

n = 5
i = 0
while i < n:
    j = 5
    while j > (n - j + 1):
        print(" " , end = "")
        j -= 1

    j = 5
    while j > (2 * j + 1):
        print("*" , end = "")
        j -= 1
        
    print()
    i += 1