class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            tup = [0]*26
            for j in i:
                tup[ord(j)-ord('a')]+=1
            if dic.get(tuple(tup)):
                dic[tuple(tup)].append(i)
            else:
                dic[tuple(tup)] = [i]
        return list(dic.values())