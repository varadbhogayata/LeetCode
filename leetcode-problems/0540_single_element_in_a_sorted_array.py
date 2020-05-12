class Solution:
    # O(n log(n))
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] ^ nums[1]

        return self.singleNonDuplicate(nums[0:len(nums) // 2]) ^ self.singleNonDuplicate(nums[len(nums) // 2:])

    # odd ^ 1 = odd - 1
    # even ^ 1 = even + 1
    def singleNonDuplicate1(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == '__main__':
    soln = Solution()
    # nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    nums = [3, 3, 7, 7, 10, 11, 11]
    ans = soln.singleNonDuplicate(nums)
    print(ans)
