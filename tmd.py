"""Some test classes"""


import os,sys
import random

sys.path.insert(0,r"c:\python32\projects\mygit")


class TestClass:
    def __init__(self):
        self.attr1 = 2
        self.attr2 = 10

    def method(self):
        self.attr1 += random.random()



