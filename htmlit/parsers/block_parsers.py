from htmlit.blocks import Block


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
        return []


class InlineBlockParser(BaseBlockParser):
    def validate_input(self, _input):
        if (not isinstance(_input, Block)) and (_input is not None):
            raise ValueError

        return _input

    def run(self):
        return ['I guesss']
