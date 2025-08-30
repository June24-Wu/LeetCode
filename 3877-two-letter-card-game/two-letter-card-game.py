class Solution:
    def score(self, cards: List[str], x: str) -> int:
        
        x0_d, x1_d = {}, {}   # track frequency of card types with x at position 0 or 1
        x0, x1, jok = 0, 0, 0 # counters for totals

        # classify cards
        for c in cards:
            if x in c:
                if c[0] == x and c[1] == x:   # joker (both positions)
                    jok += 1
                elif c[1] == x:               # x at position 1
                    x1_d[c] = x1_d.get(c, 0) + 1
                    x1 += 1
                elif c[0] == x:               # x at position 0
                    x0_d[c] = x0_d.get(c, 0) + 1
                    x0 += 1

        # sort frequency distributions
        x0_d = sorted(x0_d.values(), reverse=True)
        x1_d = sorted(x1_d.values(), reverse=True)

        # take the largest group from each side
        if x0_d: maxx0 = x0_d[0]
        else: maxx0 = 0
            
        if x1_d: maxx1 = x1_d[0]
        else: maxx1 = 0

        # fix odd counts using jokers
        if x0 % 2 == 1 and jok:
            x0 += 1
            jok -= 1
        if x1 % 2 == 1 and jok:
            x1 += 1
            jok -= 1

        # compute remainders after max group
        rem0 = x0 - maxx0
        rem1 = x1 - maxx1

        tot = 0  # total pairs

        # pair remainders against max group for x0
        if rem0 >= maxx0:
            tot += x0 // 2
            maxx0 = 0
        else: 
            tot += rem0
            maxx0 -= rem0

        # pair remainders against max group for x1
        if rem1 >= maxx1:
            tot += x1 // 2
            maxx1 = 0
        else: 
            tot += rem1
            maxx1 -= rem1

        # use jokers to help with leftover max groups
        if maxx0 and jok:
            x = min(maxx0, jok)
            tot += x
            jok -= x

        if maxx1 and jok:
            x = min(maxx1, jok)
            tot += x
            jok -= x

        # try using remaining jokers with leftover remainders
        if jok > 1 and rem0:
            x = min(jok, rem0)
            x //= 2
            tot += x
            jok -= x * 2

        if jok > 1 and rem1:
            x = min(jok, rem1)
            x //= 2
            tot += x
            jok -= x * 2
            
        return tot