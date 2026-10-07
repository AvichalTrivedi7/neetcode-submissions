class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = nums.copy()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums1:
                for j in range(len(nums1)):
                    if nums1[j]==diff and j != i:
                        return [i,j]

            