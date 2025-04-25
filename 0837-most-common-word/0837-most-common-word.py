import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # convert to lowercase
        lower = paragraph.lower()
        # separate in words
        words = re.findall(r'\w+', lower)
        # filter out banned words
        words_filtered = [word for word in words if word not in banned]
        # count word occurences
        word_count = collections.Counter(words_filtered)
        # return max occurence word
        return max(word_count, key = word_count.get)