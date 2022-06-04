class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0
    def add(self,web,count):
        curr = self
        web = web.split(".")
        for i in range(len(web) - 1,-1,-1):
            if web[i] not in curr.children:
                curr.children[web[i]] = Trie()
            curr = curr.children[web[i]]
            curr.count += count
        

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        trie = Trie()
        
        for item in cpdomains:
            count , web = item.split(" ") ; count = int(count)
            trie.add(web,count)
        ans = []
        def dfs(node,path):
            nonlocal ans
            ans.append(" ".join([str(node.count),path]))
            for i in node.children:
                dfs(node.children[i], i + "." + path)
        for i in trie.children:
            dfs(trie.children[i],i)

        # print(ans)
        return ans
        