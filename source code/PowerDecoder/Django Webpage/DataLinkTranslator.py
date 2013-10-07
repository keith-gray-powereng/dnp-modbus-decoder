import bitstring
#from BitSlice import slice
import BitSlice

'''confirms the beginning of the message is DNP3 standard'''
def DataLayerCorrect(testWord):
    #0564
    print (testWord[0:16].hex)
    return testWord[0:16].uint == bitstring.BitArray('0x0564').uint
        
def DataLayerLength(testWord):
    pass
        
def DataLayerControl(testWord):
    pass
        
def DataLayerSource(testWord):
    pass
        
def DataLayerDestination(testWord):
    pass
    
def StripCRCBits(testWord):
    pass


