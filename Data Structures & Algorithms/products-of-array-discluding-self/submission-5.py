class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        calc = 1
        where = "x"
        flag = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                calc *= nums[i]
            else:
                where = i
                flag += 1

        if where == "x":
            h = [calc]*len(nums)
        else:
            h = [0]*len(nums)
            h[where] = calc
        
        for j in range(len(nums)):
            if nums[j] != 0:
                h[j] //= nums[j]

            else:
                pass
        if flag>1:
            return [0]*len(nums)

        return h
            

