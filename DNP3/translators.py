#translators.py
from .BitSlice import getSequence
from .BitSlice import getConfirmationFlag
from .BitSlice import getUnsolicitedFlag
from .BitSlice import getFirstFlag
from .BitSlice import getFinalFlag
from .BitSlice import getLSBInternalIndications
from .BitSlice import getMSBInternalIndications
from .Report import Report


def getAppRequestHeader(fragment):
    summary = []
    summary.append(Report("Sequence number", "", getSequence(fragment).uint))
    summary.append(Report(
        "Final Flag", "Last Fragment", getFinalFlag(fragment).uint == 1))
    summary.append(Report(
        "First Flag", "First Fragment", getFirstFlag(fragment).uint == 1))
    summary.append(Report(
        "Unsolicited",
        "This information was not part of a request",
        getUnsolicitedFlag(fragment).uint == 1)
    )
    summary.append(Report(
        "Confirmation Required",
        "Opposite station must acknowledge to be valid",
        getConfirmationFlag(fragment).uint == 1)
    )
    return summary


def getAppResponseHeader(fragment):
    InternalIndications = []
    InternalIndications.append(Report(
        "Internal Indications 1 {}".format(
            LSBinternalIndicationLookup(
                getLSBInternalIndications(fragment)[:8])),
        "Block used for response Error codes, first part (LSB)",
        getLSBInternalIndications(fragment))
    )
    InternalIndications.append(Report(
        "Internal Indications 2 {}".format(
            LSBinternalIndicationLookup(
                getMSBInternalIndications(fragment)[8:16])),
        "Block used for response Error codes, first part (LSB)",
        getMSBInternalIndications(fragment))
    )

    temp = getAppRequestHeader(fragment)
    temp.append(Report(
        "Internal Indicators", "Errors for responses go here", None))
    temp[-1].AddNext(InternalIndications)
    return temp

def translateFuncCode(functionSection):

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
    elif functionSection.uint > 17 and functionSection.uint < 128:
        mtype = "REQUEST"
        funcCode = "RESERVED"
    #there are a lot of these, in the interest of rapid prototyping,
    #I skip to the reponses
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

    return Report(
        "Function", "action for message", "Function: {} ({})".format(
            funcCode, mtype)
    )

def LSBinternalIndicationLookup(fragment):
    lsb1 = ""
    if fragment.uint == 1:
        #print ("BroadCast")
        lsb1 += "BroadCast "
    if fragment.uint == 2:
        #print ("Class 1 Events")
        lsb1 += "Class 1 Events "
    if fragment.uint == 4:
        #print ("Class 2 Events")
        lsb1 += "Class 2 Events "
    if fragment.uint == 8:
        #print ("Class 3 Events")
        lsb1 += "Class 3 Events "
    if fragment.uint == 16:
        #print ("Needs time for synchronization")
        lsb1 += "Needs time for synchronization"
    if fragment.uint == 32:
        #print ("Local Control Mode")
        lsb1 += "Local Control Mode "
    if fragment.uint == 64:
        #print ("Device Trouble")
        lsb1 += "Device Trouble "
    if fragment.uint == 128:
        #print ("Device Restart")
        lsb1 += "Device Restart "

    return lsb1

def MSBinternalIndicationLookup(fragment):
    msb1 = ""
    if fragment.uint == 1:
        #print ("No function Code Support")
        msb1 += "No function Code Support "
    if fragment.uint == 2:
        #print ("Object Unknown")
        msb1 += "Object Unknown "
    if fragment.uint == 4:
        #print ("Parameter Error")
        msb1 += "Parameter Error "
    if fragment.uint == 8:
        #print ("Event Buffer Overflow")
        msb1 += "Event buffer Overflow "
    if fragment.uint == 16:
        #print ("Already Executing")
        msb1 += "Already Executing "
    if fragment.uint == 32:
        #print ("Configuration corrupt")
        msb1 += "Configuration corrupt "
    if fragment.uint == 64:
        #print ("Reserved (you shouldn't ever get this)")
        msb1 += "Reserved "
    if fragment.uint == 128:
        #print ("Reserved(2) (you shouldn't ever get this)")
        msb1 += "Reserved(2) "

    return msb1
