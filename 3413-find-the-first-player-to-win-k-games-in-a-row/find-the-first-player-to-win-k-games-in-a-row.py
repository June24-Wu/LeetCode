class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        nums = [0 for _ in range(n)]
        q = []
        for idx , i in enumerate(skills):
            while q and i >= q[-1][0]:
                v , pre = q.pop()
                nums[pre] = idx - pre - 1
            q.append([i,idx])
        length = len(q)
        while q:
            v , pre = q.pop()
            nums[pre] = length - len(q) - 1
        # print(nums)
        # return 0
        currMax = None
        currIdx = None
        for idx , i in enumerate(skills):
            if idx == 0:
                if nums[idx] >= k:
                    return idx
                else:
                    currMax = i ; currIdx = idx
                continue
            if i > currMax:
                if nums[idx] + 1 >= k:
                    return idx
                else:
                    currMax = i
                    currIdx = idx
        return currIdx
        