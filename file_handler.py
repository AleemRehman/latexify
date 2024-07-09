import os
class FileHandler():
  def __init__(self, file, options, verbosity=False):
    self.file = file
    self.options = options
    self.file_stream = ''
    self.project_name = ''
    self.verbosity = verbosity or False

    if self.file.lower().endswith('.tex'):
      self.project_name = self.file.lower()[:4]
      self.tex = True




  def file_stream_local(self):
    if self.tex:
      tex = open(self.file, "r")
      self.file_stream = tex

      if self.verbosity:
        print(self.file_stream.read())
    return self.file_stream



# cwd = os.getcwd()
# file = os.path.join(cwd, 'test_files', 'test.tex')

# fh = FileHandler(file=file, options={}, verbosity=True)

# fh.file_stream_local()
