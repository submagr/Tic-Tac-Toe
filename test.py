from agent import Agent, HumanAgent, BotAgent
from game import BoardGame, Board

if __name__ == "__main__":
    t = int(raw_input("Enter number of test cases: "))
    for i in range(t):
        print("Test Case #"+ str(i))
        p1 = HumanAgent("zero", "O")
        p2 = HumanAgent("cross", "X")
        myGame = BoardGame(p1, p2)
        myGame.game_play()
