# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby
import sys

for key, group in groupby(input()):
    print((len(list(group)), int(key)), end=' ')





