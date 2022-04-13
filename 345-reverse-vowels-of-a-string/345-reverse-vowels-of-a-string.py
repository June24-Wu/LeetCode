class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        
        li = []
        for i in s:
            if i.lower() in ["a","e","i","o","u","A","E","I","O","U"]:
                stack.append(i)
            li.append(i)
        
        for i in range(len(li)):
            if li[i].lower() in ["a","e","i","o","u"]:
                li[i] = stack.pop()
        return "".join(li)