from tokeniser import Token
import re
class LexicalAnalyser:
  def __init__(self, file_stream, verbosity= False):
    self.file_stream = file_stream
    self.current_index = 0
    self.verbosity = verbosity
    self.token_stream = []
    self.token_patterns = {
      'command': r'\\[a-zA-Z@]+',
      'comment': r'%.*',
      'environment': r'\\begin\{.*?\}|\\end\{.*?\}',
      'group': r'\{.*?\}',
      'text': r'[^\\\{\}\n%]+'
    }


  
  def scan_tex(self):
    current_token = Token()
    lexeme = ""
    for match in re.finditer(self.token_regex, self.file_stream):
      kind = match.lastgroup
      value = match.group()
      if kind == 'NEWLINE':
          continue
      elif kind == 'WHITESPACE':
          continue
      elif kind == 'COMMENT':
          continue
      else:
          current_token.set_value(value)
          current_token.set_tag(kind)
          self.token_stream.append(current_token)

    if self.verbosity:
      print(self.token_stream)
    return self.token_stream

