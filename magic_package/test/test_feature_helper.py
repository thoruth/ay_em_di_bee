import unittest

from magic_package import feature_helper
from torch import index_put_

class TestStringMethods(unittest.TestCase):

    def test_penalizer(self):
        #mock
        
        #test
        result = feature_helper.rating_review_adjuster(9.3, 2200000)
        expected =  9.1
        #assert
        self.assertAlmostEqual(result, expected, places=9)

    def test_oscar_score(self):
    
        #mock
        
        #test
        value_to_test = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        res = []
        for value in value_to_test:
            res.append(feature_helper.oscar_value(value))
        expected = [0,0.3, 0.3, 0.5, 0.5, 0.5, 1 , 1, 1, 1, 1, 1.5, 1.5]
        #assert
        for index in range(len(value_to_test)):
            self.assertEqual(res[index], expected[index])


if __name__ == '__main__':
    unittest.main()
