from file_handler import FileHandler
from lexical_analysis import LexicalAnalyser
import os


cwd = os.getcwd()
file = os.path.join(cwd, 'test_files', 'test.tex')

fh = FileHandler(file=file, options={}, verbosity=True)

fs = fh.file_stream_local()


la = LexicalAnalyser(file_stream=fs, verbosity=True)
st = la.scan_tex()

for token in st:
  print("{} - {}".format(token.tag, token.value))
