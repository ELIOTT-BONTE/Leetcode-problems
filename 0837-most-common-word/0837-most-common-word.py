import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # convert to lowercase
        words = paragraph.lower()
        # separate in words
        words = re.findall(r'\w+', words)
        # filter out banned words
        words = [word for word in words if word not in banned]
        # count word occurences
        words = collections.Counter(words)
        # return max occurence word
        return max(words, key = words.get)