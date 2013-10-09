
"""
This file will likely not run.
Test are written first, and from these test, the actual functions are made
"""

#from django.test import TestCase
from unittest import TestCase
from Report import Report
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

    def test_DataStartIsCorrect(self):
        testWord = bitstring.Bits("0x0564B34483000100DF89")
        result = BitSlice.DataLayerCorrect(testWord)
        assert result , "The hex number is not interpreted right"
        
    def test_DataLayerLengthSliceGrabsRightBits(self):
        testWord = bitstring.Bits("0x0564B34483000100DF89")
        result = BitSlice.DataLayerLength(testWord)
        assert result.uint == bitstring.Bits("0xB3").uint , "Did not grab correct length"
        
    def test_DataLayerControlSliceGrabsRightBits(self):
        testWord = bitstring.Bits("0x0564B34483000100DF89")
        result = BitSlice.DataLayerControl(testWord)
        assert result.uint == bitstring.Bits("0x44").uint , "Did not grab right control Octet"
        
    def test_DataLayerSourceSliceGrabsRightBits(self):
        testWord = bitstring.Bits("0x0564B34483000100DF89")
        result = BitSlice.DataLayerSource(testWord)
        assert result.uint == bitstring.Bits("0x0100").uint , "Did not Grab the right bits"
        
    def test_DataLayerDestinationSliceGrabsRightBits(self):
        testWord = bitstring.Bits("0x0564B34483000100DF89")
        result = BitSlice.DataLayerDestination(testWord)
        assert result.uint == bitstring.Bits("0x8300").uint , "Did not Grab the right bits"
    
    def test_StripCRCRemovesCRCBits(self):
        testWord = bitstring.Bits("0x0564B34483000100DF89")
        result = BitSlice.StripCRCBits(testWord)
        assert result.uint == bitstring.Bits("0x0564B34483000100").uint , "Did not Grab the right bits"
        
        
    def test_PresentationObjectLayersCorrectly(self):
        baseTestObject = Report("Test1", "This should be the description", "DATADATADATADATA")
        baseTestObject.AddNext(Report("Test2", "This is another description", "more data"))
        baseTestObject.Next[0].AddNext(Report("Test3", "", ""))
        
        assert baseTestObject.title == "Test1"
        assert baseTestObject.Next[0].title == "Test2"
        assert baseTestObject.Next[0].Next[0].title == "Test3" 
        
    
