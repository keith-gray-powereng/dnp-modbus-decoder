
#a basic message to get us started
#05 64 05 C0 01 00 0A 00

#bitstring is a dependency of python in order for this to work
#https://code.google.com/p/python-bitstring/
import bitstring

#application header mask (bits must be reversed
appMask = bitstring.Bits("0x000000000000000F")
seqMask = bitstring.Bits("0x000000000000000E")
seqShift = 0
consecutiveMask = bitstring.Bits("0x0000000000000020")
consecutiveShift = 5
unsolicitedMask = bitstring.Bits("0x0000000000000010")
unsolicitedShift = 5
firstMask = bitstring.Bits("0x0000000000000040")
firstShift = 6
finalMask = bitstring.Bits("0x0000000000000080")
finalShift = 7


#function code masks
#81 through 83 (hex) indicates response
funcCodeMask = bitstring.Bits("0x000000000000FF00")
funcCodeShift = 9

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
    
    print ("binary:")
    print (binMessage.bin)
    binMessage = binMessage[::-1]
    print (binMessage.bin)
    
    print ("DNP3 --- MESSAGE BEGIN -----")
    print(str(len(binMessage)) + " " + str(len(seqMask)))
    print ("NumMessage " + str(numMessage))
    #print ("seqMessage:" + str(int(seqMask,16)))
    seqValue = (binMessage & seqMask) >> seqShift
    consecutiveValue = (binMessage & consecutiveMask) >> consecutiveShift
    unsolicitedValue = (binMessage & unsolicitedMask) >> unsolicitedShift
    firstValue = (binMessage & firstMask) >> firstShift
    finalValue = (binMessage & finalMask) >>finalShift
    
    print("seqValue: " + str(seqValue))
    print("consecutive: " + str(consecutiveValue))
    print("unsolicited: " + str(unsolicitedValue))
    print("firstValue: " + str(firstValue))
    print("finalValue: " + str(finalValue))
    
    #function code parsing
    functionSection = (binMessage & funcCodeMask) >> funcCodeShift
    print("function Code: " + str(functionSection))
    
    #lsb checking
    first = (binMessage & lsbMask) >> lsbShift
    first = first.uint
    if first & 1 > 0:
        print ("BroadCast")
    if first & 2 > 0:
        print ("Class 1 Events")
    if first & 4 > 0:
        print ("Class 2 Events")
    if first & 8 > 0:
        print ("Class 3 Events")
    if first & 16 > 0:
        print ("Needs time for synchronization")
    if first & 32 > 0:
        print ("Local Control")
    if first & 64 > 0:
        print ("Device Trouble")
    if first & 128 > 0:
        print ("Device Restart")
    
    #msb checking
    second = (binMessage & lsbMask) >> msbShift
    second = second.uint
    if second & 1 > 0:
        print ("No function Code Support")
    if second & 2 > 0:
        print ("Object Unknown")
    if second & 4 > 0:
        print ("Parameter Error")
    if second & 8 > 0:
        print ("Event Buffer Overflow")
    if second & 16 > 0:
        print ("Already Executing")
    if second & 32 > 0:
        print ("Configuration corrupt")
    if second & 64 > 0:
        print ("Reserved (you shouldn't ever get this)")
    if second & 128 > 0:
        print ("Reserved(2) (you shouldn't ever get this)")
        
    
    
    
#base, proof of concept function to decode DNP3 messages
yay = input("Message:")

message = "0X" + str(yay)
dspaced = ""
for i in message:
    if i != " ":
        dspaced += i
DNP3(dspaced)
