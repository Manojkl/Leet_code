class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = 1
        while True:
            u = nums[m-1]
            for it, k in enumerate(nums[m:]):
                if k+u == target:
                    return [m-1,it+m]
            m+=1
