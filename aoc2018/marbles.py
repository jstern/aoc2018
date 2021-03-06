from collections import deque


class MarbleGame:
    def __init__(self, players: int, hi: int):
        self.players = players
        self.hi = hi
        self.circle = deque([0])
        self.scores = [0] * players
        self.turn = 1
        self.player = 0

    def play_turn(self):
        # invariant: current marble is always at the end of the deque
        if self.turn % 23 == 0:
            self.play_23()
        else:
            self.play_normal()
        self.turn = self.turn + 1
        self.player = (self.player + 1) % self.players

    def play_normal(self):
        # player places marble between 1 clockwise and 2 clockwise of current
        self.circle.rotate(-1)
        self.circle.append(self.turn)

    def play_23(self):
        # player pockets the marble
        self.scores[self.player] = self.scores[self.player] + self.turn
        self.circle.rotate(7)
        self.scores[self.player] = self.scores[self.player] + self.circle.pop()
        self.circle.rotate(-1)

    def play(self):
        while self.turn <= self.hi:
            self.play_turn()

    @property
    def winner(self):
        top = None
        for i in range(self.players):
            player = i + 1
            score = self.scores[i]
            if top is None or top[1] < score:
                top = (player, score)
        return top
