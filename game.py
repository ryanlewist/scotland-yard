
require 'board'
require 'figure'
require 'logger'

# The class Game fully describes Scotland Yard:
# The board, Mr. X and the agents.
# There are higher-level methods that change the state of the game.

class Game
  
  # Initialization creates a board and the figures
  # Then the figures are put on random starting positions
  def initialize
    puts "Starting game"
    puts "Loading board..."
    @board = Board.new
    start = [13, 26, 29, 34, 50, 53, 91, 94, 103, 112, 117, 132, 138, 141, 155, 174, 197, 198].shuffle
    @figures = []
    for i in 0..4
      @figures << Figure.new(i, start.pop)
    end
    @turns = 0
    @mrx_last_used_ticket = nil
    @logger = Logger.new
    log "## SCOTLAND YARD: MR. X VS. 4 AGENTS"
  end
  
  def log(msg)
    @logger.log(msg)
  end
  
  # Is the game over?
  # There are two possibilities:
  # - Mr. X and an agent are at the same station (=> The agents win)
  # - 20 turns have passed (=> Mr. X has won)
  def over?
    for i in 1..4
      if @figures[0].position == @figures[i].position
        log "**GAME OVER:** Mr. X was caught - The agents win."
        @logger.save
        puts "Game Over: The agents win"
        return true
      end
    end
    if @turns > 19
      log "**GAME OVER:** 20 turns have passed - Mr. X wins."
      @logger.save
      puts "Game Over: Mr. X wins"
      return true
    end
    return false
  end
  
  # Returns the position of Mr. X at the 3., 8., 13., 18. and 23. turn or 0.
  def position_of_mrx
    if @turns % 5 == 3
      @figures[0].position
    else
      0
    end
  end
  
  # Returns an array of the positions of the agents.
  def positions_of_agents
    positions = []
    @figures.each {|f| positions << f.position}
    positions.shift
    positions
  end
  
  def tickets
    tickets = []
    @figures.each {|f| tickets << f.tickets}
    tickets
  end
  
  def possible_routes_for(figure)
    routes = @board.routes_from(figure.position)
    routes.delete_if {|r| figure.tickets[r[:ticket]] == 0}
    if figure.id > 0
      routes.delete_if {|r| positions_of_agents.include?(r[:station])}
    end
    routes
  end
  
  # Moves the fgure with figure_id to [station] by [ticket].
  def move(figure_id, station, ticket)
    figure = @figures[figure_id]
    routes = possible_routes_for(figure)
    if routes.include?({station: station, ticket: ticket}) or ticket == :black
      if figure.id == 0
        log "\n### TURN #{@turns + 1}:"
        @turns += 1
        @mrx_last_used_ticket = ticket
      end
      figure_name = figure.id == 0 ? "Mr. X" : "Agent #{figure.id}"
      log "**#{figure_name}** moves from *#{figure.position}* to *#{station}* by *#{ticket}*\n"
      figure.tickets[ticket] -= 1
      figure.position = station
      return true
    end
    return false
  end
  
  # Describes the current gamstate
  def gamestate(figure_id)
    {
      figure_id: figure_id,
      routes: possible_routes_for(@figures[figure_id]),
      board: @board,
      position_of_mrx: position_of_mrx,
      positions_of_agents: positions_of_agents,
      turns: @turns,
      tickets: tickets,
      mrx_last_used_ticket: @mrx_last_used_ticket
    }
  end
  
end
