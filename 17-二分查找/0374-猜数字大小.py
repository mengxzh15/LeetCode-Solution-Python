# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass


class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n
        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            if guess(mid) == 1:
                left = mid + 1
            else:
                right = mid
        # 最后剩下的数一定是所求，无需后处理
        return left
