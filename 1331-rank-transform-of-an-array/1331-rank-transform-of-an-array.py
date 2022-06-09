class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        subArray = arr.copy() ; subArray.sort()
        table = {} ; rank = 1
        for val in subArray:
            if val not in table:
                table[val] = rank
                rank += 1
        for i in range(len(arr)):
            arr[i] = table[arr[i]]
        return arr
        