class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        q = []
        for i in hand:
            while q and q[0][1] == groupSize:
                q.pop(0)
            if q and q[0][0] + 1 == i:
                _ , num = q.pop(0)
                q.append((i,num+1))
            else:
                q.append((i,1))
            # print(q)
        while q and q[0][1] == groupSize:
            q.pop(0)
        return q == []
        