class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        t = nums1[0] % 2
        odd_cnt = 0
        even_cnt = 0
        for i in nums1:
            if i % 2 == t:
                pass
            else:
                if t == 0 and odd_cnt == 0:
                    return False
                if t == 1 and odd_cnt == 0:
                    return False
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return True


        