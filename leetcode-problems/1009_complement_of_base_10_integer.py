class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        else:return N ^ (2 ** N.bit_length() - 1)