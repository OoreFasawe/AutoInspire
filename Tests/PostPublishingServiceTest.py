import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Tests.SharedTests import SharedTests
from Utility.PostPublishingService import PostPublishingService
class PostPublishingServiceTest:
    def runTests(self):
        self.testForPostMakingServiceSingletonBehaviour()

    def testForPostPublishingSingletonBehaviour(self):
        SharedTests.testSingletonBehaviour(PostPublishingService)
        
postPublishingServiceTest = PostPublishingServiceTest()
postPublishingServiceTest.runTests()