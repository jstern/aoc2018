class MarbleGame:
    def __init__(self, players: int, hi: int):
        self.players = players
        self.hi = hi
        self.circle = [[0]]
        self.scores = [0] * players
        self.turn = 1
        self.player = 0
        self.current = 0

    def size(self):
        return len(self.circle[0])

    def insert(self, i, val):
        self.circle[0].insert(i, val)

    def append(self, val):
        self.circle[0].append(val)

    def pop(self, i):
        return self.circle[0].pop(i)

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

        # player removes and pockets the marble 7 counterclockwise
        idx = (self.current - 7) % self.size()
        # pop is O(k)
        self.scores[self.player] = self.scores[self.player] + self.pop(idx)
        self.current = idx

    def play_normal(self):
        # player places marble between 1 clockwise and 2 clockwise of current
        c1 = (self.current + 1) % self.size()
        c2 = (c1 + 1) % self.size()
        if c2 <= c1:
            self.append(self.turn)
            self.current = c1 + 1
        else:
            self.insert(c2, self.turn)
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
