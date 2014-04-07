#coding: utf-8
import sys

def main():
  if len(sys.argv) == 2:
    num = int(sys.argv[1])

    ar = sys.stdin.readlines()
    l = len(ar)
    for i in range(len(ar)-num,len(ar)):
      print ar[i],
   


if __name__ == '__main__':
  main()

