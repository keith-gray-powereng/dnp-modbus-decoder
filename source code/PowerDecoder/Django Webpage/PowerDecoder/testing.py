#code from Martin Vilcans
#http://www.librador.com/2011/05/23/How-to-run-Django-tests-without-a-database/

#"""Support for testing."""

from django.test.simple import DjangoTestSuiteRunner

class DatabaselessTestRunner(DjangoTestSuiteRunner):
    #"""A test suite runner that does not set up and tear down a database."""

    def setup_databases(self):
        #"""Overrides DjangoTestSuiteRunner"""
        pass

    def teardown_databases(self, *args):
        #"""Overrides DjangoTestSuiteRunner"""
        pass