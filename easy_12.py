class Solution:
    def plusOne(self, digits):
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            # 9 becomes 0 and carry goes to the left
            digits[i] = 0

        # If all digits were 9
        return [1] + digits
