class Solution:
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]


if __name__ == "__main__":
    sol = Solution()
    digits = [4, 3, 2, 1]
    result = sol.plusOne(digits)
    print(result)
