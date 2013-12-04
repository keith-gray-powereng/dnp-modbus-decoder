from Report import Report
import DataLinkTranslator
from bitstring import BitArray


class DNPReportBuilder:

    def dummyData(self):
        return ["05 64 12 C4 02 00 64 00 FF B7", "F8 C8 05 29 02 28 01 00 10 00 00 80 00 E8 57", "05 64 14 44 64 00 02 00 A4 D8", "F1 C8 81 00 00 29 02 28 01 00 10 00 00 80 00 7E 25"]
    
    def __init__(self):
        self.out = Report("Message", "", "")
    
    '''Translates message into a displayable report
    I am expecting "message" to be a list of hex numbers, preferrably strings'''
    def translate(self, message):
        # data link layer is first
        #it will be chunk 0 
        
        hexMessage = []
        #turn into bitstrings
        for i in message:
            hexMessage.append(BitArray(hex = i.replace(" ", "")))
        
        #verify correctness
        if not DataLinkTranslator.DataLayerCorrect(hexMessage[0]):
            self.out.AddNext(Report("ERROR", "This message is not verifyably DNP3, or may be malformed", message[0]))
            return
        
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
        
        fragment = 1
        while fragment < len(hexMessage) :
            #transport function
            
            #actual app message translation
            fragment += 1
            
        return self.out
        

            