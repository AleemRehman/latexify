class Token:
  def __init__(self, tag= None, value="", line=0):
    self.tag = tag
    self.value = value
    self.line = line

  def __copy__(self):
    return Token(self.tag, self.value, self.line)
  

  def __eq__(self, other_token):
    if not isinstance(other_token, Token):
      return False
    return self.tag == other_token.tag and self.value == other_token.value and self.line == other_token.line
  
  def set_tag(self, tag):
    self.tag = tag
    return tag
  
  def set_value(self, value):
    self.value = value
    return value
  
  def set_line(self, line):
    self.line = line
    return line
