import unittest
from unittest import TestCase
from Report import Report
import bitstring
import BitSlice
import DataLinkTranslator
import dictScriptV2

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
        result = DataLinkTranslator.DataLayerCorrect(testWord)
        assert result , "The hex number is not interpreted right"
        
    def test_DataLayerLengthSliceGrabsRightBits(self):
        testWord = bitstring.Bits("0x0564B34483000100")
        result = DataLinkTranslator.DataLayerLength(testWord)
        assert result.uint == bitstring.Bits("0xB3").uint , "Did not grab correct length, grabbed {},\n should be {}".format(result.bin, bitstring.Bits("0xB3").bin)
        
    def test_DataLayerControlSliceGrabsRightBits(self):
        testWord = bitstring.Bits("0x0564B34483000100")
        result = DataLinkTranslator.DataLayerControl(testWord)
        assert result.uint == bitstring.Bits("0x44").uint , "Did not grab right control Octet, grabbed {},\n should be {}".format(result.bin, bitstring.Bits("0x44").bin)
        
    def test_DataLayerSourceSliceGrabsRightBits(self):
        testWord = bitstring.Bits("0x0564B34483000100")
        result = DataLinkTranslator.DataLayerSource(testWord)
        assert result.uint == bitstring.Bits("0x0100").uint , "Did not Grab the right bits, grabbed {},\n should be {}".format(result.bin, bitstring.Bits("0x0100").bin)
        
    def test_DataLayerDestinationSliceGrabsRightBits(self):
        testWord = bitstring.Bits("0x0564B34483000100")
        result = DataLinkTranslator.DataLayerDestination(testWord)
        assert result.uint == bitstring.Bits("0x8300").uint , "Did not Grab the right bits, grabbed {}".format(result.hex)
    
    def test_StripCRCRemovesCRCBits(self):
        testWord = bitstring.Bits("0x0564B34483000100DF89")
        result = DataLinkTranslator.StripCRCBits(testWord)
        assert result.uint == bitstring.Bits("0x0564B34483000100").uint , "Did not Grab the right bits, grabbed {}".format(result.hex)
        
    def test_PresentationObjectLayersCorrectly(self):
        baseTestObject = Report("Test1", "This should be the description", "DATADATADATADATA")
        baseTestObject.AddNext(Report("Test2", "This is another description", "more data"))
        baseTestObject.Next[0].AddNext(Report("Test3", "", ""))
        
        assert baseTestObject.title == "Test1"
        assert baseTestObject.Next[0].title == "Test2"
        assert baseTestObject.Next[0].Next[0].title == "Test3" 
        

    def test_DictionaryFirstIndex(self):
        primaryRef = "0"
        secondaryRef = "209"
        originalValue = []
        originalValue.append('Device Attributes :: Secure authentication version :: Attrib :: This attribute provides the secure authentication version supported by the outstation. :: Attribute data type code :: UNIT8 :: Length :: UNIT8 :: Secure authentication version :: UINTn ::  :: ')
        dictionary = dictScriptV2.buildDict()
        testValue = dictionary[primaryRef][secondaryRef]
        #print('\n\n')
        #print(originalValue)
        #print(testValue)
        assert testValue == originalValue


    def test_DictionaryMidIndex(self):
        primaryRef = "0"
        secondaryRef = "242"
        originalValue = []
        originalValue.append("Device Attributes :: Device manufacturer's software version :: Attrib :: This attribute is the version code of the manufacturer's device software.  The contents of the attribute is a free form string that is formatted according to the manufacturer's normal practice.   :: Attribute data type code :: UNIT8 :: Length :: UNIT8 :: Manufacturer's software version string. :: VSTRn ::  :: ")
        dictionary = dictScriptV2.buildDict()
        testValue = dictionary[primaryRef][secondaryRef]
        #print('\n\n')
        #print(originalValue)
        #print(testValue)
        assert testValue == originalValue

    def test_DictionaryLastIndex(self):
        primaryRef = "0"
        secondaryRef = "255"
        originalValue = []
        originalValue.append('Device Attributes :: List of attribute variations :: Attrib :: This is a special attribute that is used to retrieve a list of all of the device attribute variation numbers supported by the outstation at a specified index- and the properties of those attributes.  This object has a variable length that depends on the count of attribute variations supported by the outstation. :: Attribute data type code :: UNIT8 :: Length :: UNIT8 :: Data Elements :: SET of n :: Attribute variation number :: UINT8 :: Attribute properties :: BSTR8 ::  :: ')
        dictionary = dictScriptV2.buildDict()
        testValue = dictionary[primaryRef][secondaryRef]
        #print('\n\n')
        #print(originalValue)
        #print(testValue)        
        assert testValue == originalValue

    def test_DictionaryBadIndex(self):
        primaryRef = "121"
        secondaryRef = "1"
        originalValue = []
        originalValue.append('Security Statistic :: 32-bit with flag :: Static :: This object is used to report the current value of a security statistic. See 11.9.10 for a description of a Security Statistic Point Type. See 7.5.2.2 for details of the point indexes permitted for this object and when the statistics are incremented. Variation 1 objects contain a 32-bit- unsigned integer count value.  :: Flag Octet :: BSTR8 ::Bit 0: ONLINE :: Bit 1: RESTART :: Bit 2: COMM_LOST :: Bit 3: REMOTE_FORCED :: Bit 4: LOCAL_FORCED :: Bit 5: Reserved- always 0 :: Bit 6: DISCONTINUITY :: Bit 7: Reserved- always 0 :: Association ID :: UINT16 :: Count value :: UINT32 ::  :: ')
        dictionary = dictScriptV2.buildDict()
        testValue = dictionary[primaryRef][secondaryRef]
        assert testValue != originalValue
