class Project:
    def __init__(self, name, cost, effect):
        self.name = name
        self.cost = cost
        self.effect = effect

    def play(self, player, board):
        if player.credits >= self.cost:
            player.credits -= self.cost
            self.effect(player, board)
        else:
            print(f"{player.name} nie stać na {self.name}!")

