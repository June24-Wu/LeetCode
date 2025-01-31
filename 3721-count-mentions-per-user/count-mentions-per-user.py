class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        events = [[0 if i[0] == "OFFLINE"  else 1,int(i[1]),i[2]] for i in events]
        events.sort(key = lambda x : (x[1],x[0]))
        def decode(users):
            if users.isdigit():
                return [int(users)]
            else:
                users = users.split()
                rt = []
                for u in users:
                    u = int(u.replace("id",""))
                    rt.append(u)
                return rt
        status = [0 for _ in range(n)]
        ans = [0 for _ in range(n)]
        for event , ts , users in events:
            ts = int(ts)
            if event == 0:
                for user in decode(users):
                    status[user] = int(ts) + 60
            if event == 1:
                if users == "ALL":
                    ans = [k+1 for k in ans]
                elif users == "HERE":
                    for k in range(n):
                        # print(k,status[k],ts)
                        if status[k] <= ts:
                            ans[k] += 1
                else:
                    for k in decode(users):
                        ans[k] += 1
            print(ans,status)
        return ans

        