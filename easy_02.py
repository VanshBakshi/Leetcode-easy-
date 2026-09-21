class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Numbers ending in 0 are not palindromes
        # except 0 itself
        if x != 0 and x % 10 == 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num
