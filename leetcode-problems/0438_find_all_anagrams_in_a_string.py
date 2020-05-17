import collections

"""

My Approach:
- dictionary keeping the count of the subarray of len(p).
- if the count of substring(s) == count of p, then append the index.
- O(n), O(n)
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not (s and p):
            return None
        n = len(p)

        # init s_window with first len(p) elements.
        p_cnt, s_window = collections.Counter(p), collections.Counter(s[0:n])
        ans = []

        # check for first substring of s. If same, then add 0th index.
        if s_window == p_cnt:
            ans.append(0)

        for idx in range(n, len(s)):
            """
            c1 - last element of current window --> increment count
            c2 - first element of previous window --> decrement count
            """
            c1, c2 = s[idx], s[idx - n]
            s_window[c1] = s_window.setdefault(c1, 0) + 1
            s_window[c2] = s_window.setdefault(c2, 0) - 1

            # remove items which have values = 0
            s_window = {k: v for k, v in s_window.items() if v != 0}

            if s_window == p_cnt:
                ans.append(idx - n + 1)
        return ans

