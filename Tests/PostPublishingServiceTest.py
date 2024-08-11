#TODO(oore)- Streamline imports in a better way
import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot/Utility'))
from SharedTests import SharedTests
from PostPublishingService import PostPublishingService
class PostPublishingServiceTest:
    def runTests(self):
        self.testForPostMakingServiceSingletonBehaviour()

    def testForPostPublishingSingletonBehaviour(self):
        SharedTests.testSingletonBehaviour(PostPublishingService)
        
postPublishingServiceTest = PostPublishingServiceTest()
postPublishingServiceTest.runTests()