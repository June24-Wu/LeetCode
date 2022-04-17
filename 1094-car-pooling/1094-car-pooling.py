class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = 0
        for i in trips:
            length = max(length,i[2])
        diff = [0 for i in range(length+1)]
        
        for i in trips:
            diff[i[1]] += i[0]
            diff[i[2]] -= i[0]
        pre = 0
        print(diff)
        for i in diff:
            pre += i
            if pre > capacity:
                return False
        return True
        