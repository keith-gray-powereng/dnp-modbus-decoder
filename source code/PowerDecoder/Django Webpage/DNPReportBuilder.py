from Report import Report
import DataLinkTranslator


class DNPReportBuilder:
    def __init__(self):
        self.out = Report("Message", "", "")
    
    '''Translates message into a displayable report
    I am expecting "message" to be a list of hex numbers, preferrably strings'''
    def translate(self, message):
        # data link layer is first
        #it will be chunk 0 
        
        #verify correctness
        if not DataLinkTranslator.DataLayerCorrect(message[0]):
            self.out.AddNext(Report("ERROR", "This message is not verifyably DNP3, or may be malformed", message[0]))
            break
        
        #remove CRC bits for everything
        for i in message:
            i = DataLinkTranslator.StripCRCBits(i)
        
        #Get message length
        self.length = DataLinkTranslator.DataLayerLength(message[0][:])
        self.MessageLength = self.length.uint
        self.out.AddNext(Report("Message length", "Number of octets this message contains that are not CRC related", string(self.length.uint)))
        
        #Get Control Field
        control = DataLinkTranslator.DataLayerControl(message[0][:])
        self.out.AddNext(Report("Message Control Data", "Function opertaions and qualifiers", string(control.hex)))
        #todo: break into specific parts, lookup function
        
        #message sender
        self.sender = DataLinkTranslator.DataLayerSource(message[0][:])
        self.out.AddNext(Report("Message Sender", "ID for sender", string (self.sender.hex)))
        
        #message reciever
        self.reciever = DataLinkTranslator.DataLayerDestination(message[0][:])
        self.out.AddNext(Report("Message Reciever", "ID for Reciever", string(self.reciever)))
        
        fragment = 1
        while fragment < len(message) :
            #transport function
            
            #actual app message translation
            
        return self.out
        
            