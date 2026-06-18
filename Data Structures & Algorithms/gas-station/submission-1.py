class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        left = [a-b for a,b in zip(gas, cost)]

        if sum(left) < 0:
            return -1

        total = 0
        start = 0

        for i in range(len(left)):
            total += left[i]
            if total < 0:
                total = 0
                start = i+1
            
        return start


