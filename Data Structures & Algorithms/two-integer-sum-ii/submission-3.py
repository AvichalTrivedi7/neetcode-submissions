class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for ind,val in enumerate(numbers):
            if dic.get(val):
                dic[val].append(ind)
            else:
                dic[val] = [ind]
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if (diff in dic) and i!=dic[diff][0]:
                return [i+1, dic[diff][0]+1]
            elif (diff in dic) and i!=dic[diff][1]:
                return [i+1, dic[diff][1]+1]
