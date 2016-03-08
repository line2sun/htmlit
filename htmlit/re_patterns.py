import re


STRONG = r'((\*\*|__)([.]*?)(.*?)\2)'
EM     = r'((\*|_)([.]*?)(.*?)\2)'

INLINE_PATTERN_POOL = [
    (re.compile(EM, re.MULTILINE), 'em', 1, 3),
    (re.compile(STRONG, re.MULTILINE), 'strong', 1, 3)
]



if __name__ == '__main__':
    strong = re.compile(STRONG)
    print re.findall(STRONG, 'A paragraph with **f*irst***  and **second** strong *emphasis*.')