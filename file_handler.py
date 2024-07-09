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
      assert(tex != None)
      tex.seek(0, 2)
      file_size = tex.tell()
      tex.seek(0)
      multiBuffer = tex.read(file_size)
      self.file_stream = multiBuffer
    
    if self.verbosity:
      print(self.file_stream)
    return self.file_stream
