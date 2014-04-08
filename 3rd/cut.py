#coding: utf-8
import sys

# コマンドライン引数で区切り文字と何列目を抜き出すかを指定する
# $python cut.py '\t' 1


#既知のバグ 1
#delimでタブ文字を指定しても、うまくいかない。

#既知のバグ 2
#パイプでつなぐとエラーになる(broken pipe)
# $python cut.py < hoge.txt | head -n 10


def main():
  if len(sys.argv) == 3:
    delim = sys.argv[1] # '\t'
    col = int(sys.argv[2]) # 1

    if col >= 1:
      for line in sys.stdin:
#        arr = line.split(delim)
        arr = line.rstrip().split('\t')
        print arr[col-1]

if __name__ == '__main__':
  main()
