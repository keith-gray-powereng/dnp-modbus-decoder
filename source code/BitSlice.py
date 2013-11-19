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
    
'''(Application layer) Isolates sequence bits from application layer segment'''    
def getSequence(input):
    #print ("seq")
    return input[4:8]

'''(Application layer) Isolates bit declaring requests for confirmation''' 
def getConfirmationFlag(input):
    #print ("conseq")
    return input[2:3]

'''(Application layer) Isolates bit declaring if request is unsolicited'''     
def getUnsolicitedFlag(input):
    #print ("unsol")
    return input[3:4]

'''(Application layer) Bit declaring if it is the first fragment'''     
def getFirstFlag(input):
    #print ("first")
    return input[0:1]

'''(Application layer) Bit declaring if it is final fragment''' 
def getFinalFlag(input):
    #print ("final")
    return input[1:2]
    
'''(Application layer) Declares what action should be done with data enclosed'''     
def getFuncCode(input):
    #print ("func")
    return input[8:16]
    
#only for responses
'''(Application layer) Part one of Error Codes ''' 
def getLSBInternalIndications(input):
    return slice(input, 4, 16)

'''(Application layer) Part two of Error Codes'''     
def getMSBInternalIndications(input):
    return slice(input, 4, 20)

#seq is the multiple of object parsed, zero indexed
#Object Header = Object Type (group, variation), Qualifier Field, Range Field
#page 63 has basic layouts
def OH_ObjectGroup(input, seq = 0):
    tempIn = bistring.BitArray(input)
    return tempIn[0:8]

    
def OH_ObjectVariation(input, response,  seq = 0):
    tempIn = bistring.BitArray(input)
    return tempIn[8:16]

def OH_Qualifier(input, response, seq = 0):
    tempIn = bistring.BitArray(input)
    #skip the reserved bit
    ObjectPrefix = tempIn[17:20]
    RangeSpecifier = tempIn[20:24] 
    
    typed = ""
    size = 0
    if ObjectPrefix.uint == 0:
        typed = "No Prefix"
        size = 0
    elif ObjectPrefix.uint == 1:
        typed = "index"
        size = 1
    elif ObjectPrefix.uint == 2:
        typed = "index"
        size = 2
    elif ObjectPrefix.uint == 3:
        typed = "index"
        size = 3
    elif ObjectPrefix.uint == 4:
        typed = "size"
        size = 1
    elif ObjectPrefix.uint == 5:
        typed = "size"
        size = 2
    elif ObjectPrefix.uint == 6:
        typed = "size"
        size = 3
    else:
        typed = "RESERVED"
        size = 0
    
    indexed = ""
    indexSize = 0
    if RangeSpecifier.uint == 0:
        indexed = "start-stopped"
        indexSize = 2
    elif RangeSpecifier.uint == 1:
        indexed = "start-stopped"
        indexSize = 4
    elif RangeSpecifier.uint == 2:
        indexed = "start-stopped"
        indexSize = 8
    elif RangeSpecifier.uint == 3:
        indexed = "start-stopped Virtual"
        indexSize = 2
    elif RangeSpecifier.uint == 4:
        indexed = "start-stopped Virtual"
        indexSize = 4
    elif RangeSpecifier.uint == 5:
        indexed = "start-stopped Virtual"
        indexSize = 8
    elif RangeSpecifier.uint == 6:
        indexed = "All Objects (no range)"
        indexSize = 0
    elif RangeSpecifier.uint == 7:
        indexed = "ObjectCount"
        indexSize = 1
    elif RangeSpecifier.uint == 8:
        indexed = "ObjectCount"
        indexSize = 2
    elif RangeSpecifier.uint == 9:
        indexed = "ObjectCount"
        indexSize = 4
    elif RangeSpecifier.uint == 11:
        indexed = "Object Specified"
        indexSize = 0
    else:
        indexed = "RESERVED"
        indexSize = 0
        
    return (typed, size, indexed, indexSize)
    


