class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        numss = set(nums)
        ht = sorted(list(numss))

        leng = 1
        save = 1
        for k in range(1, len(ht)):
            if ht[k] - ht[k - 1] == 1:
                leng += 1
            else:
                if leng >= save:
                    save = leng
                    leng = 1
        if nums==[]:
            return 0
        if save > leng:
            return save
        return leng
 
