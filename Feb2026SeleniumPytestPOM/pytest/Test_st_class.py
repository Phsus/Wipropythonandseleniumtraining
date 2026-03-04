# used inside the classes
# define  the class mandatorily

class Testclass:

    def setup_class(cls):
        print("API Authorization  is needed with username and password")

    def teardown_class(cls):
        print("API Authorization closed")

    def setup_class(method):
        print("opening the browser")

    def teardown_class(method):
        print("closing the browser")

    def testcase1(self):
        print("Testcase1 is executed")

    def testcase2(self):
        print("Testcase2 is executed")

    def testcase3(self):
        print("Testcase3 is executed")

class Testclass2:

    def testcase1(self):
        print("Testcase1 is executed")

    def testcase2(self):
        print("Testcase2 is executed")

    def testcase3(self):
        print("Testcase3 is executed")





