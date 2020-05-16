
require 'game'
require 'mrx'
require 'agent'

class Controller

  def run
    game = Game.new
    players = [MrXPlayer.new, AgentPlayer.new, AgentPlayer.new, AgentPlayer.new, AgentPlayer.new]
    while true
      players.each_with_index do |p, i|
        route = p.play(game.gamestate(i))
        game.move(i, route[:station], route[:ticket]) unless route.nil?
      end
      break if game.over?
    end
  end
  
end
