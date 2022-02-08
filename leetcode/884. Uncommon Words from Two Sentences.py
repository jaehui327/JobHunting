from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        result = []
        counter = Counter(s1.split() + s2.split())
        for key in counter:
            if counter[key] == 1:
                result.append(key)
        return result
        # list = s1.split() + s2.split()
        # dict = {}
        # result = []
        # for word in list:
        #     if dict.get(word):
        #         dict[word] += 1
        #     else:
        #         dict[word] = 1
        # for key, value in dict.items():
        #     if value == 1:
        #         result.append(key)
        # return result

sol = Solution()
print(sol.uncommonFromSentences("this apple is sweet", "this apple is sour"))