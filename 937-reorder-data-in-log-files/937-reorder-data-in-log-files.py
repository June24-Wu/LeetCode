class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
                continue
            log = log.split(" ")
            ide = log[0]
            content = "A".join(log[1:])
            log = " ".join(log)
            letter_logs.append((content,ide,log))
        letter_logs.sort()
        ans = []
        for i , j , k in letter_logs:
            ans.append(k)
        return ans + digit_logs
        