class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "None"
        enc = "₹".join(strs)
        return enc

    def decode(self, s: str) -> List[str]:
        if s=="None":
            return []
        dec = s.split("₹")
        return dec

        
