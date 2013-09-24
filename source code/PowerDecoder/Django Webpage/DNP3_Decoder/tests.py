
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
        
        #heads up, these numbers are signed
        # a leading zero is needed to show positivity
    def test_sliceTestFail(self):
        testWord = bitstring.Bits("0x00000000000F0000")
        result = BitSlice.slice(testWord, 0, 2)
        assert result.int == bitstring.Bits("0x0").int , "slice somehow returned the correct result ({})".format(result)
        
    def test_sliceTestPass(self):
        testWord = bitstring.Bits("0x0000000000FF0000")
        result = BitSlice.slice(testWord, 8, 16)
        assert result.int == bitstring.Bits("0x0FF").int , "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x0FF").int)   
        
    def test_sliceSequenceNum(self):
        testWord = bitstring.Bits("0x000000000000000E")
        result = BitSlice.getSequence(testWord)
        assert result.int == bitstring.Bits("0x07").int ,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x07").int)   
        
    def test_sliceConsequtiveFlag(self):
        testWord = bitstring.Bits("0x0000000000000020")
        result = BitSlice.getConsequtiveFlag(testWord, )
        assert result.int == bitstring.Bits("0x01").int,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x01").int)   
        
    def test_sliceUnsolicitedFlag(self):
        testWord = bitstring.Bits("0x0000000000000010")
        result = BitSlice.getUnsolicitedFlag(testWord)
        assert result.int == bitstring.Bits("0x01").int,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x01").int)   

    def test_sliceFirstFlag(self):
        testWord = bitstring.Bits("0x0000000000000040")
        result = BitSlice.getFirstFlag(testWord)
        assert result.int == bitstring.Bits("0x01").int ,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x01").int)   

    def test_sliceFinalFlag(self):
        testWord = bitstring.Bits("0x0000000000000080")
        result = BitSlice.getFinalFlag(testWord)
        assert result.int == bitstring.Bits("0x01").int,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x01").int)   
        
    def test_getFunctionCode(self):
        testWord = bitstring.Bits("0x000000000000FF00")
        result = BitSlice.getFuncCode(testWord)
        assert result.int == bitstring.Bits("0x0FF").int ,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x0FF").int)   
        
    def test_getLSBCodeSet(self):
        testWord = bitstring.Bits("0x00000000000F0000")
        result = BitSlice.getLSBInternalIndications(testWord)
        assert result.int == bitstring.Bits("0x0F").int ,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x0F").int)   
        
    def test_getMSBCodeSet(self):
        testWord = bitstring.Bits("0x0000000000F00000")
        result = BitSlice.getMSBInternalIndications(testWord)
        assert result.int == bitstring.Bits("0x0F").int ,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x0F").int)   
