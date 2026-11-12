class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = {}
        res = set()
        for i,v in enumerate(nums):
            hm[v] = i

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ele =  -(nums[i]+nums[j]) 
                if hm.get(ele) and (hm.get(ele)!=i and hm.get(ele)!=j):
                    k = hm[ele]
                    if nums[i]<=nums[j]<=nums[k]:
                        res.add((nums[i],nums[j],nums[k]))
                    elif nums[i]<=nums[k]<=nums[j]:
                        res.add((nums[i],nums[k],nums[j]))
                    elif nums[k]<=nums[j]<=nums[i]:
                        res.add((nums[k],nums[j],nums[i]))
                    elif nums[j]<=nums[k]<=nums[i]:
                        res.add((nums[j],nums[k],nums[i]))    
                    elif nums[j]<=nums[i]<=nums[k]:
                        res.add((nums[j],nums[i],nums[k]))
                    elif nums[k]<=nums[i]<=nums[j]:
                        res.add((nums[k],nums[i],nums[j]))
        return [list(i) for i in res]

         