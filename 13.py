def romanToInt(s):
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]

        return res + roman[s[-1]]

# Example usage
if __name__ == "__main__":
    s = "III"
    print(romanToInt(s))  # Output: 3

    s = "IV"
    print(romanToInt(s))  # Output: 4

    s = "IX"
    print(romanToInt(s))  # Output: 9

    s = "LVIII"
    print(romanToInt(s))  # Output: 58

    s = "MCMXCIV"
    print(romanToInt(s))  # Output: 1994

    s = "MMMCMXCIX"
    print(romanToInt(s))  # Output: 3999