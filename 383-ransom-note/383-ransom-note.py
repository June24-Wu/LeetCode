class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {char : magazine.count(char) for char in set(magazine)}
        for i in set(ransomNote):
            if i not in table or ransomNote.count(i) > table[i]:
                return False
        return True
        