from Report import Report
import DataLinkTranslator
from bitstring import BitArray
from BitSlice import *
from translators import *


class DNPReportBuilder:

    def dummyData(self):
        return ["05 64 12 C4 02 00 64 00 FF B7", "F8 C8 05 29 02 28 01 00 10 00 00 80 00 E8 57"]
    
    def __init__(self):
        self.out = Report("Message", "", "")
    
    '''Translates message into a displayable report
    I am expecting "message" to be a list of hex numbers, preferrably strings'''
    def translate(self, message, request):
        # data link layer is first
        #it will be chunk 0 
        
        hexMessage = []
        #turn into bitstrings
        for i in message:
            value = BitArray(hex = i.replace(" ", ""))
            hexMessage.append(value)
            
            
        for i in hexMessage:
            print (i)
        
        #verify correctness
        if not DataLinkTranslator.DataLayerCorrect(hexMessage[0]):
            self.out.AddNext(Report("ERROR", "This message is not verifyably DNP3, or may be malformed", message[0]))
            return Report("Invalid Message", "", "")
        
        #remove CRC bits for everything
        for i in hexMessage:
            i = DataLinkTranslator.StripCRCBits(i)
        
        #Get message length
        self.length = DataLinkTranslator.DataLayerLength(hexMessage[0][:])
        self.MessageLength = self.length.uint
        self.out.AddNext(Report("Message length", "Number of octets this message contains that are not CRC related", str(self.length.uint)))
        
        #Get Control Field
        control = DataLinkTranslator.DataLayerControl(hexMessage[0][:])
        self.out.AddNext(Report("Message Control Data", "Function opertaions and qualifiers", str(control.hex)))
        #todo: break into specific parts, lookup function
        
        #message sender
        self.sender = DataLinkTranslator.DataLayerSource(hexMessage[0][:])
        self.out.AddNext(Report("Message Sender", "ID for sender", str (self.sender.hex)))
        
        #message reciever
        self.reciever = DataLinkTranslator.DataLayerDestination(hexMessage[0][:])
        self.out.AddNext(Report("Message Reciever", "ID for Reciever", str(self.reciever.hex)))
        
        #you failed to strip the transport layer, Westin.
        #you failed to strip the transport layer, Westin.
        
        
        fragment = 1
        baseLayer = self.out
        while fragment < len(hexMessage) :
            bucket = []
            #requests contain no actual data
            #just outlines for what is expected in responses
            if request:
                bucket.append(Report("Object Header", "Prefix information on Application layer", ""))
                flags = getAppRequestHeader(hexMessage[fragment])
                for i in flags:
                    bucket[-1].Next.append(i)
                bucket.append(translateFuncCode(getFuncCode(hexMessage[fragment])))
                #skip internal indications
                
            
            baseLayer.AddNext(Report("Application Fragment {}".format(fragment -1), "", ""))
            for i in bucket:
                temp = i
                if not isinstance(i, Report):
                    temp = Report(i,"","")
                baseLayer.Next[-1].AddNext(temp)
                
            fragment += 1
           
        print (self.out)
        return self.out
        
        #http://www.kepware.com/Support_Center/SupportDocuments/DNP3_Control_Relay_Output_Block.pdf

        
        
            