import unittest
from unittest import TestCase
from Report import Report
import bitstring
import BitSlice
import DataLinkTranslator
import dictScriptV2
import parseInput

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
        testWord = bitstring.Bits("0x000000000000FA00")
        result = BitSlice.getFuncCode(testWord)
        assert result.int == bitstring.Bits("0x0FA").int ,  "slice is pulling the wrong bits ({}, {})".format(result.int, bitstring.Bits("0x0FF").int)   
        
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
        originalValue = 'This attribute provides the secure authentication version supported by the outstation. '
        dictionary = dictScriptV2.buildDict()
        testValue = dictionary[primaryRef][secondaryRef]
        #print('\n\n')
        #print(originalValue)
        #print(testValue)
        assert testValue["description"] == originalValue


    def test_DictionaryMidIndex(self):
        primaryRef = "0"
        secondaryRef = "242"
        originalValue = [('Attribute data type code ', 'UNIT8'), ('Length ', 'UNIT8'), ("Manufacturer's software version string. ", 'VSTRn')]
        dictionary = dictScriptV2.buildDict()
        testValue = dictionary[primaryRef][secondaryRef]
        #print('\n\n')
        #print(originalValue)
        #print(testValue)
        assert testValue["attributes"] == originalValue

    def test_DictionaryLastIndex(self):
        primaryRef = "0"
        secondaryRef = "255"
        originalValue = 'This is a special attribute that is used to retrieve a list of all of the device attribute variation numbers supported by the outstation at a specified index- and the properties of those attributes.  This object has a variable length that depends on the count of attribute variations supported by the outstation. '
        dictionary = dictScriptV2.buildDict()
        testValue = dictionary[primaryRef][secondaryRef]
        print('\n\n')
        print(originalValue)
        print('\n\n')
        print(testValue["description"])        
        assert testValue["description"] == originalValue

    def test_DictionaryBadIndex(self):
        primaryRef = "122"
        secondaryRef = "1"
        originalValue = 'This object is used to report the current value of a security statistic. See 11.9.10 for a description of a Security Statistic Point Type. See 7.5.2.2 for details of the point indexes permitted for this object and when the statistics are incremented. Variation 1 objects contain a 32-bit- unsigned integer count value.  '
        dictionary = dictScriptV2.buildDict()
        testValue = dictionary[primaryRef][secondaryRef]
        assert testValue["description"] != originalValue
		
    def test_ParseLogFile(self):
        logFile = "----------- ** Capture Session Started 12//09//2011 14:10:21 ** ------------\n" \
            + "(Port 23): No Response for Control\n" \
            + "(Port 23): Response Timeout for TB#1 Reg B CL-6, waited: 1000\n" \
            + "(Port 23):  \n" \
            + "(Port 23): DNP TX Analog Command - VOLTREDUCTION PERCENT @TB#1 Reg A CL-6 Point #16: Value -32768\n" \
            + "(Port 23)TX[25]: 05 64 12 C4 02 00 64 00 (FF B7)-CRC\n" \
            + "F8 C8 05 29 02 28 01 00 10 00 00 80 00 (E8 57)-CRC\n"
        parsedData = parseInput.parseData(logFile, "")
        result = [("056412C402006400","FFB7"),("F8C80529022801001000008000","E857")]
        assert result == parsedData

    def test_ParseSimpleInput(self):
        inputData = "05 64 05 C0 01 00 0A 00 (E0 8C), 05 64 12 C4 02 00 64 00 (FF B7)"
        parsedData = parseInput.parseData("" , inputData)
        result = [("056405C001000A00","E08C"), ("056412C402006400","FFB7")]
        assert result == parsedData

    def test_ParseTwoInputs(self): #when both inputs present, it should use the first one (if not empty)
        parsedData = parseInput.parseData("1", "2")
        result = "1"
        assert result == parsedData[0][0]
