#Bit-Slice.py

import bitstring

#startBit must be a bitstring, preferrably a BitArray
def slice(input,length, startBit):
    
    #generate "length" filter
    filter = bitstring.BitArray(length=64)
    bitFilter = ""
    for i in range(0, length):
        bitFilter += "1"
    bitFilter = "0b" + bitFilter
    
    if len(bitFilter) == 2:
        bitFilter = bitFilter + "0"
    
    filter.overwrite(bitFilter, startBit)
    filter.reverse()
    
    print (filter)
    print (input)
    
    return (filter & input) >> startBit
    
    
def getSequence(input):
    print ("seq")
    return slice(input, 3, 1)    
    
def getConsequtiveFlag(input):
    print ("conseq")
    return slice(input,1, 5)
    
def getUnsolicitedFlag(input):
    print ("unsol")
    return slice(input, 1, 4)
    
def getFirstFlag(input):
    print ("first")
    return slice(input, 1, 6)

def getFinalFlag(input):
    print ("final")
    return slice(input, 1, 7)
    
def getFuncCode(input):
    print ("func")
    return slice(input, 8,8)