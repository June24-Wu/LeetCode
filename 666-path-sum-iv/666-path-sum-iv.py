class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        table = {}
        nums.sort()
        nums = [(int(str(i)[0]),int(str(i)[1]),int(str(i)[2])) for i in nums]
        for item in nums:
            if item[0] not in table:
                table[item[0]] = {}
            table[item[0]][item[1]] = item[2]
        ans = 0
        print(table)
        def dfs(row,col,sumVal):
            nonlocal ans
            sumVal += table[row][col]
            # print(row,col,sumVal)
            if row + 1 in table and col * 2 - 1 in table[row+1]:
                dfs(row+1,col * 2 - 1,sumVal)
            if row + 1 in table and col * 2 in table[row+1]:
                dfs(row+1,col*2,sumVal)
            if row + 1 not in table or (col * 2 not in table[row+1] and col * 2 - 1 not in table[row+1]):
                # print(row,col,sumVal)
                ans += sumVal
            return
        dfs(1,1,0)
        return ans
            
        