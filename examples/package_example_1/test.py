## import main source
from os import path
# import python unittest class
import sys, unittest
# add the root package page to python system path so
# we can import the main package module
sys.path.append(path.join('..', '..'))

# import pandas csv reader and frame unit tester
from pandas import read_csv
from pandas.testing import assert_frame_equal

# import the transform functions
from transform.normalize import transform

# import the main package module model 
import testing_pkg_creation.main.model as model

# helper function to load example inputs from input folder
def load(csv, folder='input'):
  dir, filename = path.split(__file__)
  return read_csv(path.join(dir, folder, csv))

class TestPackage(unittest.TestCase):

  def setUp(self):
    # load your example spectra from the inputs folder
    self.spectra = load('ExampleSpectra.csv')

  def test_model(self):
    # Assert your transform fuction workers
    self.spectra = transform(self.spectra)
    assert_frame_equal(self.spectra, load('ExampleSpectra_Normalized.csv', 'output'))

    # actually run the model
    result = model.run(self.spectra)
    # assert the model gives the desired results
    assert_frame_equal(result, load('ExampleOutput_Predictions.csv', 'output'))

if __name__ == '__main__':
  unittest.main()