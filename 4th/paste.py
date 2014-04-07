#coding: utf-8
import sys

def main():
  delim = '\t'

  if len(sys.argv) == 3:
    f2 = open(sys.argv[2], 'r') # b.txt

  for line in open(sys.argv[1], 'r'): 
    sys.stdout.write(line.rstrip())
    sys.stdout.write(delim)
    print f2.readline()

if __name__ == '__main__':
  main()
