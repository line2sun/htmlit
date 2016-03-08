import re


EM = r'((\*|_)([.]*?)(.*?)\2)'
BACKTICK = r'((`+)([.]*)(.*)\2)'
STRONG = r'((\*\*|__)([.]*?)(.*?)\2)'
LINK_PATTERN = r'((\[)(.*)(\])(\()(.*)(\))(.*))'
SANITIZE_URL = r'((https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?)'


class PatternReFactory(object):
    def __init__(self, pattern, pattern_name, match_group_id, data_group_ids):
        self.pattern = pattern
        self.name = pattern_name
        self.match_group_id = match_group_id
        self.data_group_ids = data_group_ids

    def findall(self, _str):
        self.match = self.pattern.findall(_str)
        return self.match


INLINE_PATTERN_POOL = [
    PatternReFactory(re.compile(SANITIZE_URL, re.MULTILINE), 'url', 0, (0,)),
    PatternReFactory(re.compile(BACKTICK, re.MULTILINE), 'backtick', 0, (3,)),
    PatternReFactory(re.compile(EM, re.MULTILINE), 'em', 0, (3,)),
    PatternReFactory(re.compile(STRONG, re.MULTILINE), 'strong', 0, (3,)),
    PatternReFactory(re.compile(LINK_PATTERN, re.MULTILINE), 'link', 0, (2, 5)),
]

if __name__ == '__main__':
    a = re.findall(LINK_PATTERN, 'Let me put a bold link: [**stuff**]('
                                  'http://41.media.tumblr.com/49a58542fd70b8ca39b5bd0d9c9c53aa/'
                                  'tumblr_nob40mvTN41tb9nzio1_500.jpg)')

    print a
    b = a[0]

    print b[0]
