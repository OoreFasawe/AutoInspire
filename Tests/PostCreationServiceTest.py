import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Tests.SharedTests import SharedTests
from Utility.PostCreationService import PostCreationService
class PostCreationServiceTest:
    def runTests(self):
        self.testForPostCreationServiceSingletonBehaviour()

    def testForPostCreationServiceSingletonBehaviour(self):
        SharedTests.testSingletonBehaviour(PostCreationService)

        
postCreationServiceTest = PostCreationServiceTest()
postCreationServiceTest.runTests()

        
    
