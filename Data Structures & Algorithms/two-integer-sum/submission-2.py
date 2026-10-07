class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            hashmap[diff] = i
        for j in range(len(nums)):
            if nums[j] in hashmap.keys():
                if j!= hashmap[nums[j]]:
                    return [j,hashmap.get(nums[j])]

            


