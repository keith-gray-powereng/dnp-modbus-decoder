"""File: parseInput.py"""
"""Takes the user's input or specified text file and breaks it down into a list
of the individual messages (whether DNP3 or Modbus) which is then returned.
NOTE: if both input and a specified text file are provided, this module will
attempt to use the textbox input first, but will use the input otherwise."""
from io import StringIO
from string import hexdigits

BAD_INPUT = ""
INVALID = -1


def parseData(data, fileContents):
    try:
        input_stream = _choose_message_from_input_sources(data, fileContents)
    except ValueError:
        return BAD_INPUT

    messages = []
    transmit_message = "True"
    for line in input_stream:
        line = line.replace(' ', '')
        if '0564' in line:
            # this is the start of a DNP message
            start_of_message = line.find('0564')
            if '(' in line[start_of_message:]:
                start_of_crc = line.find('(', start_of_message)
                end_of_crc = line.find(')', start_of_message)
                segment = line[start_of_message:start_of_crc]
                crc = line[start_of_crc + 1:end_of_crc]
            else:
                start_of_crc = len(line[start_of_message:]) - 4
                end_of_crc = len(line[start_of_message:])
                segment = line[start_of_message:start_of_crc + 1]
                crc = line[start_of_crc + 1:end_of_crc]
            if 'TX[' in line:
                messages.append((segment, crc, transmit_message))
            elif 'RX[' in line:
                transmit_message = "False"
                messages.append((segment, crc, transmit_message))
            elif '(' in line:
                messages.append((segment, "True"))
            else:
                messages.append((segment + crc, "True"))
        elif line[0] in hexdigits:
            # this is a continuation of a DNP message
            start_of_message = 0
            start_of_crc = line.find('(', start_of_message)
            end_of_crc = line.find(')', start_of_message)
            segment = line[start_of_message:start_of_crc]
            crc = line[start_of_crc + 1:end_of_crc]
            messages.append((segment, crc, transmit_message))

    return messages


def _choose_message_from_input_sources(text_box_data, file_data):
    ''' Parses the data the user entered into the textbox or specified '
        'via file name.  Also ensures that the data is ready to be decoded.

        :param text_box_data: The data the user entered in the text box area
                              of the input form
        :type text_box_data: str
        :param file_data: The data from the file the user submitted from the
                          input area
        :type file_data: str
        :returns: Data from the text box if it is available. If it isn't
                  available it returns the data from the file. If neither
                  are available, it raises a ValueError exception
        :raises: ValueError

    '''
    if text_box_data != "":
        return StringIO(text_box_data)
    elif file_data != "":
        return StringIO(file_data)
    else:
        raise ValueError(
            'No Data Provided by the user in either the file chooser '
            'or the text box')
