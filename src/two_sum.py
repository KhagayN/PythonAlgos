from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            complement = target - i
            for j in nums[nums.index(i) + 1:]:
                if j == complement:
                    return [nums.index(i), nums.index(j, nums.index(i) + 1 )]