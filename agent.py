
class AgentPlayer
  
  def initialize
    @@possible_positions_mrx = []
  end
  
  # play gets called by the controller once per turn
  def play(gamestate)
    if gamestate[:figure_id] == 1
      calculate_possible_positions_mrx(gamestate[:position_of_mrx], gamestate[:mrx_last_used_ticket], gamestate[:board])
    end
    play_greedy(gamestate[:routes], gamestate[:board])
  end
  
  # Play to a random station
  def play_random(routes)
    routes.sample
  end
  
  def play_greedy(routes, board)
    return nil if routes.empty?
    return play_random(routes) if @@possible_positions_mrx.empty?
    min_average_distance_to_mrx = 10
    route_to_go_to = 0
    routes.each_with_index do |route, index|
      my_position = route[:station]
      sum_of_distances_to_mrx = 0
      @@possible_positions_mrx.each do |position_of_mrx|
        current_distance_to_mrx = board.distance(my_position, position_of_mrx)
        sum_of_distances_to_mrx += current_distance_to_mrx
      end
      current_avgerage_distance_to_mrx = sum_of_distances_to_mrx / @@possible_positions_mrx.length
      if current_avgerage_distance_to_mrx < min_average_distance_to_mrx
        min_average_distance_to_mrx = current_avgerage_distance_to_mrx
        route_to_go_to = index
      end
    end
    return routes[route_to_go_to]
  end
  
  def calculate_possible_positions_mrx(position_of_mrx, mrx_last_used_ticket, board)
    if position_of_mrx == 0
      new_positions = []
      @@possible_positions_mrx.each do |p|
        board.routes_from(p).each do |q|
          if q[:ticket] == mrx_last_used_ticket and not new_positions.include?(q[:station])
            new_positions << q[:station]
          end
        end
      end
      @@possible_positions_mrx = new_positions.sort
    else
      @@possible_positions_mrx = [position_of_mrx]  
    end
  end
  
end
