class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        output=False
        
        for i in ransomNote:
            if i in magazine:
                output=True
                magazine=magazine.replace(i,"",1)
            else:
                return False
        
       
        return output