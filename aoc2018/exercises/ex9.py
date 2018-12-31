from .. import marbles


if __name__ == "__main__":
    game = marbles.MarbleGame(players=452, hi=71250)
    game.play()
    print(game.winner)

    game = marbles.MarbleGame(players=452, hi=7_125_000)
    game.play()
    print(game.winner)
