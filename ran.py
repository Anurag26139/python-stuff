class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=sorted(list(ransomNote))
        m=sorted(list(magazine))
        for char in m:
            if r and char==r[0]:
                r.pop(0)
        if r:
            return False
        else:
            return True