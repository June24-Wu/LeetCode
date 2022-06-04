class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":return False
        
        heap = [0]
        dp = [ False for _ in range(len(s))]
        
        for index in range(minJump,len(s)):
            char = s[index]
            if char == "1":
                continue
            # index - maxJump <= i <= index - minJump
            while heap and heap[0] < index - maxJump:
                heap.pop(0)
            if heap == []:
                print(index)
                return False
            if heap[0] <= index - minJump:
                heap.append(index)
                dp[index] = True
        # print(dp)
        return dp[-1]
        
        