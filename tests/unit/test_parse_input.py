import logging
import os
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

    def test_pasted_message_with_only_message_bytes(self):
        'Verifies the result for a pasted message with no extra characters'
        input_data = '05 64 05 C0 01 00 0A 00 E0 8C'
        output_data = [(input_data.replace(' ', ''), "True")]
        exit_value = parseInput.parseData(input_data, '')
        self.assertEqual(exit_value, output_data)

if __name__ == '__main__':
    unittest.main()
