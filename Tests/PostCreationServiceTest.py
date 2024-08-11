#TODO(oore)- Streamline imports in a better way
import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot/Utility'))
from SharedTests import SharedTests
from PostCreationService import PostCreationService
class PostCreationServiceTest:
    def runTests(self):
        self.testForPostCreationServiceSingletonBehaviour()

    def testForPostCreationServiceSingletonBehaviour(self):
        SharedTests.testSingletonBehaviour(PostCreationService)

        
postCreationServiceTest = PostCreationServiceTest()
postCreationServiceTest.runTests()

        
    
