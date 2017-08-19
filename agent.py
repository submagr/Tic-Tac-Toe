class Agent(object):
    '''
    '''
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class HumanAgent(Agent):
    '''
    '''
    def __init__(self, name, symbol):
        super(HumanAgent, self).__init__(name, symbol)

    def play(self):
        temp = [int(x) for x in raw_input("\t" + self.name + "'s turn. Please enter a move:").split(" ")]
        print(temp)
        return temp[0], temp[1]

class BotAgent(Agent):
    '''
    '''
