from .block_parsers import InlineBlockParser, HighLevelBlockParser


class MarkdownParser(object):
    def __init__(self):
        self._high_level_parser = HighLevelBlockParser()
        self._inline_parser = InlineBlockParser()

    def run(self, _input):
        high_level_blocks = []

        if isinstance(_input, basestring):
            high_level_blocks = self._high_level_parser.parse(_input=_input)

        for block in high_level_blocks:
            block = self._inline_parser.parse(block)

        return [block.to_str() for block in high_level_blocks]

