class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        q = [[]]
        length = len(nums)
        for i in nums:
            for j in range(len(q)):
                q.append(q[j] + [i])
        
        l2 = []
        for i in q:
            i = str(i).replace("[","").replace("]","")
            l2.append(i)
        l2 = list(set(l2))
        l3 = []
        for i in l2:
            l3.append(i.split(","))
        return l3