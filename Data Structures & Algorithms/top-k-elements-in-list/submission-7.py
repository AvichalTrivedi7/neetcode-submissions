class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashp = [0]*2001

        out = []
        for i in nums:
            if i>=0:
                hashp[i] += 1
            else:
                hashp[i] += 1

        for i in range(k):
            j = max(hashp)
            if hashp.index(j) <= 1000:
                out.append(hashp.index(j))
                hashp[hashp.index(j)]=0
            else:
                m = hashp.index(j) - len(hashp) 
                out.append(m) 
                hashp[hashp.index(j)]=0
        
        return out
