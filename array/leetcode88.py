from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 使用过滤器
        index = m + n - 1
        while (n - 1 >= 0) & (m - 1 >= 0):
            if nums1[m - 1] > nums2[n - 1]:
                nums1[index] = nums1[m - 1]
                m -= 1
            else :
                nums1[index] = nums2[n - 1]
                n -= 1
            index -= 1
        if m > 0:
            while m > 0:
                nums1[index] = nums1[m - 1]
                m -= 1
                index -= 1
        elif n > 0:
            while n > 0:
                nums1[index] = nums2[n - 1]
                n -= 1
                index -= 1

if __name__ == '__main__':
    nums1 = [2, 0]
    nums2 = [1]
    instance = Solution()
    instance.merge(nums1, 1, nums2, 1)
    print(nums1)