from tokeniser import Token
class LexicalAnalyser:
  def __init__(self, file_stream):
    self.file_stream = file_stream
    self.current_index = 0


  def next_character(self):
    if self.current_index < len(self.file_stream):
      peek = self.file_stream[self.current_index]
      self.current_index +=1
      return peek
    else: return '\0'

  def scan_tex(self):
    current_token = Token()
    lexeme = ""

