'''
CLI Interface tests
===================
'''

from unittest import TestCase

from htmlit.__main__ import parse_options


class TestCLIInvocation(TestCase):
    """ Tests the command line invocation of FAF Markdown."""
    def setUp(self):
        """ Creates an instance of subprocess."""
        self.default_options = {
            'input_file_path': None,
            'output_path': '~/markdown/outputs',
            'input_url': None,
        }

    def testNoOptions(self):
        markdown_options = parse_options()
        self.assertEqual(markdown_options, self.default_options)

    def testGivenInputFilePathOnly(self):
        _input = 'test.md'
        markdown_options = parse_options(input=_input)
        correct_options = {
            'input_file_path': 'test.md',
            'output_path': '~/markdown/outputs',
            'input_url': None,
        }
        self.assertEqual(markdown_options, correct_options)

    def testGivenInputUrlOnly(self):
        _input = 'http://example.com/markdown/input.md'
        markdown_options = parse_options(input=_input)
        correct_options = {
            'input_file_path': None,
            'output_path': '~/markdown/outputs',
            'input_url': 'http://example.com/markdown/input.md',
        }
        self.assertEqual(markdown_options, correct_options)
