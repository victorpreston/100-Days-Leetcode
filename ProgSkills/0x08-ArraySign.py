#!/usr/bin/python3

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ArraySign = 1

        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                ArraySign = -ArraySign
        return ArraySign
