class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 4 or n == 1:
            # print("The number: ", n)
            square_num_sum = sum([int(i) ** 2 for i in str(n)])
            n = square_num_sum
            if n == 1:
                return True
            else:
                continue
        else:
            return False