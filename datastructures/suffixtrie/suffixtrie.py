from ._trie import Trie


class SuffixTrie(Trie):

    def __init__(self):
        self.ngram_counter = dict()
        super().__init__()

    def insert(self, word):
        for i, v in enumerate(word):
            ngram = word[i:]
            if ngram in self.ngram_counter:
                self.ngram_counter[word[i:]] += 1
            else:
                self.ngram_counter[ngram] = 1
            super().insert(word[i:])

    def delete(self, word):
        for i, v in enumerate(word):
            ngram = word[i:]
            if ngram in self.ngram_counter:
                self.ngram_counter[word[i:]] -= 1
                if self.ngram_counter[word[i:]] == 0:
                    super().delete(word[i:])
