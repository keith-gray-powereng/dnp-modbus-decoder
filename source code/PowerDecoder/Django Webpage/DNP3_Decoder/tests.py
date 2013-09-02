"""
This file will likely not run.
Test are written first, and from these test, the actual functions are made
"""

from django.test import TestCase
import bitstring
import POC


class SimpleTest(TestCase):
    def setUp(self):
        #do stuff here to setup tests
        #POC does not require a standard setup
        pass
        
    def test_sliceTestFail(self):
        testWord = bitstring.Bits("0x0000F0000")
        result = slice(testWord, 0, 2)
        assert result == bitstring.Bits("0x0") , "slice somehow returned the correct result"
        
    def test_sliceTestPass(self):
        testWord = bitstring.Bits("0x0000FF0000")
        result = slice(testWord, 8, 2)
        assert result == bitstring.Bits("0xFF") , "slice is pulling the wrong bits"    
        