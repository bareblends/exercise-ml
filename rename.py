import sys
import string
import os
import random

def rn(File):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(5))
    final = "%s.png" % result_str
    os.rename(File, final)

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            rn(arg)
