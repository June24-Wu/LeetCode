class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = customers[0][0]
        wt = 0 ; n = len(customers)
        for i in range(n):
            if customers[i][0] >= curr_time:
                curr_time = customers[i][0] + customers[i][1]
                wt += customers[i][1]
            else:
                newtime = curr_time + customers[i][1]
                wt += newtime - customers[i][0]
                curr_time = newtime
            # print(curr_time,wt)
        return wt / n

        