
# A Figure is either Mr. X (id = 0) or an Agent (id > 0)
# A figure holds on to his tickets and his current position

class Figure
  
  attr_accessor :tickets, :position
  attr_reader :id
  
  def initialize(id, position)
    @id = id
    @position = position
    if id > 0
      @tickets = {taxi: 10, bus: 8, underground: 4, black: 0}
    else
      @tickets = {taxi: 99, bus: 99, underground: 99, black: 4}
    end
  end
  
end
