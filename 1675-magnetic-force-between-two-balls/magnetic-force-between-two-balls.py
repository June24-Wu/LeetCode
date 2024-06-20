class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        right = position[-1] - position[0]
        left = 1
        n = len(position)

        def isValid(force):
            ball = 1
            curr = position[0]
            for i in range(1,n):
                if position[i] - curr >= force:
                    ball += 1
                    curr = position[i]
            return ball >= m
        # for _ in range(10):
        #     print(left,right)
        while left < right:
            # print(left,right)
            mid = (left + right) // 2
            if isValid(mid):
                left = mid + 1
            else:
                right = mid
        return left if isValid(left) else left - 1 
        