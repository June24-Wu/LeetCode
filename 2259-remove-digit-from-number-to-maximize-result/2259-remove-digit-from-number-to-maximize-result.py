class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number = list(number)
        maxNum = - float("inf")
        for i in range(len(number)):
            if number[i] == digit:
                subarray = number[:i] + number[i+1:]
                subarray = "".join(subarray)
                subarray = int(subarray)
                maxNum = max(maxNum,subarray)
        return str(maxNum)
        