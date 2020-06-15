from typing import List


class Solution:
    def is_sequence(self, word, S):
        index = 0
        for i in range(len(word)):
            res = S.find(word[i], index)
            if -1 == res:
                return False
            else:
                index = res + 1
        return True

    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count = 0
        for w in words:
            if self.is_sequence(w, S):
                count += 1
        return count


S = "abcde"
words = ["a", "bb", "acd", "ace"]
obj = Solution()
res = obj.numMatchingSubseq(S, words)
print(res)
