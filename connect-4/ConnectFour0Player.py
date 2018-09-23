import ConnectFourRandomAI
import ConnectFourMinimaxAI
import ConnectFourMostlyRandomAI
import ConnectFourEngine
import ConnectFourBoard
import ConnectFourAlphaBetaAI

if __name__ == '__main__':
    # Initialise the game engine
    # Modify these parameters to tweak the game
    app = ConnectFourEngine.ConnectFour(
            ai_delay = 8,
            blue_player = ConnectFourAlphaBetaAI.AIcheck,
            red_player = ConnectFourMinimaxAI.AIcheck,
            )
    # start the game engine
    app.game_loop()
