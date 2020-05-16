class MrXPlayer

    # play gets called by the controller once per turn
    def play(gamestate)
        play_greedy(gamestate[:routes], gamestate[:positions_of_agents], gamestate[:board])

    end

    # Play to a random station
    def play_random(routes)
        routes.sample

    end

    # Play to the station with the maximal avarage distance to all agents
    # using a greedy algorithm
    def play_greedy(routes, positions_of_agents, board)
        max_average_distance_to_agents = 0
        route_to_go_to = 0
        routes.each_with_index
        do | route, index |
        my_position = route[:station]
        sum_of_distances_to_agents = 0
        positions_of_agents.each
        do | position_of_agent |
        current_distance_to_agent = board.distance(my_position, position_of_agent)
        sum_of_distances_to_agents += current_distance_to_agent

    end
    current_avgerage_distance_to_agents = sum_of_distances_to_agents / 4
    if current_avgerage_distance_to_agents > max_average_distance_to_agents
        max_average_distance_to_agents = current_avgerage_distance_to_agents
        route_to_go_to = index
    end


end
routes[route_to_go_to]
end

end
