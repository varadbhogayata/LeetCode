class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            # print("mid: {} l: {} r: {}".format(mid, l, r))
        return False