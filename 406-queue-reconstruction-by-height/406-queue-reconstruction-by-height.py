class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : ( - x[0], x[1]))
        
        arr = []
        
        for index , (height , idx) in enumerate(people):
            arr.insert(idx,people[index])
        return arr
        