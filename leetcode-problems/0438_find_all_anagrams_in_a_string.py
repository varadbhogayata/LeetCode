import collections

"""

My Approach:
- dictionary keeping the count of the subarray of len(p).
- if the count of substring(s) == count of p, then append the index.
- O(Ns + Np), O(1) (as max 26 characters)
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        # init s_window with first len(p) elements.
        p_cnt, s_window = collections.Counter(p), collections.Counter(s[0:np])
        ans = []

        # check for first substring of s. If same, then add 0th index.
        if s_window == p_cnt:
            ans.append(0)

        for idx in range(np, ns):
            """
            c1 - last element of current window --> increment count
            c2 - first element of previous window --> decrement count
            """
            c1, c2 = s[idx], s[idx - np]
            s_window[c1] = s_window.setdefault(c1, 0) + 1

            if s_window[c2] > 1:
                s_window[c2] = s_window.setdefault(c2, 0) - 1
            else:
                del s_window[c2]

            if s_window == p_cnt:
                ans.append(idx - np + 1)
        return ans

