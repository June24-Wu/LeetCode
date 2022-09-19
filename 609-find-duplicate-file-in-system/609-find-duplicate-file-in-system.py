class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        table = collections.defaultdict(list)
        
        for path in paths:
            path = path.split(" ")
            root_path = path[0]
            for file in path[1:]:
                file = file.split("(")
                name = root_path + "/" + file[0]
                table[file[1][:-1]].append(name)
        ans = []
        for i in table:
            if len(table[i])  > 1:
                ans.append(table[i])
        return ans
        