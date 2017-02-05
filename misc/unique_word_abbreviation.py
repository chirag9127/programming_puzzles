"""
An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:
"""


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.abbrev_set = {}
        self.words = set()
        for word in dictionary:
            abbr = self.get_abbr(word)
            if word in self.words:
                continue
            if abbr not in self.abbrev_set:
                self.abbrev_set[abbr] = 0
            self.abbrev_set[abbr] += 1
            self.words.add(word)

    def get_abbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word[1:-1])) + word[-1]

    def isUnique(self, word):
        num_words = self.abbrev_set.get(self.get_abbr(word))
        if not num_words:
            return True
        if num_words == 1 and word in self.words:
            return True
        return False


def test_unique_word_abbrev():
    obj = ValidWordAbbr(["deer", "door", "cake", "card"])

    assert obj.isUnique("dear") is False
    assert obj.isUnique("cart") is True
    assert obj.isUnique("cane") is False
    assert obj.isUnique("make") is True

    obj = ValidWordAbbr(["hello"])

    assert obj.isUnique("hello") is True
