class Compiler:
  def __init__(self, verbosity, options):
    self.verbosity = verbosity
    self.options = options
    self.latex_processor = ''

    if self.options['pdf']:
      self.latex_processor = 'pdflatex'
    
    self.output = ''
    self.glossaries = dict()
    self.indexer = 0
    self.bib = ''


  def compile(self, input, recompile = False):
    # main hook for the compilation of the input, bringing together all other compilation steps
    if self.verbosity:
      return '-'*20+'currently compiling'+'-'*20

    
    return ''
  
  def compare_current_old(self, input):
    # compare the last staged and compiled document to the one with the current changes, only make compile new elements and de-couple elements removed

    if self.verbosity:
      return 'comparing old doc to new, only compile new elements of page'
    

  
  def text_stream(self, input):
    # receive the stream from the console, change to WebSocket API connection when FE begun
    return ''
  

  
  def guard_rail(self, input):
    # wrap code to handle safely, stop execution of code by compiler
    return ''
  


cmp = Compiler(verbosity=True)


