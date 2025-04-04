pick = 6

def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

def guessNumber(n):
    l, r = 1, n
    while l <= r:
        m = (l + r) // 2
        if guess(m) == 0:
            return m
        elif guess(m) == -1:
            r = m - 1
        else:
            l = m + 1
    return -1

# Test case guessNumber
print(guessNumber(10))  # Output: 6
# Test case guessNumber
print(guessNumber(1))   # Output: 1