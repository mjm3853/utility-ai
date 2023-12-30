class Agent:
    def __init__(self, actions):
        self.actions = actions

    def decide_and_execute(self, state):
        best_action = None
        highest_utility = float('-inf')

        for action in self.actions:
            utility = action.calculate_utility(state)
            if utility > highest_utility:
                highest_utility = utility
                best_action = action

        best_action.execute(state)