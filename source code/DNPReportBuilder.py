from Report import Report
import DataLinkTranslator
from bitstring import BitArray
from BitSlice import *
from translators import *


class DNPReportBuilder:

    def dummyData(self):
        return ["05 64 12 C4 02 00 64 00 FF B7", "F8 C8 05 29 02 28 01 00 10 00 00 80 00 E8 57", "05 64 14 44 64 00 02 00 A4 D8", "F1 C8 81 00 00 29 02 28 01 00 10 00 00 80 00 7E 25"]
    
    def __init__(self):
        self.out = Report("Message", "", "")
    
    '''Translates message into a displayable report
    I am expecting "message" to be a list of hex numbers, preferrably strings'''
    def translate(self, message, request):

        hexMessageIN = []
        #turn into bitstrings
        for i in message:
            value = BitArray(hex = i.replace(" ", ""))
            hexMessageIN.append(value)
            
           
        #detect multiple messages
        hexMessages = []
        temp = []
        for i in hexMessageIN:
            print (i[0:16].hex)
            if i[0:16].hex == BitArray("0x0564").hex:
                if len(temp) > 0:
                    hexMessages.append(list(temp))
                temp = []
            temp.append(i)
        if len(temp) > 0:
            hexMessages.append(list(temp))
           
        allMessages = Report("All Messages", "The entirity of the message", "", "")
        messageCount = -1
        index = -1
        for hexMessage in hexMessages:
            index += 1
            messageCount += 1
            hexString = ""
            for msg in hexMessage:
                hexString += msg.hex + ', '
            thisMessage = Report("Message {}".format(messageCount), "", "", hexString)
                       
            #verify correctness
            try:
                if not DataLinkTranslator.DataLayerCorrect(hexMessage[0]):
                    thisMessage.AddNext(Report("ERROR", "This message is not verifyably DNP3, or may be malformed", message[0]), "")
                    return Report("Invalid Message", "", "", "")
            except:
                return Report("Invalid Input", "", "", "")
                
            #remove CRC bits for everything
            for i in hexMessage:
                i = DataLinkTranslator.StripCRCBits(i)
            
            #Get message length
            thisMessage.length = DataLinkTranslator.DataLayerLength(hexMessage[0][:])
            thisMessage.MessageLength = thisMessage.length.uint
            thisMessage.AddNext(Report("Message length", "Number of octets this message contains that are not CRC related", str(thisMessage.length.uint), ""))
            
            #Get Control Field
            control = DataLinkTranslator.DataLayerControl(hexMessage[0][:])
            thisMessage.AddNext(Report("Message Control Data", "Function operations and qualifiers", str(control.hex), ""))
            thisMessage.Next[-1].AddNext(DataLinkTranslator.DataLayerControlReport(control))
            
            #message sender
            thisMessage.sender = DataLinkTranslator.DataLayerSource(hexMessage[0][:])
            thisMessage.AddNext(Report("Message Sender", "ID for sender", str (thisMessage.sender.hex), ""))
            
            #message reciever
            thisMessage.reciever = DataLinkTranslator.DataLayerDestination(hexMessage[0][:])
            thisMessage.AddNext(Report("Message Reciever", "ID for Reciever", str(thisMessage.reciever.hex), ""))
            
            #message transport layer
            thisMessage.transport = ""
            if hexMessage[1][0]:
                thisMessage.transport += " FINAL "
            if hexMessage[1][1]:
                thisMessage.transport += " FIRST "
            thisMessage.AddNext(Report("Transport Function", "Links together large messages in sequence", (thisMessage.transport + "Seq {}").format(hexMessage[1][2:8].uint), ""))
            hexMessage[1] = hexMessage[1][8:]
            
            #technically a block, so sue me
            fragment = 1
            baseLayer = thisMessage
            while fragment < len(hexMessage) :
            
                bucket = []
                #requests contain no actual data
                #just outlines for what is expected in responses
                if request[index]:
                    bucket.append(Report("Object Header", "Prefix information on Application layer", "", ""))
                    flags = getAppRequestHeader(hexMessage[fragment])
                    for i in flags:
                        bucket[-1].Next.append(i)
                    bucket.append(translateFuncCode(getFuncCode(hexMessage[fragment])))
                    #skip internal indications, does not exist in requests
                    
                for i in bucket:
                    temp = i
                    if not isinstance(i, Report):
                        temp = Report(i,"","","")
                    baseLayer.Next[-1].AddNext(temp)
                    
                baseLayer.AddNext(Report("Application Fragment {}".format(fragment -1), "", "", ""))
                    
                fragment += 1
                
            allMessages.AddNext(thisMessage)
               
        print (allMessages)
        return allMessages
        
        #http://www.kepware.com/Support_Center/SupportDocuments/DNP3_Control_Relay_Output_Block.pdf

        
        
            