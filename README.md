### An easy way to use re module
If you are a perl user, you must like it.

In perl, you use the regexp like this.
```perl
$s =  "123:abcdefg";
if ($s =~ /'(\d+):([a-z]+)'/) {
    $k = $1;
    $v = $2;
}
```
---------------------------------------
But in re module, it beacomes complex in coding
```python
import re
s = "123:abcdefg"
match =  re.match(r'(\d+):([a-z]+)', s)
if match:
    k = match.group(0)
    v = match.group(1)
```
---------------------------------------
Now, the easy_re will help you
```python
import easy_re
r = easy_re.RE()

s = "123:abcdefg"
if r.m(r'(\d+):([a-z]+)', s):
    k = r.group(0)
    v = r.group(1)
```
---------------------------------------
