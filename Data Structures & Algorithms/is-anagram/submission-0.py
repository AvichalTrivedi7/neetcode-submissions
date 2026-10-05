class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        for i in s:
            if dict1.get(i) == None:
                dict1[i] = 1
            else:
                dict1[i] = int(dict1.get(i)) + 1
        for j in t:
            if dict2.get(j) == None:
                dict2[j] = 1
            else:
                dict2[j] = int(dict2.get(j)) + 1
        return dict1==dict2