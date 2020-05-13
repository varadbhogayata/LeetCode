class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        votes = [-1] + [0] * N
        for a, b in trust:
            # a loses his chance of being the judge
            votes[a] = float('-inf')
            votes[b] += 1
        for i, v in enumerate(votes):
            # check if there is anyone got all other people's votes.
            if v == N-1: return i
        return -1