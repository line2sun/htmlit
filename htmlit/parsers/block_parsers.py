from htmlit.blocks import Block
from htmlit.html_tags import *


class BaseBlockParser(object):
    def __init__(self, _input=None):
        self._input = self.validate_input(_input)

    def parse(self, _input):
        """ Use .parse() to reuse the instances of the parser."""
        self._input = self.validate_input(_input)
        return self.run()

    def validate_input(self, _input):
        raise NotImplemented

    def run(self):
        raise NotImplemented


class HighLevelBlockParser(BaseBlockParser):
    def validate_input(self, _input):
        if (not isinstance(_input, basestring)) and (_input is not None):
            raise ValueError
        return _input

    def run(self):
        result = []
        inp_str = self._input.split('\n')
        current_block = ''

        for line in inp_str:
            if line.startswith('#'):
                current_block += line
                level = current_block.rfind('#')+1
                current_block = current_block[level:]
                block = Block(current_block)
                block.set_html_tag(Header(level=level))
                result.append(block)
                current_block = ''
                continue

            elif line.startswith('```')and not current_block:
                current_block += line

            elif line.startswith('```') and current_block:
                current_block += line
                current_block = current_block[3:-3]
                block = Block(current_block)
                block.set_html_tag(Code())
                result.append(block)
                current_block = ''
                continue

            elif line == '' and current_block:
                block = Block(current_block)
                block.set_html_tag(Paragraph())
                result.append(block)
                current_block = ''
                continue
            elif line == '' and not current_block:
                continue
            else:
                current_block += line + '\n'

        return result


class InlineBlockParser(BaseBlockParser):
    def validate_input(self, _input):
        if (not isinstance(_input, Block)) and (_input is not None):
            raise ValueError

        return _input

    def run(self):

        return []

if __name__ == '__main__':
    inp_path = '/Users/line2sun/test1/in.md'

    with open(inp_path, 'r') as _file:
        inp = _file.read()

    hbp = HighLevelBlockParser(_input=inp)
    for item in hbp.run():
        print item

