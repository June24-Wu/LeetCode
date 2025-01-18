class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_char = chars[0]
        curr_num = 0
        ans = []
        for i in chars:
            if i != curr_char:
                ans.append(curr_char)
                if curr_num > 1:
                    ans.append(str(curr_num))
                curr_char = i
                curr_num = 1
            else:
                curr_num += 1
        ans.append(curr_char)
        if curr_num > 1:
            ans.append(str(curr_num))
        ans = "".join(ans)
        chars[:len(ans)] = ans
        return len(ans)
        # return len())
