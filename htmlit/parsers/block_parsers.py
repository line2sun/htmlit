import re
from htmlit.blocks import Block
from htmlit.html_tags import Paragraph, Header, Code, INLINE_HTML_TAG_NAME_MAP
from htmlit.re_patterns import INLINE_PATTERN_POOL


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

            if line.startswith('#') and not current_block:
                current_block += line
                level = current_block.rfind('#')+1
                current_block = current_block[level:]
                block = Block(current_block)
                block.set_html_tag(Header(level=level))
                result.append(block)
                current_block = ''
                continue
            elif line.startswith('#') and current_block:
                block = Block(current_block)
                block.set_html_tag(Paragraph())
                result.append(block)
                current_block = line
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
        """
        :return: a list of Block objects.
        """
        inp_block = self._input

        for pattern in INLINE_PATTERN_POOL:

            # print inp_block                               # To see each stage of parsing uncomment this.
            _new_inline_blocks, _new_data = self._inline_parse(pattern, inp_block)
            if _new_inline_blocks:
                inp_block.data = _new_data
                inp_block.inline_blocks = _new_inline_blocks

        return inp_block

    @staticmethod
    def _inline_parse(pattern, _block):
        result = []

        matches = pattern.findall(_block.data)

        _new_block_data = _block.data
        # print 'MATCHES: ', matches

        for match in matches:
            # print 'FILTER: ', filter(lambda e: len(e) > 0, map(lambda l: match[l], pattern.data_group_ids))
            if filter(lambda e: len(e) > 0, map(lambda l: match[l], pattern.data_group_ids)):

                _sub_match_pattern = match[pattern.match_group_id]
                # print 'SUB_MATCH_PATTERN: ', _sub_match_pattern

                _new_block_data = _block.data.replace(_sub_match_pattern, '%s')
                _block.data = _new_block_data
                _new_data = '::'.join(map(str, map(lambda e: match[e], pattern.data_group_ids)))
                # print '_NEW_DATA: ', _new_data
                _new_block = Block(_new_data)
                _new_block.set_html_tag(INLINE_HTML_TAG_NAME_MAP[pattern.name]())

                occ = len(re.findall('%s', _new_data))
                # print 'OCC: ', occ
                if occ > 0:
                    _new_block.inline_blocks = _block.inline_blocks[:occ]
                    _block.inline_blocks = _block.inline_blocks[occ:]
                result.append(_new_block)
        result += _block.inline_blocks
        # print '---------------> NEW_DATA: ', _new_block_data
        return result, _new_block_data

if __name__ == '__main__':
    inp_path = '/Users/line2sun/test1/in.md'

    with open(inp_path, 'r') as _file:
        inp = _file.read()

    hbp = HighLevelBlockParser(_input=inp)
    ibp = InlineBlockParser()
    high_level_blocks = hbp.run()

    for item in high_level_blocks:
        item = ibp.parse(_input=item)

    for inliner in high_level_blocks:
        print inliner.to_str()


    # data = 'fancy **strong _em_ and *another em with `code` emphasis*** plus **str_on_g** text.'
    # _input = Block(data)
    # _input.set_html_tag(Paragraph())
    # ibp = InlineBlockParser()
    # print ibp.parse(_input=_input).to_str()
