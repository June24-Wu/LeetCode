class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0 ; index = 0 ;insert = 0
        
        while index < len(s):
            if s[index] == "(":
                left += 1
                index += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    insert += 1
                if index+1 >= len(s) or s[index+1] != ")":
                    index += 1
                    insert += 1
                else:
                    index += 2
        insert += left * 2
        return insert
                        
                
        