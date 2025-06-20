from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if (length <= 1):
            return length
        left = 0
        for i in range(1, length):
            if (nums[left] == nums[i]):
                continue
            nums[left + 1] = nums[i]
            left += 1
        return left + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))