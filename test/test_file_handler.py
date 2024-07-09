import unittest
from file_handler import FileHandler


class FileHandlerTestSuite(unittest.TestCase):
  def test_file_stream(self):
    fh = FileHandler()
