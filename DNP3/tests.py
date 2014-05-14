from django.test import TestCase
from django.test.client import Client

MULTI_RESET_LINK_CONTEXT = '''<ul class="collapsibleList">
<li>
Message 0: Source: 0a00, Destination: 0100, Function: RESET_LINK_STATES (0)
<ul>
<li title="Number of octets this message contains that are not CRC related">
Message length: 5
<li>
Message Control Data: c0
<ul>
<li>
Control Byte: 0xc0
<ul>
<li title="Message Direction">
DIR bit: From Master Station
<li title="Primary message indicator">
PRM bit: Use FCB and FCV for synching
<li title="Frame Count Bit">
FCB bit: False
<li title="Frame Count Valid">
FCV bit: False
<li title="Action for outstation to take with this message">
Function: RESET_LINK_STATES (0)
</ul>
</li>
</ul>
</li>
<li title="ID for sender">
Message Sender: 0a00
<li title="ID for Reciever">
Message Reciever: 0100
</ul>
</li>
<li>
Message 1: Source: 0a00, Destination: 0100, Function: RESET_LINK_STATES (0)
<ul>
<li title="Number of octets this message contains that are not CRC related">
Message length: 5
<li>
Message Control Data: c0
<ul>
<li>
Control Byte: 0xc0
<ul>
<li title="Message Direction">
DIR bit: From Master Station
<li title="Primary message indicator">
PRM bit: Use FCB and FCV for synching
<li title="Frame Count Bit">
FCB bit: False
<li title="Frame Count Valid">
FCV bit: False
<li title="Action for outstation to take with this message">
Function: RESET_LINK_STATES (0)
</ul>
</li>
</ul>
</li>
<li title="ID for sender">
Message Sender: 0a00
<li title="ID for Reciever">
Message Reciever: 0100
</ul>
</li>
<li>
Message 2: Source: 0a00, Destination: 0100, Function: RESET_LINK_STATES (0)
<ul>
<li title="Number of octets this message contains that are not CRC related">
Message length: 5
<li>
Message Control Data: c0
<ul>
<li>
Control Byte: 0xc0
<ul>
<li title="Message Direction">
DIR bit: From Master Station
<li title="Primary message indicator">
PRM bit: Use FCB and FCV for synching
<li title="Frame Count Bit">
FCB bit: False
<li title="Frame Count Valid">
FCV bit: False
<li title="Action for outstation to take with this message">
Function: RESET_LINK_STATES (0)
</ul>
</li>
</ul>
</li>
<li title="ID for sender">
Message Sender: 0a00
<li title="ID for Reciever">
Message Reciever: 0100
</ul>
</li>
<li>
Message 3: Source: 0a00, Destination: 0100, Function: RESET_LINK_STATES (0)
<ul>
<li title="Number of octets this message contains that are not CRC related">
Message length: 5
<li>
Message Control Data: c0
<ul>
<li>
Control Byte: 0xc0
<ul>
<li title="Message Direction">
DIR bit: From Master Station
<li title="Primary message indicator">
PRM bit: Use FCB and FCV for synching
<li title="Frame Count Bit">
FCB bit: False
<li title="Frame Count Valid">
FCV bit: False
<li title="Action for outstation to take with this message">
Function: RESET_LINK_STATES (0)
</ul>
</li>
</ul>
</li>
<li title="ID for sender">
Message Sender: 0a00
<li title="ID for Reciever">
Message Reciever: 0100
</ul>
</li>
<li>
Message 4: Source: 0a00, Destination: 0100, Function: RESET_LINK_STATES (0)
<ul>
<li title="Number of octets this message contains that are not CRC related">
Message length: 5
<li>
Message Control Data: c0
<ul>
<li>
Control Byte: 0xc0
<ul>
<li title="Message Direction">
DIR bit: From Master Station
<li title="Primary message indicator">
PRM bit: Use FCB and FCV for synching
<li title="Frame Count Bit">
FCB bit: False
<li title="Frame Count Valid">
FCV bit: False
<li title="Action for outstation to take with this message">
Function: RESET_LINK_STATES (0)
</ul>
</li>
</ul>
</li>
<li title="ID for sender">
Message Sender: 0a00
<li title="ID for Reciever">
Message Reciever: 0100
</ul>
</li>
<li>
Message 5: Source: 0a00, Destination: 0100, Function: RESET_LINK_STATES (0)
<ul>
<li title="Number of octets this message contains that are not CRC related">
Message length: 5
<li>
Message Control Data: c0
<ul>
<li>
Control Byte: 0xc0
<ul>
<li title="Message Direction">
DIR bit: From Master Station
<li title="Primary message indicator">
PRM bit: Use FCB and FCV for synching
<li title="Frame Count Bit">
FCB bit: False
<li title="Frame Count Valid">
FCV bit: False
<li title="Action for outstation to take with this message">
Function: RESET_LINK_STATES (0)
</ul>
</li>
</ul>
</li>
<li title="ID for sender">
Message Sender: 0a00
<li title="ID for Reciever">
Message Reciever: 0100
</ul>
</li>

</ul>'''


class TestIntegration(TestCase):
    'Run the integration tests'
    def setUp(self):
        self.client = Client()

    def test_single_reset_remote_link(self):
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

    def test_multiple_reset_remote_link(self):
        'Verifies a series of reset remote link messages from a file'
        response = self.client.get(
            '/Power/DNP3/DNP3results/?inputByFile=DNP-OrionLX-Reset-Remote-'
            'Link.log&inputByText=&fileContents=-----------+**+Capture+Session'
            '+Started+02%2F11%2F2013+13%3A20%3A00+**+------------%0D%0A(Port+1'
            ')%3A+Response+Timeout+for+Device+2%2C+waited%3A+1000%0D%0A(Port+1'
            ')%3A+Consecutive+Failures+from+Device+Device+2%3A+22%0D%0A(Port+1'
            ')%3A+Setting+All+Points+for+Device+Device+2%3A+Offline%0D%0A(Port'
            '+1)%3A++%0D%0A(Port+1)%3A+Reset+Remote+Link+-+Device+2+Address+1+'
            '%0D%0A(Port+1)TX[10]%3A+05+64+05+C0+01+00+0A+00+(E0+8C)-CRC%0D%0A'
            '(Port+1)%3A+Response+Timeout+for+Device+2%2C+waited%3A+1000%0D%0A'
            '(Port+1)%3A+Consecutive+Failures+from+Device+Device+2%3A+23%0D%0A'
            '(Port+1)%3A+Setting+All+Points+for+Device+Device+2%3A+Offline%0D%'
            '0A(Port+1)%3A++%0D%0A(Port+1)%3A+Reset+Remote+Link+-+Device+2+'
            'Address+1+%0D%0A(Port+1)TX[10]%3A+05+64+05+C0+01+00+0A+00+(E0+8C)'
            '-CRC%0D%0A(Port+1)%3A+Response+Timeout+for+Device+2%2C+waited%3A+'
            '1000%0D%0A(Port+1)%3A+Consecutive+Failures+from+Device+Device+2%3'
            'A+24%0D%0A(Port+1)%3A+Setting+All+Points+for+Device+Device+2%3A+'
            'Offline%0D%0A(Port+1)%3A++%0D%0A(Port+1)%3A+Reset+Remote+Link+-+'
            'Device+2+Address+1+%0D%0A(Port+1)TX[10]%3A+05+64+05+C0+01+00+0A+'
            '00+(E0+8C)-CRC%0D%0A(Port+1)%3A+Response+Timeout+for+Device+2%2C'
            '+waited%3A+1000%0D%0A(Port+1)%3A+Consecutive+Failures+from+Device'
            '+Device+2%3A+25%0D%0A(Port+1)%3A+Setting+All+Points+for+Device+'
            'Device+2%3A+Offline%0D%0A(Port+1)%3A++%0D%0A(Port+1)%3A+Reset+'
            'Remote+Link+-+Device+2+Address+1+%0D%0A(Port+1)TX[10]%3A+05+64+'
            '05+C0+01+00+0A+00+(E0+8C)-CRC%0D%0A(Port+1)%3A+Response+Timeout+'
            'for+Device+2%2C+waited%3A+1000%0D%0A(Port+1)%3A+Consecutive+'
            'Failures+from+Device+Device+2%3A+26%0D%0A(Port+1)%3A+Setting+All+'
            'Points+for+Device+Device+2%3A+Offline%0D%0A(Port+1)%3A++%0D%0A('
            'Port+1)%3A+Reset+Remote+Link+-+Device+2+Address+1+%0D%0A(Port+1)'
            'TX[10]%3A+05+64+05+C0+01+00+0A+00+(E0+8C)-CRC%0D%0A(Port+1)%3A+'
            'Response+Timeout+for+Device+2%2C+waited%3A+1000%0D%0A(Port+1)%3A+'
            'Consecutive+Failures+from+Device+Device+2%3A+27%0D%0A(Port+1)%3A+'
            'Setting+All+Points+for+Device+Device+2%3A+Offline%0D%0A(Port+1)'
            '%3A++%0D%0A(Port+1)%3A+Reset+Remote+Link+-+Device+2+Address+1+%0D'
            '%0A(Port+1)TX[10]%3A+05+64+05+C0+01+00+0A+00+(E0+8C)-CRC%0D%0A&'
            'printPass=false'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['messages'],
            []
        )
        self.assertEqual(
            response.context['decodedStuff'],
            MULTI_RESET_LINK_CONTEXT
        )
