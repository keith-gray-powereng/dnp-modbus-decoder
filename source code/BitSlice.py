#BitSlice.py

import bitstring

#startBit must be a bitstring, preferrably a BitArray
'''slice gets the bits specified by counting from the least signifigant bit, as this is sometimes easier
for starting from msb, use bistring slice ([]) notation'''
def slice(input,length, startBit):
    
    #generate "length" filter
    filter = bitstring.BitArray(length=len(input))
    bitFilter = ""
    for i in range(0, length):
        bitFilter += "1"
    bitFilter = "0b" + bitFilter
    
    if len(bitFilter) == 2:
        bitFilter = bitFilter + "0"
    
    filter.overwrite(bitFilter, startBit)
    filter.reverse()
    
    #print (filter)
    #print (input)
    
    return (filter & input) >> startBit
    
    
def getSequence(input):
    #print ("seq")
    return slice(input, 4, 1)    
    
def getConsequtiveFlag(input):
    #print ("conseq")
    return slice(input,1, 5)
    
def getUnsolicitedFlag(input):
    #print ("unsol")
    return slice(input, 1, 4)
    
def getFirstFlag(input):
    #print ("first")
    return slice(input, 1, 6)

def getFinalFlag(input):
    #print ("final")
    return slice(input, 1, 7)
    
def getFuncCode(input):
    #print ("func")
    return slice(input, 8,8)
    
#only for responses
def getLSBInternalIndications(input):
    return slice(input, 4, 16)
    
def getMSBInternalIndications(input):
    return slice(input, 4, 20)
    
#everything after will need to take a 16 bit displacement if it is a response, and if it isn't, not.

#seq is the multiple of object parsed, zero indexed
#Object Header = Object Type (group, variation), Qualifier Field, Range Field
def OH_ObjectGroup(input, response, seq = 0):
    if input:
        return slice(input, 8, 32 + seq * 8)
    else:
        return slice(input, 8, 16 + seq * 8)
    
def OH_ObjectVariation(input, response,  seq = 0):
    if input:
        return slice(input, 8, 40 + seq * 8)
    else:
        return slice(input, 8, 24 + seq * 8)

def OH_Qualifier(input, response, seq = 0):
    #is an octet (pg 74 (32))
    #the object Prefix code defined here is REALLY important: it determines how future parts are parsed, also constains range specifier and object prefix
    #contains a Range specifier code (4), a Object prefix code(3), and a 0 bit (reserved)
    pass
    
# I'm going to re-evaluate what is going on, as this gets hella complicated
#each DNP object parses differntly
#data type codes can be found on page 170, and can be defined further in that section

