"""AMD-SMI fixture tests; run with PYTHONPATH=src python -m unittest discover -s tests."""
import unittest
from pathlib import Path
from unittest.mock import patch
from diagnostics import hardware

FIXTURE = Path(__file__).parent / 'fixtures' / 'mi300x-amd-smi-static.txt'

class TestAmdGpu(unittest.TestCase):
    def test_mi300x_fixture(self):
        devices = hardware._parse_amd_smi_static(FIXTURE.read_text())
        self.assertEqual(len(devices), 1)
        gpu = devices[0]
        self.assertEqual(gpu['Name'], 'AMD Instinct MI300X VF')
        self.assertEqual(gpu['Architecture'], 'gfx942')
        self.assertEqual(gpu['Memory Total (MB)'], 196288.0)
        self.assertEqual(gpu['PCI Bus ID'], '0000:83:00.0')
        self.assertEqual(gpu['Compute Units'], 304)

    def test_empty_and_malformed(self):
        self.assertEqual(hardware._parse_amd_smi_static(''), [])
        self.assertEqual(hardware._parse_amd_smi_static('GPU: 0\n    ASIC:\n        MARKET_NAME: '), [])

    def test_linux_detects_amd_without_gputil(self):
        with patch.object(hardware.platform, 'system', return_value='Linux'), \
             patch.object(hardware, '_run_command', return_value=FIXTURE.read_text()), \
             patch.object(hardware, 'GPUtil', None):
            result = hardware.get_gpu_info()
        self.assertEqual(result['Status'], 'Detected')
        self.assertEqual(result['Devices'][0]['Architecture'], 'gfx942')

    def test_two_amd_gpus(self):
        text = FIXTURE.read_text()
        second = text.replace('GPU: 0', 'GPU: 1', 1).replace('0000:83:00.0', '0000:84:00.0', 1)
        self.assertEqual(len(hardware._parse_amd_smi_static(text + '\n' + second)), 2)

if __name__ == '__main__':
    unittest.main()
