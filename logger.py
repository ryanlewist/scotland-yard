
class Logger
  
  def initialize(filename = 'log.md')
    @filename = filename
    @contents = "*Date: #{Time.now}*\n"
    @contents << "----------------------------------------\n"
  end
  
  def log(message)
    @contents << message << "\n"
  end
  
  def save
    File.open(@filename, 'w') {|f| f.puts(@contents)}
  end
  
end
