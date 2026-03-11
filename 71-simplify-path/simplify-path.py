class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)
        ans = []
        for i in path:
            if i == "" or i == ".":
                continue
            elif i == "..":
                ans.pop() if ans else None
            else:
                ans.append(i)
        return "/" + "/".join(ans)
        