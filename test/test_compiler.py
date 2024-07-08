from compiler import Compiler
import unittest

class CompilerTestSuite(unittest.TestCase):
  def compiler_document():
    # compile a normal LaTex document, no components
    # this should PASS with valid inputs!
    return ''
  
  def inject_guard_rail():
    # compile normal document but with malicious code, put guard rails around it
    return ''
  
if __name__== 'main':
  unittest.main()