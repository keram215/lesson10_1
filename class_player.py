class Player:
    name = None
    answers = None

    def __init__(self, name):
        self.name = name
        self.answers = []

    def is_answer(self, word):
        if word not in self.answers:
            return True
        else:
            return False

    def add(self, word):
        self.answers.append(word)

    def point(self):
        point = 0
        for answer in self.answers:
            point += len(answer)
        return point
