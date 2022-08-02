class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxD = max(damage)
        if maxD >= armor:
            return sum(damage) + 1 - armor
        else:
            return sum(damage) + 1 - maxD
        