class SharedTests:
    @staticmethod
    def testSingletonBehaviour(object):
        firstInstance = object()
        secondInstance = object()
        assert firstInstance == secondInstance, "Objects should be the same instance"