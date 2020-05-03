class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            mod_s = (''.join(e for e in s if e.isalnum())).lower()
            rev_s = mod_s[::-1]
        return True if mod_s == rev_s else False
            