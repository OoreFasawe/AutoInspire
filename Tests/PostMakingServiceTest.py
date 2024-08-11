#TODO(oore)- Streamline imports in a better way
import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot/Utility'))
from SharedTests import SharedTests
from PostMakingService import PostMakingService
class PostMakingServiceTest:
    def runTests(self):
        self.testForPostMakingServiceSingletonBehaviour()

    def testForPostMakingServiceSingletonBehaviour(self):
        SharedTests.testSingletonBehaviour(PostMakingService)

        
postMakingServiceTest = PostMakingServiceTest()
postMakingServiceTest.runTests()

        
    
