class Word:
    word = None
    subwords = None

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def check_word(self, word):
        if word in self.subwords:
            return True
        else:
            return False