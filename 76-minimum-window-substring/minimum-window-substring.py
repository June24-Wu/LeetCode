class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        m = collections.defaultdict(int)
        def is_valid(m):
            for k, v in t.items():
                if m[k] < v:
                    return False
            return True
        left = 0; n = len(s); ans = ""; minv = float("inf")
        for right in range(n):
            m[s[right]] += 1
            while is_valid(m):
                if right - left + 1 < minv:
                    minv = right - left + 1
                    ans = s[left:right+1]
                # print(left,right)
                m[s[left]] -= 1
                left += 1
        return ans if minv != float("inf") else ""
                

        