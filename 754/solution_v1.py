class Solution:

    def reachNumber(self, target:int) -> int:
        target = abs(target)
        sum = 0
        step = 0
        while sum < target:
            step +=1
            sum += step
        while (sum-target)%2 != 0:
            step +=1
            sum += step
        return step
