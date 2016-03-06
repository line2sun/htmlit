from unittest import TestCase

from htmlit.blocks import Block
from htmlit.html_tags import Paragraph


class TestBlockImplementation(TestCase):
    # Testing __init__() method.
    def test_instantiation_with_no_args(self):
        b = Block()
        self.assertEqual([b.data, b.inline_blocks, b.html_tag], [None, [], None])

    def test_instantiation_with_a_string(self):
        _input = 'a whatever string'
        b = Block(_input=_input)
        self.assertEqual([b.data, b.inline_blocks, b.html_tag], [_input, [], None])

    def test_instantiation_with_another_block_instance(self):
        b1 = Block('test_instantiation_with_another_block_instance')
        b2 = Block(_input=b1)
        self.assertEqual([b2.data, b2.html_tag, b2.inline_blocks], [b1.data, b1.html_tag, b1.inline_blocks])

    def test_instantiation_with_nonvalid_data(self):
        _input = 222222
        self.assertRaises(ValueError, Block, _input=_input)

    def test_output_with_no_inline_blocks(self):
        b = Block('Banana')
        b.set_html_tag(Paragraph())
        self.assertEqual(b.to_str(), '<p>Banana</p>')

    def test_output_with_no_html_tag_setted(self):
        b = Block('Vaniusha')
        self.assertRaises(AttributeError, b.to_str)

    def test_output_with_inline_blocks(self):
        b = Block('kkk %s - %s')
        b.set_html_tag(_tag=Paragraph())

        b1 = Block('b1')
        b1.set_html_tag(Paragraph())

        b2 = Block('b2 %s --> %s')
        b2.set_html_tag(Paragraph())

        b3 = Block('b3')
        b3.set_html_tag(Paragraph())

        b4 = Block('b4')
        b4.set_html_tag(Paragraph())

        b2.inline_blocks = [b3, b4]

        b.inline_blocks = [b1, b2]

        self.assertEqual(b.to_str(), '<p>kkk <p>b1</p> - <p>b2 <p>b3</p> --> <p>b4</p></p></p>')