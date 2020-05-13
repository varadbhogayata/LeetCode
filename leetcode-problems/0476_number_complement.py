class Solution:
    def findComplement(self, num: int) -> int:
        """
        ex. 5 = 101 ---> complement = 2 (010)
        101 ^ 111 = 010. Here, 111(7 in decimal) = 2**(no of digits) - 1
        """
        return num ^ (pow(2, num.bit_length()) - 1)