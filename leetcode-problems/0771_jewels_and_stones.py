class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = collections.Counter(S)
        cnt = 0
        for char in J:
            if char in S:
                cnt += d[char]
        return cnt