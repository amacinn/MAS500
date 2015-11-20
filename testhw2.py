#Ali Shtarbanov
#Andrew MacInnes

#Test file

import unittest
import homework2

class TestMediaCloudAPICall (unittest.TestCase):
	def testMediaCloudAPICall (self):
		res = homework2.activateNow()
		assert res!=None 
		
if __name__ == "__main__":
    unittest.main()
