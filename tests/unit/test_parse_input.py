import logging
import os
import pdb
import sys
import unittest

test_path = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(test_path, '../../DNP3'))
import parseInput


class TestParseInput(unittest.TestCase):
    def test_bad_exit(self):
        'Verifies the function returns an empty string when no data is passed in'
        exit_value = parseInput.parseData('', '')
        self.assertEqual(exit_value, '')

    def test_pasted_tx_message_with_only_message_bytes(self):
        'Verifies the result for a pasted message with no extra characters'
        input_data = '05 64 05 C0 01 00 0A 00 E0 8C'
        output_data = [(input_data.replace(' ', ''), "True")]
        exit_value = parseInput.parseData(input_data, '')
        self.assertEqual(exit_value, output_data)

    def test_pasted_tx_message_with_message_bytes_and_parens_around_crc(self):
        'Verifies the result for a pasted message with parenthesis around the crc bytes'
        input_data = '05 64 05 C0 01 00 0A 00 (E0 8C)'
        output_data = input_data.replace(' ', '')
        paren_location = output_data.find('(')
        expected_output = [(output_data[:paren_location], "True")]
        exit_value = parseInput.parseData(input_data, '')
        self.assertEqual(exit_value, expected_output)

    def test_pasted_tx_message_with_message_bytes_and_parens_around_crc_and_leading_tx(self):
        'Verifies the result for a pasted message with leading TX[xx]: and parenthesis around the crc bytes'
        input_data = 'TX[10]: 05 64 05 C0 01 00 0A 00 (E0 8C)\n'
        output_data = input_data.replace(' ', '')
        open_paren_location = output_data.find('(')
        close_paren_location = output_data.find(')')
        colon_location = output_data.find(':')
        expected_output = [
            (
                output_data[colon_location + 1:open_paren_location],
                output_data[open_paren_location + 1:close_paren_location],
                "True"
            )]
        exit_value = parseInput.parseData(input_data, '')
        self.assertEqual(exit_value, expected_output)

    def test_file_message(self):
        'Verifies the result for a series of messages from a file'
        input_data = (''
            '----------- ** Capture Session Started 02/11/2013 13:20:00 ** ------------\n'
            '(Port 1): Response Timeout for Device 2, waited: 1000\n'
            '(Port 1): Consecutive Failures from Device Device 2: 22\n'
            '(Port 1): Setting All Points for Device Device 2: Offline\n'
            '(Port 1):  \n'
            '(Port 1): Reset Remote Link - Device 2 Address 1 \n'
            '(Port 1)TX[10]: 05 64 05 C0 01 00 0A 00 (E0 8C)-CRC\n'
            '(Port 1): Response Timeout for Device 2, waited: 1000\n'
            '(Port 1): Consecutive Failures from Device Device 2: 23\n'
            '(Port 1): Setting All Points for Device Device 2: Offline\n'
            '(Port 1):  \n'
            '(Port 1): Reset Remote Link - Device 2 Address 1 \n'
            '(Port 1)TX[10]: 05 64 05 C0 01 00 0A 00 (E0 8C)-CRC\n'
            '(Port 1): Response Timeout for Device 2, waited: 1000\n'
            '(Port 1): Consecutive Failures from Device Device 2: 24\n'
            '(Port 1): Setting All Points for Device Device 2: Offline\n'
            '(Port 1):  \n'
            '(Port 1): Reset Remote Link - Device 2 Address 1 \n'
            '(Port 1)TX[10]: 05 64 05 C0 01 00 0A 00 (E0 8C)-CRC\n'
            '(Port 1): Response Timeout for Device 2, waited: 1000\n'
            '(Port 1): Consecutive Failures from Device Device 2: 25\n'
            '(Port 1): Setting All Points for Device Device 2: Offline\n'
            '(Port 1):  \n'
            '(Port 1): Reset Remote Link - Device 2 Address 1 \n'
            '(Port 1)TX[10]: 05 64 05 C0 01 00 0A 00 (E0 8C)-CRC\n'
            '(Port 1): Response Timeout for Device 2, waited: 1000\n'
            '(Port 1): Consecutive Failures from Device Device 2: 26\n'
            '(Port 1): Setting All Points for Device Device 2: Offline\n'
            '(Port 1):  \n'
            '(Port 1): Reset Remote Link - Device 2 Address 1 \n'
            '(Port 1)TX[10]: 05 64 05 C0 01 00 0A 00 (E0 8C)-CRC\n'
            '(Port 1): Response Timeout for Device 2, waited: 1000\n'
            '(Port 1): Consecutive Failures from Device Device 2: 27\n'
            '(Port 1): Setting All Points for Device Device 2: Offline\n'
            '(Port 1):  \n'
            '(Port 1): Reset Remote Link - Device 2 Address 1 \n'
            '(Port 1)TX[10]: 05 64 05 C0 01 00 0A 00 (E0 8C)-CRC\n')
        output_data = input_data.replace(' ', '')
        expected_output = [
            (
                '056405C001000A00',
                'E08C',
                'True'
            ),
            (
                '056405C001000A00',
                'E08C',
                'True'
            ),
            (
                '056405C001000A00',
                'E08C',
                'True'
            ),
            (
                '056405C001000A00',
                'E08C',
                'True'
            ),
            (
                '056405C001000A00',
                'E08C',
                'True'
            ),
            (
                '056405C001000A00',
                'E08C',
                'True'
            )
        ]
        exit_value = parseInput.parseData('', input_data)
        self.assertEqual(exit_value, expected_output)


    def test_pasted_rx_message_with_message_bytes_and_parens_around_crc_and_leading_tx(self):
        'Verifies the result for a pasted message with leading TX[xx]: and parenthesis around the crc bytes'
        input_data = ('RX[17]: 05 64 0A 44 83 00 BF 00 (B1 4A)-CRC\n'
                      'E9 C1 81 00 00 (66 44)\n')
        output_data = input_data.replace(' ', '')
        open_paren_location = output_data.find('(')
        close_paren_location = output_data.find(')')
        colon_location = output_data.find(':')
        expected_output = [
            (
                output_data[colon_location + 1:open_paren_location],
                output_data[open_paren_location + 1:close_paren_location],
                "False"
            ),
            (
                'E9C1810000',
                '6644',
                'False'
            )
        ]
        exit_value = parseInput.parseData(input_data, '')
        self.assertEqual(exit_value, expected_output)

if __name__ == '__main__':
    unittest.main()
