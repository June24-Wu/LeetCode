class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        li = [i+1 for i in range(n)]
        count = 1
        while len(li) > 1:
            node = li.pop(0)
            if count % k != 0:
                li.append(node)
            count += 1
            # print(li)
        return li[0]
        