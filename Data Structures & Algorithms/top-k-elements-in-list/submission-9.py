class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        
        buclist = [[] for i in range(len(nums)+1)]

        for val,freq in dic.items():
            buclist[freq].append(val)

        res = []
        for j in range(len(buclist)-1, 0, -1):
            for l in buclist[j]:
                res.append(l)
            if len(res) == k:
                return res


