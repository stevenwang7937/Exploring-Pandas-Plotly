import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_zero(self,):
        """ When number of people equals zero """

        self.assertEqual(a1.num_buses(0),0)


    def test_less_fifty(self,):
        """ When number of people is less than 50 """

        self.assertEqual(a1.num_buses(25),1)


    def test_fifty(self,):
        """ When number of people equals 50 """

        self.assertEqual(a1.num_buses(50),1)


    def test_more_fifty(self,):
        """ When number of people equals greater than 50 """

        self.assertEqual(a1.num_buses(51),2)
        
            
    

if __name__ == '__main__':
    unittest.main(exit=False)
