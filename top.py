"""top module"""

import os,sys

sys.path.insert(0,r"c:\python32\projects\mygit")

from tmd import TestClass

t = TestClass()

for i in range(3):
    t.method()

print (t.attr1)