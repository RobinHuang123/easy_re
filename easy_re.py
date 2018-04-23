r"""An easy way to use re module
If you are a perl user, you must like it.
===In perl, you use the regexp like this.
$s =  "123:abcdefg";
if ($s =~ /'(\d+):([a-z]+)'/) {
    $k = $1;
    $v = $2;
}

===But in re module, it beacomes complex in coding
import re
s = "123:abcdefg"
match =  re.match(r'(\d+):([a-z]+)', s)
if match:
    k = match.group(0)
    v = match.group(1)

===Now, the easy_re will help you
import easy_re
r = easy_re.RE()

s = "123:abcdefg"
if r.m(r'(\d+):([a-z]+)', s):
    k = r.group(0)
    v = r.group(1)

"""



import re
import functools

import sre_compile

class RE(object):
    """An Class for re module"""

    __reMethods__ = [
        "match", "fullmatch", "search", "sub", "subn", "split",
        "findall", "finditer", "compile", "purge", "template", "escape",
        ]

    __matchMethods__ = ['end', 'expand', 'groupdict', 'groups', 'span', 'start']

    # flags
    A = ASCII = sre_compile.SRE_FLAG_ASCII # assume ascii "locale"
    I = IGNORECASE = sre_compile.SRE_FLAG_IGNORECASE # ignore case
    L = LOCALE = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
    U = UNICODE = sre_compile.SRE_FLAG_UNICODE # assume unicode "locale"
    M = MULTILINE = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
    S = DOTALL = sre_compile.SRE_FLAG_DOTALL # make dot match newline
    X = VERBOSE = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments

    def __init__(self):
        self.res = None
        self.__proxy()

    def __proxy(self):
        def getFunc(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                self.res = func(*args, **kw)
                return self.res
            return wrapper

        for method in RE.__reMethods__:
            #self.__dict__[method] = getFunc( re.__dict__[method] )
            setattr(self, method, getFunc( re.__dict__[method] ))

        self.m = self.match
        self.s = self.sub

        return self

    def end(self, *args, **kw):
        return self.res.end(*args, **kw)

    def expand(self, *args, **kw):
        return self.res.expand(*args, **kw)

    def groupdict(self, *args, **kw):
        return self.res.groupdict(*args, **kw)

    def group(self, *args, **kw):
        return self.res.group(*args, **kw)

    def groups(self, *args, **kw):
        return self.res.group(*args, **kw)

    def span(self, *args, **kw):
        return self.res.span(*args, **kw)

    def start(self, *args, **kw):
        return self.res.start(*args, **kw)


if __name__ == '__main__':
    """unit test"""
    r = RE()
    if r.m(r'abc', 'abcd',):
        print(r.group(0))


