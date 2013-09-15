"""
This file will likely not run.
Test are written first, and from these test, the actual functions are made
"""

#from django.test import TestCase
from unittest import TestCase
import bitstring
#import POC
import BitSlice

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
        result = slice(testWord, 16, 8)
        assert result == bitstring.Bits("0xFF") , "slice is pulling the wrong bits"    
        
    def test_sliceSequenceNum(self):
        testWord = bitstring.Bits("0x000000000000000E")
        result = getSequence(testWord)
        assert result == bitstring.Bits("0x7") , "get Sequence slice Failed"
        
    def test_sliceConsequtiveFlag(self):
        testWord = bitstring.Bits("0x0000000000000020")
        result = getConsequtiveFlag(testWord, )
        assert result == bitstring.Bits("0x1")
        
    def test_sliceUnsolicitedFlag(self):
        testWord = bitstring.Bits("0x0000000000000010")
        result = getUnsolicitedFlag(testWord)
        assert result == bitstring.Bits("0x1")     

    def test_sliceFirstFlag(self):
        testWord = bitstring.Bits("0x0000000000000040")
        result = getFirstFlag(testWord)
        assert result == bitstring.Bits("0x1")  

    def test_sliceFinalFlag(self):
        testWord = bitstring.Bits("0x0000000000000080")
        result = getFinalFlag(testWord)
        assert result == bitstring.Bits("0x1") 
        
    def test_getFunctionCode(self):
        testWord = bitstring.Bits("0x000000000000FF00")
        result = getFuncCode(testWord)
        assert result == bitstring.Bits("0x1") 