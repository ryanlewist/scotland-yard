import random
import board
import figure
import logger


# The class Game fully describes Scotland Yard:
# The board, Mr. X and the agents.
# There are higher-level methods that change the state of the game.


class Game:

    # Initialization creates a board and the figures
    # Then the figures are put on random starting positions
    def __init__(self):
        print("Starting game")
        print("Loading board...")
        self.board = board.Board()
        all_starts = [13, 26, 29, 34, 50, 53, 91, 94, 103, 112, 117, 132, 138, 141, 155, 174, 197, 198]
        start = random.sample(all_starts, 5)
        self.figures = []
        for i in range(0, 5):
            self.figures.append(figure.Figure(i, start[i]))
        self.turns = 0
        self.mrx_last_used_ticket = None
        self.logger = logger.Logger()
        self.logger.log("## SCOTLAND YARD: MR. X VS. 4 AGENTS")

    def log(self, msg):
        self.logger.log(msg)

    # Is the game over?
    # There are two possibilities:
    # - Mr. X and an agent are at the same station (=> The agents win)
    # - 20 turns have passed (=> Mr. X has won)
    def is_over(self):
        for i in range(1, 5):
            if self.figures[0].position == self.figures[i].position:
                self.logger.log("**GAME OVER:** Mr. X was caught - The agents win.")
                self.logger.save()
                print("Game Over: The agents win")
                return True
        if self.turns > 19:
            self.logger.log("**GAME OVER:** 20 turns have passed - Mr. X wins.")
            self.logger.save()
            print("Game Over: Mr. X wins")
            return True
        return False

    # Returns the position of Mr. X at the 3, 8, 13, and 18 turns.
    def position_of_mrx(self):
        if self.turns % 5 == 3:
            return self.figures[0].position
        else:
            return 0

    # Returns an array of the positions of the agents.
    def positions_of_agents(self):
        positions = []
        for f in self.figures:
            positions.append(f.position)
        positions.pop(0)  # Remove Mr. X's position
        return positions

    def tickets(self):
        tickets = []
        for f in self.figures:
            tickets.append(f.tickets)
        return tickets

    def possible_routes_for(self, figure):
        routes = self.board.routes_from(figure.position)
        routes[:] = [r for r in routes if figure.tickets[r['ticket']] != 0]
        # TODO: Not sure how the following piece works. I think it means that you can't move
        #  to the same space as another agent, but I'm not sure why it only applies to the agents
        #  and not Mr. X,  who also can't move into the same space as an agent. Maybe it's because agents
        #  move to the same space as Mr. X, but Mr. X would never try to move to a space with an agent because
        #  he tries to maximize the distance between them. Per the rules, if he is cornered, the game
        #  should end and the agents win. That condition should be added to the is_over class.
        if figure.id > 0:
            routes[:] = [r for r in routes if r['station'] not in self.positions_of_agents()]
        return routes

    # Moves the figure with figure_id to [station] by [ticket].
    def move(self, figure_id, station, ticket):
        figure = self.figures[figure_id]
        routes = self.possible_routes_for(figure)
        if {'station': station, 'ticket': ticket} in routes or ticket == 'black':
            if figure.id == 0:
                self.turns += 1
                self.logger.log("\n### TURN {0}:".format(self.turns))
                self.mrx_last_used_ticket = ticket
                figure_name = 'Mr. X'
            else:
                figure_name = 'Agent {0}'.format(figure.id)
            self.logger.log("**{figure_name}** moves from *{figure_position}* to *{station}* by *{ticket}*\n".format(
                figure_name=figure_name, figure_position=figure.position, station=station, ticket=ticket))
            figure.tickets[ticket] -= 1
            figure.position = station
            return True
        return False

    # Describes the current gamestate
    def gamestate(self, figure_id):
        state = {
            'figure_id': figure_id,
            'routes': self.possible_routes_for(self.figures[figure_id]),
            'board': self.board,
            'position_of_mrx': self.position_of_mrx(),
            'positions_of_agents': self.positions_of_agents(),
            'turns': self.turns,
            'tickets': self.tickets(),
            'mrx_last_used_ticket': self.mrx_last_used_ticket
        }
        return state
