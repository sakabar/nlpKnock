#encode: utf-8

import sys

print len(list(set(map((lambda l: l.split('\t')[0]), sys.stdin.readlines()))))
