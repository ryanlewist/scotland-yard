import random

class MrXPlayer:

    # play gets called by the controller once per turn
    def play(self, gamestate):
        return self.play_greedy(gamestate['routes'], gamestate['positions_of_agents'], gamestate['board'])

    # Play to a random station
    def play_random(self, routes):
        return random.sample(routes,1)[0]

    # Play to the station with the maximal average distance to all agents using a greedy algorithm
    def play_greedy(self, routes, positions_of_agents, board):
        max_average_distance_to_agents = 0
        route_to_go_to = 0
        for index, route in enumerate(routes):
            my_position = route['station']
            sum_of_distances_to_agents = 0
            for position_of_agent in positions_of_agents:
                current_distance_to_agent = board.distance(my_position, position_of_agent)
                sum_of_distances_to_agents += current_distance_to_agent
            current_average_distance_to_agents = sum_of_distances_to_agents / 4
            if current_average_distance_to_agents > max_average_distance_to_agents:
                max_average_distance_to_agents = current_average_distance_to_agents
                route_to_go_to = index
        return routes[route_to_go_to]
