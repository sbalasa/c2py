import sys

from ctypes import CDLL

f = CDLL(sys.argv[1])
print(f.hello())
