from htmlit.exceptions import ExecutionError
from htmlit.html_tags import BaseHTMLTag


class Block:

    def __init__(self, _input=None):                           # ToDo: Make sure that the initialization is well tested.
        if isinstance(_input, self.__class__):
            self.data = _input.data
            self.html_tag = _input.html_tag
            self.inline_blocks = _input.inline_blocks
        elif isinstance(_input, basestring):
            self.data = _input
            self.inline_blocks = []
            self.html_tag = None
        elif _input is None:
            self.data = None
        else:
            raise ValueError

    def set_html_tag(self, _tag=None):
        if not issubclass(_tag.__class__, BaseHTMLTag):
            raise ValueError

        self.html_tag = _tag

    def __str__(self):
        return self.data

    def has_inline(self):
        if self.inline_blocks:
            return True

        return False

    def to_str(self):
        if not self.has_inline():
            return self.html_tag.get_html_repr(self.data)

        # Make sure that all inline blocks are eliminated and the data attribute is up to date.
        try:
            self._format_inlines()
        except ExecutionError as e:
            print e.message
            exit(1)
        return self.to_str()

    def _format_inlines(self):
        """ Make sure that the use of this method is wrapped in a try block.
        In case that it returns, the data of current block is ready to be converted to html.
        In case that ExecutionError was raised the program execution will terminate with 1.
        """
        if not self.has_inline():
            raise ExecutionError(message='Make sure that inline blocks are processed.')  # ToDo: This is confusing me!

        # Format the data. at this point all inline blocks are not nested, hopefully.
        tmp = [block.to_str() for block in self.inline_blocks]
        self.data = self.data % tuple(tmp)
        self.inline_blocks = []

        return 0


if __name__ == '__main__':
    from htmlit.html_tags import Paragraph
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

    print b.has_inline()
    print b1.has_inline()
    print b2.has_inline()
    print b3.has_inline()
    print b4.has_inline()

    print b.to_str()
