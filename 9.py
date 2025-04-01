def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    if x % 10 == 0:
        return False
    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return x == reversed_num or x == reversed_num // 10
# Test cases
print(isPalindrome(121))  # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))  # False
print(isPalindrome(12321))  # True
print(isPalindrome(0))  # True
print(isPalindrome(1234321))  # True
print(isPalindrome(123456))  # False
print(isPalindrome(123456789987654321))  # True
print(isPalindrome(123456789))  # False
print(isPalindrome(1001))  # True
print(isPalindrome(1000001))  # True
print(isPalindrome(1234567890987654321))  # True