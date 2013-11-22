#translators.py
from BitSlice import *
from Report import Report

def getAppRequestHeader(fragment):
    summary = []
    summary.append(Report("Sequence number", "", getSequence(fragment).uint))
    summary.append(Report("Final Flag" , "Last Fragment", getFinalFlag(fragment).uint == 1))
    summary.append(Report("First Flag", "First Fragment", getFirstFlag(fragment).uint == 1))
    summary.append(Report("Unsolicited", "This information was not part of a request", getUnsolicitedFlag(fragment).uint == 1))
    summary.append(Report("Confirmation Required", "Opposite station must acknowledge to be valid", getConfirmationFlag(fragment).uint == 1))
    return summary
    
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
        
        
    return Report("Function", "action for message", "Function: {} ({})".format(funcCode,mtype))