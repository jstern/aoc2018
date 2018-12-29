class MarbleGame:
    def __init__(self, players: int, hi: int):
        self.players = players
        self.hi = hi
        self.circle = [0]
        self.scores = [0] * players
        self.turn = 1
        self.player = 0
        self.current = 0

    def play_turn(self):
        if self.turn % 23 == 0:
            self.play_23()
        else:
            self.play_normal()
        self.turn = self.turn + 1
        self.player = (self.player + 1) % self.players

    def play_23(self):
        # player pockets the marble
        self.scores[self.player] = self.scores[self.player] + self.turn
        idx = (self.current - 7) % len(self.circle)
        self.scores[self.player] = self.scores[self.player] + self.circle.pop(idx)
        self.current = idx

    def play_normal(self):
        # player places marble between 1 clockwise and 2 clockwise of current
        c1 = (self.current + 1) % len(self.circle)
        c2 = (c1 + 1) % len(self.circle)
        if c2 <= c1:
            self.circle.append(self.turn)
            self.current = c1 + 1
        else:
            self.circle.insert(c2, self.turn)
            self.current = c2

    def play(self):
        while self.turn <= self.hi:
            self.play_turn()

    @property
    def state(self):
        marbles = [str(m) for m in self.circle]
        marbles[self.current] = f"({marbles[self.current]})"
        return f"[{self.player}]  {' '.join(marbles)}"

    @property
    def current_marble(self):
        return self.circle[self.current]

    @property
    def winner(self):
        top = None
        for i in range(self.players):
            player = i + 1
            score = self.scores[i]
            if top is None or top[1] < score:
                top = (player, score)
        return top
