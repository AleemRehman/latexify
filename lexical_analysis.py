from tokeniser import Token
import re
class LexicalAnalyser:
  def __init__(self, file_stream, verbosity= False):
    self.file_stream = file_stream
    self.current_index = 0
    self.verbosity = verbosity
    self.token_specification = [
      ('COMMAND', r'\\[a-zA-Z]+'),          # LaTeX commands
      ('BEGIN_ENV', r'\\begin\{[a-zA-Z]+\}'), # Begin environment
      ('END_ENV', r'\\end\{[a-zA-Z]+\}'),   # End environment
      ('COMMENT', r'%.*'),                 # Comments
      ('TEXT', r'[^\\%]+'),                # Text (not starting with \ or %)
      ('NEWLINE', r'\n'),                  # Line endings
      ('WHITESPACE', r'[ \t]+'),           # Spaces and tabs
    ]

    self.token_regex = re.compile('|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.token_specification))

    self.token_stream = []


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
      import pdb
      pdb.set_trace()
      print(self.token_stream)
    return self.token_stream

