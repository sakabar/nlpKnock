#coding: utf-8
import sys

def main():
  if len(sys.argv) == 2:
    num = int(sys.argv[1])

#readlines()をreadline()とtypoしたところ、動くには動いた
#1行読みとって、そのi文字目を出力しようとしてしまったようだ
#静的チェックではじきたいなあ

    ar = sys.stdin.readlines()
    for i in range(0,num):
      print ar[i],
   


if __name__ == '__main__':
  main()
