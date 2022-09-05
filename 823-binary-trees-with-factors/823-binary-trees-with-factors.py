class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0
        table = {}
        
        for i in range(len(arr)):
            left =  0 ; right = i - 1 ; temp = 1
            while left <= right:
                if arr[left] * arr[right] < arr[i]:
                    left += 1
                elif arr[left] * arr[right] > arr[i]:
                    right -= 1
                else:
                    if arr[left] == arr[right]:
                        temp += table[arr[left]] ** 2
                    else:
                        temp += table[arr[left]] * table[arr[right]] * 2
                    left += 1
            table[arr[i]] = temp
            ans += temp
        return ans % (10**9 + 7)
                        
        