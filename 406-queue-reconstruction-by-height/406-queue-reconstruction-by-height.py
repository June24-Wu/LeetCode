class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        
        new = []
        
        for i in people:
            new.insert(i[1],i)
        
        return new