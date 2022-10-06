import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # so all players get their next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # checking for a correct value by casting to an int
            # if it isn't correct \ isn't available = print invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # this is when the if statement fails
            except ValueError:
                print("Invalid square. Try again.")

        return val
