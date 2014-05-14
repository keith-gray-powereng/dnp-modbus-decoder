from django.test import TestCase
from django.test.client import Client


class TestIntegration(TestCase):
    'Run the integration tests'
    def setUp(self):
        self.client = Client()

    def test_reset_remote_link(self):
        'Verifies a Reset Remote Link Message entered in the text area'
        response = self.client.get(
            '/Power/DNP3/DNP3results/?inputByFile=&inputByText=05+64+05+C0+01+'
            '00+0A+00+(E0+8C)&fileContents=&printPass=false'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['messages'],
            []
        )
        self.assertEqual(
            response.context['decodedStuff'],
            '<ul class="collapsibleList">\n<li>\nMessage '
            '0: Source: 0a00, Destination: 0100, Function:'
            ' RESET_LINK_STATES (0)\n<ul>\n<li title="'
            'Number of octets this message contains that '
            'are not CRC related">\nMessage length: 5\n'
            '<li>\nMessage Control Data: c0\n<ul>\n<li>\n'
            'Control Byte: 0xc0\n<ul>\n<li title="Message '
            'Direction">\nDIR bit: From Master Station\n'
            '<li title="Primary message indicator">\nPRM '
            'bit: Use FCB and FCV for synching\n<li '
            'title="Frame Count Bit">\nFCB bit: False\n'
            '<li title="Frame Count Valid">\nFCV bit: '
            'False\n<li title="Action for outstation to '
            'take with this message">\nFunction: '
            'RESET_LINK_STATES (0)\n</ul>\n</li>\n</ul>\n'
            '</li>\n<li title="ID for sender">\nMessage '
            'Sender: 0a00\n<li title="ID for Reciever">\n'
            'Message Reciever: 0100\n</ul>\n</li>\n\n</ul>'
        )
