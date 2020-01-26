import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_empty_list(self,):
        """ When the list is empty """

        self.assertTrue(a1.stock_price_summary([]) == (0, 0))


    def test_zero_list(self,):
        """ When the list contains only zero """

        self.assertTrue(a1.stock_price_summary([0,]) == (0, 0))
        

    def test_only_gain(self,):
        """ When the list contains only gain and no losses """

        self.assertTrue(a1.stock_price_summary([0.15,]) == (0.15, 0))


    def test_only_loss(self,):
        """ When the list contains only loss and no gains """

        self.assertTrue(a1.stock_price_summary([-0.15,]) == (0, -0.15))


    def test_normal(self,):
        """ When the list contains both gains and losses """

        self.assertTrue(a1.stock_price_summary([0.15, -0.15, 0]) == (0.15, -0.15))    

    


if __name__ == '__main__':
    unittest.main(exit=False)
