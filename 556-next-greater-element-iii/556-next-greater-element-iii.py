class Solution:
    def nextGreaterElement(self, n: int) -> int:
        origin = n ;
        n = [int(i) for i in list(str(n))]
        if len(n) == 1:
            return -1
        for left in range(len(n) -2,-1,-1):
            if n[left] < n[left + 1]:
                break
        flag = False
        for right in range(left+1,len(n)-1):
            if n[right] > n[left] and n[right + 1] <= n[left]:
                flag = True
                break
        if flag == False:
            right = len(n) - 1
        n[left] , n[right] = n[right] , n[left]
        subarray = n[left+1:]
        subarray.sort()
        n[left+1:] = subarray
        num = int("".join([str(i) for i in n]))
        return num if num > origin and num <= 2147483647 else -1
        