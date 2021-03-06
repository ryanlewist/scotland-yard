import game as the_game
import mrx
import agent


class Controller:

    def run(self):
        game = the_game.Game()
        players = [mrx.MrXPlayer(), agent.AgentPlayer(), agent.AgentPlayer(), agent.AgentPlayer(), agent.AgentPlayer()]
        while True:
            for i, p in enumerate(players):
                route = p.play(game.gamestate(i))
                if route:
                    game.move(i, route['station'], route['ticket'])
            if game.is_over():
                break
