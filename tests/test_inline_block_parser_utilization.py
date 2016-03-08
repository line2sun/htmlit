"""
Inline Block Parser objects utilization tests.
"""

from unittest import TestCase


from htmlit.blocks import Block
from htmlit.html_tags import Paragraph
from htmlit.parsers.block_parsers import InlineBlockParser


class TestInlineBlockParserUsage(TestCase):
    def setUp(self):
        self.inline_parser = InlineBlockParser()

    def test_string_input(self):
        md = u'This is a **bold** text.'
        self.assertRaises(ValueError, self.inline_parser.parse, _input=md)

    def test_invalid_input(self):
        _input = [2234, 44, 'test', 'fails']
        with self.assertRaises(ValueError) as ve:
            self.inline_parser.parse(_input)
        self.assertTrue(ve)

    def test_returns_a_block_instance(self):
        block = Block('test')
        block.set_html_tag(Paragraph())
        self.assertIsInstance(self.inline_parser.parse(block), Block)

    # def test_initialization_without_params(self):
    #     block = Block()
    #     self.