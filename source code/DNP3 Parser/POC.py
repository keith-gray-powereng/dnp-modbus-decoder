
#FIVE SPACES TO A TAB


#a basic message to get us started
#05 64 05 C0 01 00 0A 00

#bitstring is a dependency of python in order for this to work
#https://code.google.com/p/python-bitstring/
import bitstring

#application header mask (bits must be reversed first)
appMask = bitstring.Bits("0x000000000000000F")
seqMask = bitstring.Bits("0x000000000000000E")
seqShift = 0
consecutiveMask = bitstring.Bits("0x0000000000000020")
consecutiveShift = 5
unsolicitedMask = bitstring.Bits("0x0000000000000010")
unsolicitedShift = 4
firstMask = bitstring.Bits("0x0000000000000040")
firstShift = 6
finalMask = bitstring.Bits("0x0000000000000080")
finalShift = 7


#function code masks
#81 through 83 (hex) indicates response
funcCodeMask = bitstring.Bits("0x000000000000FF00")
funcCodeShift = 8

#only for response from outstations
lsbMask = bitstring.Bits("0x00000000000F0000")
msbMask = bitstring.Bits("0x0000000000F00000")
lsbShift = 12
msbShift = 16



def DNP3(message):
    
    #bytes are recieved in reverse byte order
    print (message)
    binMessage = bitstring.BitArray(message)
    numMessage = int(message,16)
    #binMessage = bin(int(message,16))
    
    #flip
    print ("binary:")
    print (binMessage.bin)
    binMessage = binMessage[::-1]
    print (binMessage.bin)
    
    print ("DNP3 --- MESSAGE BEGIN -----")
    print(str(len(binMessage)) + " " + str(len(seqMask)))
    print ("NumMessage " + str(numMessage))
    #print ("seqMessage:" + str(int(seqMask,16)))
    seqValue = (binMessage & seqMask) >> seqShift
    confirmValue = (binMessage & consecutiveMask) >> consecutiveShift
    unsolicitedValue = (binMessage & unsolicitedMask) >> unsolicitedShift
    firstValue = (binMessage & firstMask) >> firstShift
    finalValue = (binMessage & finalMask) >>finalShift
    
    print("seqValue: " + str(seqValue))
    print("confirm: " + str(confirmValue))
    print("unsolicited: " + str(unsolicitedValue))
    print("firstValue: " + str(firstValue))
    print("finalValue: " + str(finalValue))
    
    appControl = ""
    if firstValue.uint > 0:
        appControl += "FIRST "
    if finalValue.uint > 0 :
        appControl += "FINAL "
    if confirmValue.uint > 0:
        appControl += "CONFIRM "
    if unsolicitedValue.uint > 0:
        appControl += "UNSOLICITED"
        
    print (appControl)
    
    
    #function code parsing
    functionSection = (binMessage & funcCodeMask) >> funcCodeShift
    print("function Code: " + str(functionSection) + " (" + str(functionSection.uint)+ ") ")
    
    mtype = ""
    funcCode = ""
    
    if functionSection.uint == 0:
        mtype = "CONFIRM"
        funcCode = "CONFIRMATION"
    elif functionSection.uint == 1:
        mtype = "REQUEST"
        funcCode = "READ"
    elif functionSection.uint == 2:
        mtype = "REQUEST"
        funcCode = "WRITE"
    elif functionSection.uint == 3:
        mtype = "REQUEST"
        funcCode = "SELECT"
    elif functionSection.uint == 4:
        mtype = "REQUEST"
        funcCode = "OPERATE"
    elif functionSection.uint == 5:
        mtype = "REQUEST"
        funcCode = "DIRECT_OPERATE"
    elif functionSection.uint == 6:
        mtype = "REQUEST"
        funcCode = "DIRECT_OPERATE_NORESPONSE"
    elif functionSection.uint == 7:
        mtype = "REQUEST"
        funcCode = "IMMEDIATE_FREEZE"
    elif functionSection.uint == 8:
        mtype = "REQUEST"
        funcCode = "IMMEDIATE_FREEZE_NORESPONSE"
    elif functionSection.uint == 9:
        mtype = "REQUEST"
        funcCode = "FREEZE_CLEAR"
    elif functionSection.uint == 10:
        mtype = "REQUEST"
        funcCode = "FREEZE_CLEAR_NORESPONSE"
    elif functionSection.uint == 11:
        mtype = "REQUEST"
        funcCode = "FREEZE_AT_TIME"
    elif functionSection.uint == 12:
        mtype = "REQUEST"
        funcCode = "FREEZE_AT_TIME_NORESPONSE"
    elif functionSection.uint == 13:
        mtype = "REQUEST"
        funcCode = "COLD_RESTART"
    elif functionSection.uint == 14:
        mtype = "REQUEST"
        funcCode = "WARM_RESTART"
    elif functionSection.uint == 15:
        mtype = "REQUEST"
        funcCode = "INITIALIZE_DATA"
    elif functionSection.uint == 16:
        mtype = "REQUEST"
        funcCode = "INITIALIZE_APPLICATION"
    #there are a lot of these, in the interest of rapid prototyping, I skip to the reponses   
    elif functionSection.uint == 129:
        mtype = "RESPONSE"
        funcCode = "RESPONSE"
    elif functionSection.uint == 130:
        mtype = "RESPONSE"
        funcCode = "UNSOLITED_RESPONSE"
    elif functionSection.uint == 131:
        mtype = "RESPONSE"
        funcCode = "AUTHENTICATE_RESPONSE"
    elif functionSection.uint >= 132:
        mtype = "RESPONSE"
        funcCode = "RESERVED"
        
    print (mtype)
    print (funcCode)
    
    #lsb checking
    first = (binMessage & lsbMask) >> lsbShift
    first = first.uint
    lsb1 = ""
    if first & 1 > 0:
        print ("BroadCast")
        lsb1 += "BroadCast "
    if first & 2 > 0:
        print ("Class 1 Events")
        lsb1 += "Class 1 Events "
    if first & 4 > 0:
        print ("Class 2 Events")
        lsb1 += "Class 2 Events "
    if first & 8 > 0:
        print ("Class 3 Events")
        lsb1 += "Class 3 Events "
    if first & 16 > 0:
        print ("Needs time for synchronization")
        lsb1 += "Needs time for synchronization"
    if first & 32 > 0:
        print ("Local Control Mode")
        lsb1 += "Local Control Mode "
    if first & 64 > 0:
        print ("Device Trouble")
        lsb1 += "Device Trouble "
    if first & 128 > 0:
        print ("Device Restart")
        lsb1 += "Device Restart "
    
    #msb checking
    second = (binMessage & lsbMask) >> msbShift
    second = second.uint
    msb1 = ""
    if second & 1 > 0:
        print ("No function Code Support")
        msb1 += "No function Code Support "
    if second & 2 > 0:
        print ("Object Unknown")
        msb1 += "Object Unknown "
    if second & 4 > 0:
        print ("Parameter Error")
        msb1 += "Parameter Error "
    if second & 8 > 0:
        print ("Event Buffer Overflow")
        msb1 += "Event buffer Overflow "
    if second & 16 > 0:
        print ("Already Executing")
        msb1 += "Already Executing "
    if second & 32 > 0:
        print ("Configuration corrupt")
        msb1 += "Configuration corrupt "
    if second & 64 > 0:
        print ("Reserved (you shouldn't ever get this)")
        msb1 += "Reserved "
    if second & 128 > 0:
        print ("Reserved(2) (you shouldn't ever get this)")
        msb1 += "Reserved(2) "
        
        
        
    
    
    
#base, proof of concept function to decode DNP3 messages
yay = input("Message:")

message = "0X" + str(yay)
dspaced = ""
for i in message:
    if i != " ":
        dspaced += i
DNP3(dspaced)
