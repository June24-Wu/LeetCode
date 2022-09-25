class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        origin = nums.copy()
        front = True
        back = True
        cnt = 0
        for idx , item in enumerate(nums):
            if front == False:
                break
            if idx == 0 or nums[idx] >= nums[idx-1]:
                continue
            if cnt == 1:
                front = False
                continue
            nums[idx] = nums[idx-1]
            cnt += 1
        cnt = 0
        nums = origin
        for idx in range(len(nums)-2,-1,-1):
            if back == False:
                break
            if nums[idx] <= nums[idx+1]:
                continue
            if cnt == 1:
                print(idx)
                back = False
                continue
            nums[idx] = nums[idx+1]
            cnt += 1
        print(front,back)
        return front or back
        