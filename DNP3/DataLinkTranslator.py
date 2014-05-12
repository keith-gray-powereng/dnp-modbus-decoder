import bitstring
#from BitSlice import slice
from .Report import Report

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
    
def DataLayerControlReport(ControlOctet):
    ControlByte = Report("Control Byte", "Message Context", ControlOctet)
    if ControlOctet[0:1].uint == 1:
        ControlByte.AddNext(Report("DIR bit", "Message Direction", "From Master Station"))
    else:
        ControlByte.AddNext(Report("DIR bit", "Message Direction", "From Slave Station"))
        
    PRM = ControlOctet[1:2].uint
    Source = ""
    if PRM == 1:
        Source = "Use FCB and FCV for synching"
    else:
        Source = "Message Completing"
    ControlByte.AddNext(Report("PRM bit", "Primary message indicator", Source))

    ControlByte.AddNext(Report("FCB bit", "Frame Count Bit", ControlOctet[2:3].uint == 1))
    
    if PRM == 1:
        ControlByte.AddNext(Report("FCV bit", "Frame Count Valid", ControlOctet[3:4].uint == 1))
    else:
        ControlByte.AddNext(Report("DFC bit", "Data Flow Control, buffers were availble", not ControlOctet[3:4] == 1))
        
    funcCode = ControlOctet[5:9]
    functionName = ""
    if PRM == 1:
        FCV = -1
        if funcCode.uint == 0:
            functionName = "RESET_LINK_STATES (0)"
            FCV = 0
        elif funcCode.uint == 2:
            functionName = "TEST_LINK_STATES (2)"
            FCV = 1
        elif funcCode.uint == 3:
            functionName = "CONFIRMED_USER_DATA (3)"
            FCV = 1
        elif funcCode.uint == 4:
            functionName = "UNCONFIRMED_USER_DATA (4)"
            FCV = 0
        elif funcCode.uint == 9:
            functionName = "REQUEST_LINK_STATUS (9)"
            FCV = 0
        else:
            functionName = "RESERVED ({})".format(funcCode)
        
    else:
        if funcCode.uint == 0:
            functionName = "ACK (0)"
        elif funcCode.uint == 1:
            functionName = "NACK (1)"
        elif funcCode.uint == 11:
            functionName = "LINK_STATUS (11)"
        elif funcCode.uint == 15:
            functionName = "NOT_SUPPORTED (15)"
        else:
            functionName = "RESERVED ({})".format(funcCode)
    ControlByte.AddNext(Report("Function", "Action for outstation to take with this message", functionName))
    return ControlByte
            
            

