class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0 ; r = len(people) - 1
        ans = 0 ; origin = limit
        while l <= r:
            ans += 1
            if people[r] + people[l] <= limit:
                l += 1
            r -= 1
        return ans