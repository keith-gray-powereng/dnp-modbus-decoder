"""File: parseInput.py"""
"""Takes the user's input or specified text file and breaks it down into a list
of the individual messages (whether DNP3 or Modbus) which is then returned.
NOTE: if both input and a specified text file are provided, this module will
attempt to use the textbox input first, but will use the input otherwise."""
from string import hexdigits

badExit = "" #what to return if bad file name
INVALID = -1

def parseData(data, fileContents):
	"""Parses the data the user entered into the textbox or specified via file name.
	Also ensures that the data is ready to be decoded."""	
	msg = ""
	if data != "": #first try to use the data from the textbox (because the input file box auto-loads a value) 
		msg = data
	elif fileContents != "": #if the textbox is empty then go with the data in the textbox
		msg = fileContents
	else: #if neither condition was met, then no input was entered, so return a bad value
		return badExit
	
	i = 0
	j = 0
	bytes = 0
	byteCount = 0
	gotCrc = True
	messages = [] #Message type? #Use two indexes per message, first=message, second=CRC (or nothing if no CRC given)
	#First tries to parse the input as if it were setup like a normal capture file log.
	while i < len(msg)-2 and i != INVALID: #iterating through msg to find each message and CRC codes
		i = msg.find("X", i) + 1
		if i == INVALID+1:
			break
		elif i != (INVALID+1) and msg[i] == "[": # or msg[i:i+2] == "X:": #looking for TX[/RX[ or TX:/RX:
			c = "" #temporary crc
			m = "" #temporary msg
			bytes = int(msg[i+1:(msg.find("]", i))]) * 2
			byteCount = 0
			i = msg.find(":", i) + 1
			while i < len(msg) and byteCount < bytes:
				if msg[i] == "(":
					#start getting CRC
					i += 1
					while i < len(msg) and msg[i] != ")":#CRC ends with )
						if msg[i] != " ":
							c += msg[i]
							byteCount += 1
						i += 1
					
					messages.append( (m, c) )
					m = ""
					c = ""
					i = msg.find("\n", i) + 1
					if i == 0:
						break
				elif msg[i] != " " and msg[i] != "\n":
					byteCount += 1
					m += msg[i]
					i += 1
				else:
					i += 1
			#end while (msg)
			if m != "":
				messages.append( (m,c) ) #pushing message and crc as a tuple
		#end if
	#end while
	
	#If log-file parsing failed, try normal message input parsing instead
	if len(messages) == 0:
		c = "" #temporary crc
		m = "" #temporary msg
		seperator_chars = ['-', '/', '_', '(']
		nxt_msg_chars = ['\n', '\r', ',']
		status = 'm'
		for letter in msg:
			if letter in hexdigits: #if the current letter is a hex digit, it adds it to 'c' or 'm'
				if status == 'm': #add to message
					m += letter
				else: #add to crc
					c += letter
			elif letter in seperator_chars: #if it's a seperator, it ends current message, begins reading crc
				status = 'c'
			elif letter in nxt_msg_chars: #ends current message or crc and begins next message
				if m == "" and c == "":
					continue #if both m and c are empty, doesn't add either to messages
				messages.append( (m,c) )
				m = ""
				c = ""
				status = 'm'
			else: #if whitespace or other character, it's ignored
				continue
				
		if m != "":
			messages.append( (m,c) )
			
	return messages
