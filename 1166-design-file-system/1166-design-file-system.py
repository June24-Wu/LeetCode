class Tree:
    def __init__(self,val:str):
        self.children = collections.defaultdict(dict)
        self.val = val
class FileSystem:
    def __init__(self):
        self.tree = Tree(0)
        
    def createPath(self, path: str, value: int) -> bool:
        if path == "" or path == "/":
            return False
        path = path.split("/")[1:]
        curr = self.tree
        for idx , i in enumerate(path[:-1]):
            if i not in curr.children:
                return False
            curr = curr.children[i]
        if path[-1] in curr.children:
            return False
        else:
            curr.children[path[-1]] = Tree(value)
        return True

    def get(self, path: str) -> int:
        if path == "" or path == "/":
            return False
        path = path.split("/")[1:]
        curr = self.tree
        for i in path:
            if i not in curr.children:
                return - 1
            curr = curr.children[i]
        return curr.val
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)