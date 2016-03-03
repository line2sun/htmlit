from htmlit.blocks import Block
from htmlit.parsers.block_parsers import InlineBlockParser, HighLevelBlockParser


class MarkdownParser(object):
    def __init__(self):
        pass

    def parse(self, _input):
        if isinstance(_input, Block):
            return self._parse_block(_input)
        else:
            return self._parse_string(_input)

    def _parse_block(self, a_block):
        parser = InlineBlockParser(a_block)
        return parser.run()

    def _parse_string(self, a_string):
        parser = HighLevelBlockParser(a_string)
        return parser.run()
