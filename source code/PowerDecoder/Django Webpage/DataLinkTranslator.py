import bitstring
#from BitSlice import slice
import BitSlice

'''confirms the beginning of the message is DNP3 standard'''
def DataLayerCorrect(testWord):
    #0564
    #print (testWord[0:16].hex)
    return testWord[0:16].uint == bitstring.BitArray('0x0564').uint
        
'''Gets Message length, in octets'''
def DataLayerLength(testWord):
    # one octet, 2 octets from left
    return testWord[16:24]
        
'''Gets transmission information'''
def DataLayerControl(testWord):
    #one octet, 3 octets from left
    return testWord[24:32]
        
'''Sender of message'''
def DataLayerSource(testWord):
    return testWord[48:64]

'''Reciever of message'''    
def DataLayerDestination(testWord):
    #two octets, 6 from the left
    return testWord[32:48]
    
'''Removes Bits Where CRC would be (does not detect if they are there)'''
def StripCRCBits(testWord):
    #CRC is the last 16 bits
    if(type(testWord) == bitstring.Bits):
        testWord = bitstring.BitArray(testWord)
    del testWord[-16:]
    return testWord


