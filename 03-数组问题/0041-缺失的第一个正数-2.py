# 41. 缺失的第一个正数
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1
        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1] = nums[index1] ^ nums[index2]
        nums[index2] = nums[index1] ^ nums[index2]
        nums[index1] = nums[index1] ^ nums[index2]


if __name__ == '__main__':
    nums = [4, 4, 4, 3, 2, 31, -1, 2]

    solution = Solution()
    res = solution.firstMissingPositive(nums)
    print(res)
