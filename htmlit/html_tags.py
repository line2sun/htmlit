

class BaseHTMLTag(object):
    """ This class represents an HTML Tag.
      The main purpose of all HTMLTag classes
    is to handle the string representation of tags.

      All HTMLTag classes will inherit from BaseHTMLTag,
    and override the .get_html_repr() method if needed.
    """
    HTML_OPEN_REPR = ''
    HTML_CLOSE_REPR = ''

    def __init__(self):
        pass

    def get_html_repr(self, text=None):
        return self.HTML_OPEN_REPR + text + self.HTML_CLOSE_REPR

    def __unicode__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.__unicode__()


class Header(BaseHTMLTag):
    def __init__(self, level=None):
        super(Header, self).__init__()
        self.HTML_OPEN_REPR = '<h%s>'
        self.HTML_CLOSE_REPR = '</h%s>'
        self._level = None
        self.set_level(level)

    def set_level(self, level):
        if level<1 or level>6:
            raise ValueError
        self._level = level

    def level(self):
        return self._level

    def get_html_repr(self, text=None):
        html_repr = self.HTML_OPEN_REPR % self.level() + text + \
            self.HTML_CLOSE_REPR % self.level()
        return html_repr


class Paragraph(BaseHTMLTag):
    def __init__(self):
        super(Paragraph, self).__init__()
        self.HTML_OPEN_REPR = '<p>'
        self.HTML_CLOSE_REPR = '</p>'


class Code(BaseHTMLTag):
    def __init__(self):
        super(Code, self).__init__()
        self.HTML_OPEN_REPR = '<code>'
        self.HTML_CLOSE_REPR = '</code>'


class Strong(BaseHTMLTag):
    def __init__(self):
        super(Strong, self).__init__()
        self.HTML_OPEN_REPR = '<strong>'
        self.HTML_CLOSE_REPR = '</strong>'


class Em(BaseHTMLTag):
    def __init__(self):
        super(Em, self).__init__()
        self.HTML_OPEN_REPR = '<em>'
        self.HTML_CLOSE_REPR = '</em>'


class URL(BaseHTMLTag):
    def __init__(self):
        super(URL, self).__init__()
        self.HTML_OPEN_REPR = ''
        self.HTML_CLOSE_REPR = ''


class Anchor(BaseHTMLTag):
    def __init__(self):
        super(Anchor, self).__init__()
        self.HTML_OPEN_REPR = '<a%s>'
        self.HTML_CLOSE_REPR = '</a>'

    def get_html_repr(self, text=None):
        data, url = text.split('::')
        result = self.HTML_OPEN_REPR % (' href=' + url)
        result += data + self.HTML_CLOSE_REPR
        return result


INLINE_HTML_TAG_NAME_MAP = {
    'em': Em,
    'strong': Strong,
    'backtick': Code,
    'url': URL,
    'link': Anchor,
}