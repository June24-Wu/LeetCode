class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def get(num):
            return a * num ** 2 + b * num + c
        if a == 0:
            return [get(i) for i in nums] if b > 0 else [get(i) for i in nums][::-1]
        mid = - b / (2 * a)
        right = bisect.bisect_left(nums,mid)
        left = right - 1
        ans = []

        while left >= 0 or right < len(nums):
            if left < 0:
                ans.append(get(nums[right]))
                right += 1
                continue
            if right >= len(nums):
                ans.append(get(nums[left]))
                left -= 1
                continue
            leftval =  abs(nums[left] - mid)    ; rightval = abs(nums[right] - mid)
            if leftval < rightval:
                ans.append(get(nums[left]))
                left -= 1
            else:
                ans.append(get(nums[right]))
                right += 1
        return ans if a >= 0 else ans[::-1]
                
        