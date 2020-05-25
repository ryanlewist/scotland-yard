import random


class AgentPlayer:

    possible_positions_mrx = []

    # play gets called by the controller once per turn
    def play(self, gamestate):
        if gamestate['figure_id'] == 1:
            self.calculate_possible_positions_mrx(gamestate['position_of_mrx'], gamestate['mrx_last_used_ticket'],
                                                  gamestate['board'])
        return self.play_greedy(gamestate['routes'], gamestate['board'])

    # Play to a random station
    def play_random(self, routes):
        return random.sample(routes, 1)[0]

    def play_greedy(self, routes, board):
        if not routes:
            return None
        if not AgentPlayer.possible_positions_mrx:
            return self.play_random(routes)
        min_average_distance_to_mrx = 10
        route_to_go_to = 0
        for index, route in enumerate(routes):
            my_position = route['station']
            sum_of_distances_to_mrx = 0
            for position_of_mrx in AgentPlayer.possible_positions_mrx:
                current_distance_to_mrx = board.distance(my_position, position_of_mrx)
                sum_of_distances_to_mrx += current_distance_to_mrx
            current_avgerage_distance_to_mrx = sum_of_distances_to_mrx / len(AgentPlayer.possible_positions_mrx)
            if current_avgerage_distance_to_mrx < min_average_distance_to_mrx:
                min_average_distance_to_mrx = current_avgerage_distance_to_mrx
                route_to_go_to = index
        return routes[route_to_go_to]

    def calculate_possible_positions_mrx(self, position_of_mrx, mrx_last_used_ticket, board):
        if position_of_mrx == 0:
            if AgentPlayer.possible_positions_mrx:
                new_positions = []
                for p in AgentPlayer.possible_positions_mrx:
                    for q in board.routes_from(p):
                        if q['ticket'] == mrx_last_used_ticket and not q['station'] in new_positions:
                            new_positions.append(q['station'])
                new_positions.sort()
                AgentPlayer.possible_positions_mrx = new_positions
        else:
            AgentPlayer.possible_positions_mrx = [position_of_mrx]
