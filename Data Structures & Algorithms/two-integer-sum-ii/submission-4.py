class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(numbers)):
            diff = target - numbers[i]
            hashmap[diff] = i
        for j in range(len(numbers)):
            if numbers[j] in hashmap.keys():
                if j!= hashmap[numbers[j]]:
                    return [j+1,hashmap.get(numbers[j])+1]