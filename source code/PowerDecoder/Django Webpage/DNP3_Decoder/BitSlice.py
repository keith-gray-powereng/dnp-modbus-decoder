#Bit-Slice.py

import bitstring

#startBit must be a bitstring, preferrably a BitArray
def slice(input, startBit, length):
    
    #generate "length" filter
    filter = ""
    for i in range(0,length):
        filter += "1"
        
    #generate padding bits
    for i in range(0, 63):
        if i - 1 >= startBit and (start - 1  + length) > i:
            pass
        elif  i < startBit:
            filter = filter + "0"
        else:
            filter = "0" + filter
            
    #convert to bitstring
    num = bitstring.Bits(bin = filter)
    
    #convert
    word = bitstring.BitArray(input)
    result = (word & num) >> startBit
    
    
    return result
    
def getSequence(input):
    return slice(input,1, 3)    
    
def getConsequtiveFlag(input):
    return slice(input,1, 5)
    
def getUnsolicitedFlag(input):
    return slice(input, 1, 4)
    
def getFirstFlag(input):
    return slice(input, 1, 6)

def getFinalFlag(input):
    return slice(input, 1, 7)
    
def getFuncCode(input):
    return slice(input, 8,8)