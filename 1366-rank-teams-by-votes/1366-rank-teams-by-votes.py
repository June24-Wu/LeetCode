class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        table = {}
        for vote in votes:
            for i in range(len(vote)):
                if vote[i] not in table:
                    table[vote[i]] = [0 for _  in range(len(vote))]
                table[vote[i]][i] += 1
        
        res = { tuple(table[i] +[-ord(i)]): i for i in table}
        keys = list(res.keys())
        keys.sort(reverse = True)

        return "".join([res[i] for i in keys])
        