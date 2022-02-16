from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        temp = []
        s = ""
        for (i, n) in enumerate(nums):
            if i == 0:
                temp = [n, n]
            elif n == temp[1] + 1:
                temp.pop()
                temp.append(n)
            else:
                result.append(temp)
                temp = [n, n]
        if temp:
            result.append(temp)
        return self.makeString(result)

    def makeString(self, nums: List[List[int]]) -> List[str]:
        result = []
        for num in nums:
            s = str(num[0])
            if num[0] != num[1]:
                s += "->" + str(num[1])
            result.append(s)
        return result


sol = Solution()
# print(sol.summaryRanges([1,2,3,7,8,9]))
# print(sol.summaryRanges([0,2,3,4,6,8,9]))
print(sol.summaryRanges([]))