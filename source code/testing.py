"""Support for testing.  Also a roundabout way of disabling certain requirements to run tests without the use of a database."""

from django.test.simple import DjangoTestSuiteRunner

class DatabaselessTestRunner(DjangoTestSuiteRunner):
    """A test suite runner that does not set up and tear down a database."""

    def setup_databases(self):
        pass

    def teardown_databases(self, *args):
        pass