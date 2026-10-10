class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            k = "".join(sorted(i))
            if dic.get(k):
                dic.get(k).append(i)
            else:
                dic[k] = [i]
        return list(dic.values())
        





                    
            

        

            




